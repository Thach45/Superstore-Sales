from flask import render_template, request, current_app
import pandas as pd

def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Sử dụng cú pháp dấu chấm để truy cập collection
    # Bước 1: Lấy dữ liệu từ MongoDB
    data = list(collection.find())  # Trả về tất cả dữ liệu từ collection
    
    # Bước 2: Chuyển đổi đối tượng ObjectId thành chuỗi (nếu có)
    for item in data:
        item['_id'] = str(item['_id'])
    
    # Bước 3: Trả về dữ liệu dưới dạng JSON
    return render_template('customer.html', records=data)