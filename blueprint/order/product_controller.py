from flask import render_template, request, current_app
import pandas as pd
from helper.infoTopCustomer import countUser, countUserPurchases, userMax

def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders  # Sử dụng cú pháp dấu chấm để truy cập collection
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    # Bước 1: Lấy dữ liệu từ MongoDB
    data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả dữ liệu từ collection
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    # Bước 2: Chuyển đổi đối tượng ObjectId thành chuỗi (nếu có)
    for item in data:
        item['_id'] = str(item['_id'])


    return render_template('order.html', records=data, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))

