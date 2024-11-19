from flask import render_template, current_app, url_for
from flask import jsonify
import os
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')

def format_number(number, decimal_places=2):
    # Nếu input là số, đảm bảo là chuỗi trước khi loại bỏ dấu phẩy
    if isinstance(number, (int, float)):
        number_str = str(number) 
    else:
        # Nếu đầu vào là chuỗi, kiểm tra có dấu phẩy hay không
        number_str = number.replace(",", "")  

    # Chuyển chuỗi đã chuẩn hóa thành float
    number = float(number_str)

    # Trả về chuỗi đã được định dạng
    return f"{number:,.{decimal_places}f}"

def format_number1(number, decimal_places=2):
    # Nếu input là số, đảm bảo là chuỗi trước khi loại bỏ dấu phẩy
    if isinstance(number, (int)):
        number_str = str(number) 
    else:
        # Nếu đầu vào là chuỗi, kiểm tra có dấu phẩy hay không
        number_str = number.replace(",", "")  

    # Chuyển chuỗi đã chuẩn hóa thành float
    number = int(number_str)

    # Trả về chuỗi đã được định dạng
    return f"{number}"


def home():
    
    mongo = current_app.config['MONGO'] ####
    
    # Dữ liệu mẫu
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1700]

    # Tạo biểu đồ
    plt.figure(figsize=(10, 5))
    plt.fill_between(month, sales, color="skyblue", alpha=0.4)
    plt.plot(month, sales, color="Slateblue", alpha=0.6)
    image_path = os.path.join(current_app.root_path, 'static', 'images', 'sales.png')
    plt.savefig(image_path)
    plt.close()
    #tạo biểu đồ tròn
    labels = ['A', 'B', 'C', 'D']
    values = [20, 30, 40, 10]
    plt.figure(figsize=(3, 3))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title('Các cách vận chuyển')
    image_path = os.path.join(current_app.root_path, 'static', 'images', 'pie.png')
    plt.savefig(image_path)
    plt.close()
    
    image_url_pie = url_for('static', filename='images/revenue_structure_by_category.png')
    image_url_plot = url_for('static', filename='images/monthly_revenue_per_year.png')
    
    collection = mongo.db.datastore
    
    #tổng doanh thu
    total_sales = collection.aggregate([
        {
            '$group': {
                '_id': None,  # Không phân nhóm, tính tổng cho tất cả các phần tử
                'total_sales': {'$sum': '$Sales'}  # Tính tổng trường 'sale'
            }
        }
    ])
    total_sales_result = list(total_sales)  # Chuyển CommandCursor thành danh sách
    total_sales_value = total_sales_result[0]['total_sales']
    total_sales_value = format_number(total_sales_value)
    
    #đếm số đơn hàng
    oders = collection.distinct("OrderID")
    oders_count = format_number1(len(oders))
    
    #sản phẩm gần nhất
    pipeline = [
    # Chuyển đổi trường "OrderDate" từ chuỗi thành datetime (nếu cần thiết)
    {
        '$addFields': {
            'OrderDate': {
                '$dateFromString': {
                    'dateString': '$OrderDate',
                    'format': '%d/%m/%Y'
                }
            }
        }
    },
    # Sắp xếp các bản ghi theo "OrderDate"
    {
        '$sort': {
            'OrderDate': -1  # Sắp xếp theo thứ tự tăng dần (1) hoặc giảm dần (-1)
        }
    },
    # Giới hạn số lượng bản ghi trả về là 3
    {
        '$limit': 3
    },
    # Chọn các trường bạn muốn (nếu cần thiết)
    {
        '$project': {
            'OrderID': 1,
            'CustomerName': 1,
            'Sales': 1,
            'OrderDate': 1,
            'ProductName': 1
        }
    }
]
    # Thực thi aggregate pipeline
    recent_products = collection.aggregate(pipeline)
    list_recent = []
    for i in recent_products:
        list_recent.append([i['OrderID'],i['CustomerName'],i['ProductName'],i['Sales']])
    
     
    # đếm số người mua

    collection = mongo.db.users
    customer = collection.distinct("IDCustomer")
    Count_customer = format_number1(len(customer))
    
    #top bán chạy
    collection = mongo.db.products
    pipeline = [
    {
        '$sort': {
            'Quantity': -1 
        }
    },
    # Giới hạn số lượng bản ghi trả về là 3
    {
        '$limit': 3
    },
    # Chọn các trường bạn muốn (nếu cần thiết)  
    {
        '$project': {
            'Quantity': 1,
            'ProductName': 1,
            'Sales': 1,
        }
    }
    
]
    top_products = collection.aggregate(pipeline)
    list_products = []
    for i in top_products:
        product_sales = float(i['Sales']) * int(i['Quantity'])
        list_products.append([i['ProductName'],format_number1(i['Quantity']),product_sales])

    
    
    
    return render_template('dashboard.html', image_url_plot=image_url_plot, image_url_pie=image_url_pie , 
                                            totalsale = total_sales_value, oderscount = oders_count
                                            ,countcustomer = Count_customer,listrecent = list_recent
                                            ,listproducts = list_products)
    
    