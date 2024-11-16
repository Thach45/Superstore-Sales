import matplotlib
matplotlib.use('Agg')  # Sử dụng backend không có GUI
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from flask import jsonify, current_app, render_template, url_for
from bson import json_util
from datetime import datetime

def home():
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    data = list(collection.find({}, {
                                    'OrderDate': 1, 
                                    '_id': 0,
                                    'TotalCost': 1
                                    }).limit(10))  # Lấy trường OrderDate và TotalCost, bỏ qua _id

    # Chuyển đổi dữ liệu thành JSON
    month = []
    sales = []
    for item in data:
        # Chuyển đổi OrderDate thành đối tượng datetime với định dạng đúng
        order_date = datetime.strptime(item['OrderDate'], '%d/%m/%Y')
        month.append(order_date)
        sales.append(item['TotalCost'])

    # Tạo biểu đồ
    plt.figure(figsize=(10, 5))
    plt.fill_between(month, sales, color="skyblue", alpha=0.4)
    plt.plot(month, sales, color="Slateblue", alpha=0.6)
    plt.xlabel('Order Date')
    plt.ylabel('Total Cost')
    plt.title('Sales Over Time')

    # Định dạng trục hoành để hiển thị mm/yy
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    # Lưu biểu đồ dưới dạng hình ảnh
    image_path = 'static/images/sales_over_time.png'
    plt.savefig(image_path)
    plt.close()

    # Trả về đường dẫn hình ảnh để hiển thị trên trang web
    return 