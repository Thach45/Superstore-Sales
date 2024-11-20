from flask import render_template, request, current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from datetime import datetime

def home():

    filter_city = request.args.get('City', '')
    filter_segment = request.args.get('Segment', '')
    filter_region = request.args.get('Region', '')
    filter_state = request.args.get('State', '')

    
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  
    
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
    
    return render_template("customer.html", records=data, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))

def filter_orders():
    filter_orderMonth = request.args.get('OrderMonth', '')
    filter_shipMonth = request.args.get('ShipMonth', '')

    mongo = current_app.config['MONGO']
    collection = mongo.db.orders

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

    return render_template("order.html", records=data, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))
