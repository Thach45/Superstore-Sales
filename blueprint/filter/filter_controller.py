from flask import render_template, request, current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
from helper.DateOrder import MonthYearOrder, MonthYearShip
from helper.Customer import CustomerState, CustomerCity
from datetime import datetime

def home_Customer():

    filter_city = request.args.get('City', '')
    filter_segment = request.args.get('Segment', '')
    filter_region = request.args.get('Region', '')
    filter_state = request.args.get('State', '')

    
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  
    states = CustomerState(collection)
    cities = CustomerCity(collection)
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    query = {}

    if filter_city:
        city = filter_city.split(',')  
        query["City"] = {"$in": city}  
    if filter_segment:
        query["Segment"] = {"$regex": filter_segment, "$options": "i"}

    if filter_region:
        query["Region"] = {"$regex": filter_region, "$options": "i"}
    if filter_state:
        query["State"] = {"$regex": filter_state, "$options": "i"}
    total_records = collection.count_documents(query)
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find(query).skip(skip).limit(limit))  
    
    return render_template("customer.html", 
                           records=data, 
                           page=page, 
                           total_pages=total_pages, 
                           totalUser=countUser(collection), 
                           totalPurchases=countUserPurchases(collection), 
                           user=userMax(collection),
                           states=states,
                           cities=cities)

def filter_orders():
    filter_orderMonth = request.args.get('OrderMonth', '')
    filter_shipMonth = request.args.get('ShipMonth', '')
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    monthYearOrder = MonthYearOrder(collection)
    monthYearShip = MonthYearShip(collection)  

    query = {}
    and_conditions = []

    # Lọc theo OrderMonth (chỉ lọc theo tháng và năm)
    if filter_orderMonth:
        try:
            # Tách tháng và năm từ định dạng ngày/tháng/năm
            order_month, order_year = map(int, filter_orderMonth.split('/'))
            # Lọc theo tháng và năm sau khi chuyển đổi OrderDate thành kiểu Date
            and_conditions.append({
                "$and": [
                    {"$expr": {"$eq": [{"$month": {"$dateFromString": {"dateString": "$OrderDate", "format": "%d/%m/%Y"}}}, order_month]}},
                    {"$expr": {"$eq": [{"$year": {"$dateFromString": {"dateString": "$OrderDate", "format": "%d/%m/%Y"}}}, order_year]}}
                ]
            })
        except ValueError:
            pass  # Nếu định dạng không hợp lệ, không làm gì cả

    # Lọc theo ShipMonth (chỉ lọc theo tháng và năm)
    if filter_shipMonth:
        try:
            # Tách tháng và năm từ định dạng ngày/tháng/năm
            ship_month, ship_year = map(int, filter_shipMonth.split('/'))
            # Lọc theo tháng và năm sau khi chuyển đổi ShipDate thành kiểu Date
            and_conditions.append({
                "$and": [
                    {"$expr": {"$eq": [{"$month": {"$dateFromString": {"dateString": "$ShipDate", "format": "%d/%m/%Y"}}}, ship_month]}},
                    {"$expr": {"$eq": [{"$year": {"$dateFromString": {"dateString": "$ShipDate", "format": "%d/%m/%Y"}}}, ship_year]}}
                ]
            })
        except ValueError:
            pass  # Nếu định dạng không hợp lệ, không làm gì cả

    # Gộp các điều kiện
    if and_conditions:
        query["$and"] = and_conditions

    # Truy vấn dữ liệu
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit

    total_records = collection.count_documents(query)
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find(query).skip(skip).limit(limit))

    return render_template("order.html", records=data, page=page, total_pages=total_pages, 
                            totalOrder=countOrder(collection), 
                            totalPurchases=countOrderPurchases(collection), 
                            order=orderMax(collection),
                            MonthYearOrder=monthYearOrder,
                            MonthYearShip=monthYearShip)
                           


def home_Product():
    
    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    
    filter_category = request.args.get('Category', '')
    filter_sub = request.args.get('Sub-Category', '')
    if filter_category == "OfficeSupplies": # đổi tên category cho phù hợp với tên trong database
        filter_category = "Office Supplies"

    query = {}
    if filter_category:
        category = filter_category.split(',')  
        query["Category"] = {"$in": category}  
    if filter_sub:
        query["SubCategory"] = {"$regex": filter_sub, "$options": "i"}
        
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    total_records = collection.count_documents(query)
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find(query).skip(skip).limit(limit))  
    
    return render_template("product.html", records=data, page=page, total_pages=total_pages, 
                                           totalProduct=countProduct(collection), 
                                           totalPurchases=countProductPurchases(collection), 
                                           product=productMax(collection))