from flask import render_template, request, current_app, redirect, url_for, flash
from bson import ObjectId  # Để xử lý ObjectId của MongoDB
from helper.infoTopCustomer import countUser, countUserPurchases, userMax

def delCustomer(id):
    """Xóa khách hàng theo ID"""

    # Code phân chia thành các trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.users 

    
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))

    # Xóa khách hàng nếu ID hợp lệ
    if id:
        collection.delete_one({"_id": ObjectId(id)})
        flash('Khách hàng đã được xóa thành công!', 'success')
    else:
        flash('Không tìm thấy khách hàng để xóa.', 'error')
    
    # Chuyển hướng về trang khách hàng sau khi xóa
    return redirect(url_for('customer.home_route', page=page))
    

def delProduct(id):
    """Xóa sản phẩm theo ID"""

    # Code phân chia thành các trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.products  

    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))

    # Xóa sản phẩm nếu ID hợp lệ
    if id:
        collection.delete_one({"_id": ObjectId(id)})
        flash('Sản phẩm đã được xóa thành công!', 'success')
    else:
        flash('Không tìm thấy sản phẩm để xóa.', 'error')

    # Chuyển hướng về trang sản phẩm sau khi xóa
    return redirect(url_for('product.home_route', page=page))


def delOrder(id):
    """Xóa đơn hàngtheo ID"""

    # Code phân chia thành các trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit
    collection = mongo.db.orders

    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))

    # Xóa đơn hàng nếu ID hợp lệ
    if id:
        collection.delete_one({"_id": ObjectId(id)})
        flash('Đơn hàng đã được xóa thành công!', 'success')
    else:
        flash('Không tìm thấy đơn hàng để xóa.', 'error')

    # Chuyển hướng về trang đơn hàng sau khi xóa
    return redirect(url_for('order.home_route',page=page))