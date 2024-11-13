from flask import render_template, request, current_app
import pandas as pd

def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Sử dụng cú pháp dấu chấm để truy cập collection
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

    total_purchases = countUserPurchases(collection)

    return render_template('customer.html', records=data, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=total_purchases, user=userMax(collection))

def countUser(collection):  
    unique_names = collection.distinct("Name")  # Dùng hàm có sẵn distinct để tối ưu
    return len(unique_names)

def countUserPurchases(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$Name",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = max(total_purchases.values())
    return max_purchases
def userMax(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$Name",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
    user = max_purchases[0][0]
    return user