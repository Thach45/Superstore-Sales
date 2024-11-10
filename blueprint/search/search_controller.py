from flask import Flask, render_template, request , current_app
from pymongo import MongoClient

def home():
    # Lấy tham số 'Name' từ URL và chuyển về chữ thường
    search_name = request.args.get('Name', '').lower()

    # Truy cập collection MongoDB sử dụng cấu hình của ứng dụng Flask
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Truy cập collection 'users' trong MongoDB

    # Bước 1: Nếu có tham số tìm kiếm, thực hiện tìm kiếm không phân biệt chữ hoa, chữ thường trong trường 'Name'
    if search_name:
        query = {"Name": {"$regex": search_name, "$options": "i"}}  # Tìm kiếm không phân biệt chữ hoa, chữ thường bằng biểu thức chính quy
        data = list(collection.find(query))  # Tìm những người dùng phù hợp với truy vấn tìm kiếm
    else:
        data = list(collection.find())  # Trả về tất cả người dùng nếu không có tham số tìm kiếm

    # Bước 2: Render template 'customer.html' và truyền dữ liệu vào template
    return render_template("customer.html", records=data)
