from flask import render_template, request, current_app
import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import OrderedDict
from helper.infoTopOrder import countOrder, countOrderPurchases, orderMax
from helper.DateOrder import MonthYearOrder, MonthYearShip
def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders

    page = int(request.args.get('page', 1))
    limit = 20
    monthYearOrder = MonthYearOrder(collection)
    monthYearShip = MonthYearShip(collection)
    skip = (page - 1) * limit 
    orderDate = list(collection.find({},{"OrderDate":1,"Frequency":1,"_id":0}))
    orderDate = pd.DataFrame(orderDate)
    orderDate['OrderDate'] = pd.to_datetime(orderDate['OrderDate'], format='%d/%m/%Y')
    orderDate['Year'] = orderDate['OrderDate'].dt.year
    orderDate['Month'] = orderDate['OrderDate'].dt.month

    order_frequency = orderDate.groupby(['Year', 'Month'])['Frequency'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    for year in order_frequency['Year'].unique():
        yearly_data = order_frequency[order_frequency['Year'] == year]
        plt.plot(yearly_data['Month'], yearly_data['Frequency'], marker='o', linestyle='-',linewidth=4, label=str(year))

    plt.xticks(range(1, 13))
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.title('Order Frequency by Year')
    plt.legend(title='Year')
    plt.tight_layout()
    plt.savefig(os.path.join(current_app.root_path, 'static', 'images', 'order_frequency.png'))
    plt.close()

    # Bước 1: Lấy dữ liệu từ MongoDB
    data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả dữ liệu từ collection
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    # Bước 2: Chuyển đổi đối tượng ObjectId thành chuỗi (nếu có)
    for item in data:
        item['_id'] = str(item['_id'])


    return render_template('order.html',
                            records=data, 
                            page=page, 
                            total_pages=total_pages, 
                            totalOrder=countOrder(collection), 
                            totalPurchases=countOrderPurchases(collection), 
                            order=orderMax(collection),
                            MonthYearOrder=monthYearOrder,
                            MonthYearShip=monthYearShip)

