from flask import render_template, current_app, url_for
from flask import jsonify
from helper.infoTopOrder import countOrder
from helper.infoTopCustomer import countUser
from helper.infoTopDashboard import TopProduct,TopRecent,TotalSales
import os
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')


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
    
    image_url_pie = url_for('static', filename='images/pie.png')
    image_url_plot = url_for('static', filename='images/sales.png')
    
    collection = mongo.db.datastore 
    #tổng doanh thu
    total_sales_value = TotalSales(collection)
    #top 3 sản phẩm gần đây
    list_recent = TopRecent(collection)
    
    collection = mongo.db.users
    #đếm số customer
    count_customer = countUser(collection)
    
    collection = mongo.db.products
    #top 3 sản phẩm bán chạy
    list_products = TopProduct(collection)

    collection = mongo.db.orders
    #đếm số đơn hàng
    orders_count = countOrder(collection) 
    
    return render_template('dashboard.html', image_url_plot=image_url_plot, image_url_pie=image_url_pie , 
                                            totalsale = total_sales_value, orderscount = orders_count
                                            ,countcustomer = count_customer,listrecent = list_recent
                                            ,listproducts = list_products)
    
    