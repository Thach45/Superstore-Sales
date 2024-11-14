from flask import Flask, render_template, request , current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
def home():
    
    search_IDCustomer= request.args.get('IDCustomer','').lower()
    # Lấy tham số 'Name' từ URL và chuyển về chữ thường
    search_name = request.args.get('Name', '').lower()

    # Truy cập collection MongoDB sử dụng cấu hình của ứng dụng Flask
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Truy cập collection 'users' trong MongoDB
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    
    # Bước 1: Nếu có tham số tìm kiếm, thực hiện tìm kiếm không phân biệt chữ hoa, chữ thường trong trường 'Name'
    if '-' not in search_name:
        if search_name:
            query = {"Name": {"$regex": search_name, "$options": "i"}}  # Tìm kiếm không phân biệt chữ hoa, chữ thường bằng biểu thức chính quy
            data = list(collection.find(query).skip(skip).limit(limit))  # Tìm những người dùng phù hợp với truy vấn tìm kiếm
        else:
            data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả người dùng nếu không có tham số tìm kiếm
    if '-' in search_IDCustomer:
        if search_IDCustomer:
            query = {"IDCustomer":{"$regex": search_IDCustomer, "$options": "i"}}
            data = list(collection.find(query).skip(skip).limit(limit))
        else:
            data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả người dùng nếu không có tham số tìm kiếm
    
    # Bước 2: Render template 'customer.html' và truyền dữ liệu vào template
    total_records = collection.count_documents(query if search_name else {})  # Đếm số người dùng phù hợp với truy vấn tìm kiếm
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    return render_template("customer.html", records=data, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))
