from flask import render_template, current_app, url_for
from flask import jsonify
from helper.infoTopOrder import countOrder
from helper.infoTopCustomer import countUser
from helper.infoTopDashboard import TopProduct,TopRecent,TotalSales
import os
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')


def home():
    
    mongo = current_app.config['MONGO'] ####
    collection = mongo.db.orders
    # Dữ liệu mẫu
    orderDate = list(collection.find({},{"OrderDate":1,"TotalCost":1,"_id":0}))
    orderDate = pd.DataFrame(orderDate)
    orderDate['OrderDate'] = pd.to_datetime(orderDate['OrderDate'], format='%d/%m/%Y')
    orderDate['Year'] = orderDate['OrderDate'].dt.year
    orderDate['Month'] = orderDate['OrderDate'].dt.month
    orderDate['TotalCost'] = pd.to_numeric(orderDate['TotalCost'], errors='coerce')
    order_frequency = orderDate.groupby(['Year', 'Month'])['TotalCost'].sum().reset_index()
    yearTotalCost = orderDate.groupby('Year')['TotalCost'].sum().reset_index()
    print(yearTotalCost['Year'])
    if not yearTotalCost.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(yearTotalCost['Year'], yearTotalCost['TotalCost'],color='blue',width=0.5,alpha=0.5,edgecolor='black',linewidth=1,)
        plt.xlabel('Year')
        plt.xticks(yearTotalCost['Year'].astype(int))
        plt.ylabel('Total Cost')
        plt.title('Total Cost by Year')
        plt.savefig(os.path.join(current_app.root_path, 'static', 'images', 'sales_year.png'))
        plt.close()
    plt.figure(figsize=(10, 5))
    for year in order_frequency['Year'].unique():
        yearly_data = order_frequency[order_frequency['Year'] == year]
        plt.plot(yearly_data['Month'], yearly_data['TotalCost'], marker='o', linestyle='-',linewidth=3, label=str(year))

    plt.xticks(range(1, 13))
    plt.xlabel('Month')
    plt.ylabel('Total Cost')
    plt.title('Total Cost by Year')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(os.path.join(current_app.root_path, 'static', 'images', 'sales.png'))
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
    
    