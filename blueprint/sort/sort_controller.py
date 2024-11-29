from flask import request, jsonify, render_template, current_app
from flask_pymongo import PyMongo as mongo
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
from helper.DateOrder import MonthYearOrder, MonthYearShip
from helper.Customer import CustomerState, CustomerCity
def SortCustomer():
    """Sắp xếp khách hàng theo trường Quantity"""

    mongo = current_app.config['MONGO']

    # Lấy thông tin sắp xếp (tăng dần hoặc giảm dần) từ tham số URL
    sort_quantity = request.args.get('sort') 

    # Kiểm tra tính hợp lệ của tham số sắp xếp
    if sort_quantity not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    # Quy đổi tham số sắp xếp thành giá trị MongoDB: 1 (tăng dần), -1 (giảm dần)
    mongo_quantity = 1 if sort_quantity == 'asc' else -1

     # Phân trang
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 

     # Truy vấn collection "users"
    collection = mongo.db.users
    states = CustomerState(collection)
    cities = CustomerCity(collection)
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)

     # Thực hiện truy vấn MongoDB để lấy dữ liệu đã sắp xếp và phân trang
    sorted_quantity = list(collection.find().sort("Quantity", mongo_quantity).skip(skip).limit(limit))
    return render_template("customer.html",
                           records=sorted_quantity, 
                           page=page, 
                           total_pages=total_pages, 
                           totalUser=countUser(collection), 
                           totalPurchases=countUserPurchases(collection), 
                           user=userMax(collection), 
                           states=states, 
                           cities=cities)
    
def SortProduct():
    """Sắp xếp sản phẩm theo trường Quantity hoặc Revenue"""

    mongo = current_app.config['MONGO']

    # Lấy trường cần sắp xếp từ tham số URL, mặc định là 'Quantity'
    sort_field = request.args.get('field', 'Quantity')
    sort_product = request.args.get('sort') 

    if sort_product not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_product = 1 if sort_product == 'asc' else -1
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 

     # Truy vấn collection "products"
    collection = mongo.db.products
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)

    Sorted_product = list(collection.find().sort(sort_field, mongo_product).skip(skip).limit(limit))
    return render_template("product.html",records=Sorted_product, page=page, total_pages=total_pages,
                           totalProduct=countProduct(collection), 
                           totalPurchases=countProductPurchases(collection), 
                           product=productMax(collection))

def SortOrder():
    """Sắp xếp đơn hàng theo trường Costs hoặc Frequency"""

    mongo = current_app.config['MONGO']

    # Lấy trường cần sắp xếp từ tham số URL, mặc định là 'Frequency'
    sort_field = request.args.get('field', 'Frequency')
    sort_order = request.args.get('sort') 
    monthYearOrder = MonthYearOrder(mongo.db.orders)
    monthYearShip = MonthYearShip(mongo.db.orders)
    if sort_order not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_order = 1 if sort_order == 'asc' else -1
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 

    # Truy vấn collection "orders"
    collection = mongo.db.orders
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    Sorted_order = list(collection.find().sort(sort_field, mongo_order).skip(skip).limit(limit))

    return render_template("order.html",records=Sorted_order, 
                           page=page, 
                           total_pages=total_pages,
                           totalOrder=countOrder(collection), 
                           totalPurchases=countOrderPurchases(collection), 
                           order=orderMax(collection),
                           MonthYearOrder=monthYearOrder,
                           MonthYearShip=monthYearShip)
