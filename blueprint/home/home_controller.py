from flask import render_template, current_app, url_for
from flask import jsonify
from helper.infoTopOrder import countOrder,totalRevenue,topRecent
from helper.infoTopCustomer import countUser
from helper.infoTopDashboard import TopProduct
import os
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')


def home():
    """Page home"""
    mongo = current_app.config['MONGO']
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

    if not yearTotalCost.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(yearTotalCost['Year'], yearTotalCost['TotalCost'],color='#99C1A9',width=0.5)
        plt.grid(linestyle ='--',alpha = 0.7)
        plt.xlabel('Year')
        plt.xticks(yearTotalCost['Year'].astype(int))
        plt.ylabel('Total Cost')
        plt.title('Total Cost by Year')
        plt.savefig(os.path.join(current_app.root_path, 'static', 'images', 'sales_year.png'))
        plt.close()

    plt.figure(figsize=(10, 5))
    for year in order_frequency['Year'].unique():
        yearly_data = order_frequency[order_frequency['Year'] == year]
        plt.plot(yearly_data['Month'], yearly_data['TotalCost'], marker='o', linestyle='-',linewidth=2, label=str(year))
    plt.grid(linestyle ='--',alpha = 0.7)
    plt.xticks(range(1, 13))
    plt.xlabel('Month')
    plt.ylabel('Total Cost')
    plt.title('Total Cost by Year')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(os.path.join(current_app.root_path, 'static', 'images', 'sales.png'))
    plt.close()  
    
    collection = mongo.db.users
    #đếm số customer
    count_customer = countUser(collection)
    
    collection = mongo.db.products
    #top 3 sản phẩm bán chạy
    list_products = TopProduct(collection)

    collection = mongo.db.orders
    #đếm số đơn hàng
    orders_count = countOrder(collection) 
    #tổng doanh thu
    total_revenue = totalRevenue(collection)
    #top 3 sản phẩm gần đây
    list_recent = topRecent(collection)
    
    return render_template('dashboard.html',totalsale = total_revenue, orderscount = orders_count
                                            ,countcustomer = count_customer,listrecent = list_recent
                                            ,listproducts = list_products)
    
    