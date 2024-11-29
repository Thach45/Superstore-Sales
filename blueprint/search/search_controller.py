from flask import Flask, render_template, request , current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser,countUserPurchases,userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
from helper.DateOrder import MonthYearOrder, MonthYearShip
from helper.Customer import CustomerState, CustomerCity
def SearchCustomer():
    """Lấy ra tất cả các tên hoặc ID của người dùng có liên quan đến từ khoá"""
    search_IDCustomer= request.args.get('IDCustomer','').lower()
    # Lấy tham số 'Name' từ URL và chuyển về chữ thường
    search_name = request.args.get('Name', '').lower()

    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    states = CustomerState(collection)
    cities = CustomerCity(collection)
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    
    # Bước 1: Nếu có tham số tìm kiếm, thực hiện tìm kiếm không phân biệt chữ hoa, chữ thường trong trường 'Name'
    if '-' not in search_name:
        if search_name:
            query = {"Name": {"$regex": search_name, "$options": "i"}}  # Tìm kiếm không phân biệt chữ hoa, chữ thường bằng biểu thức chính quy
            data = list(collection.find(query).skip(skip).limit(limit)) 
        else:
            data = list(collection.find().skip(skip).limit(limit))
    if '-' in search_IDCustomer:
        if search_IDCustomer:
            query = {"IDCustomer":{"$regex": search_IDCustomer, "$options": "i"}}
            data = list(collection.find(query).skip(skip).limit(limit))
        else:
            data = list(collection.find().skip(skip).limit(limit))
    
    # Bước 2: Render template 'customer.html' và truyền dữ liệu vào template
    total_records = collection.count_documents(query if search_name else {})  # Đếm số người dùng phù hợp với truy vấn tìm kiếm
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    return render_template("customer.html", 
                           records=data, 
                           page=page, 
                           total_pages=total_pages,
                           totalUser=countUser(collection), 
                           totalPurchases=countUserPurchases(collection), 
                           user=userMax(collection),
                           states=states,
                           cities=cities)

def SearchProduct():
    """Lấy ra tên tất cả sản phẩm có liên quan đến từ khoá"""
    search_ProductName = request.args.get('ProductName', '').lower()

    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    if search_ProductName:
            query = {"ProductName": {"$regex": search_ProductName, "$options": "i"}} 
            data = list(collection.find(query).skip(skip).limit(limit))
    else:
            data = list(collection.find().skip(skip).limit(limit))
    
    total_records = collection.count_documents(query if search_ProductName else {})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    return render_template("product.html", records=data, page=page, total_pages=total_pages,totalProduct=countProduct(collection), totalPurchases=countProductPurchases(collection), product=productMax(collection))

def SearchOrder():
    """Lấy ra tất cả order ID của đơn hàng có liên quan đến từ khoá"""
    search_OrderID = request.args.get('OrderID', '').lower()
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    page = int(request.args.get('page', 1))
    monthYearOrder = MonthYearOrder(collection)
    monthYearShip = MonthYearShip(collection)
    limit = 20
    skip = (page - 1) * limit 
    if search_OrderID:
            query = {"OrderID": {"$regex": search_OrderID, "$options": "i"}} 
            data = list(collection.find(query).skip(skip).limit(limit)) 
    else:
            data = list(collection.find().skip(skip).limit(limit))  
    
    
    total_records = collection.count_documents(query if search_OrderID else {}) 
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    return render_template("order.html", records=data, page=page, 
                           total_pages=total_pages,totalOrder=countOrder(collection),
                           totalPurchases=countOrderPurchases(collection), order=orderMax(collection),
                           MonthYearOrder=monthYearOrder,
                           MonthYearShip=monthYearShip)