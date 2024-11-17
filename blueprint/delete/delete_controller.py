from flask import render_template, request, current_app, redirect, url_for
from bson import ObjectId  # Để xử lý ObjectId của MongoDB
from helper.infoTopCustomer import countUser, countUserPurchases, userMax

def delCustomer(id):
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.users 

    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))

    if id:
        collection.delete_one({"_id": ObjectId(id)})
    #----------------------
    return redirect(url_for('customer.home_route', page=page))
    

def delProduct(id):
    #Không được xoá đoạn duới này, đoạn dưới là code để chia thành các trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.products  

    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))
    #No delete code-------
    if id:
        collection.delete_one({"_id": ObjectId(id)})
    #----------------------
    return redirect(url_for('product.home_route', page=page))


def delOrder(id):
    #code phan chia thanh cac trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit
    collection = mongo.db.orders
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))
    #No delete code-------
    if id:
        collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('order.home_route', page=page))
