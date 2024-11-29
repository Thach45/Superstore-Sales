from flask import render_template, request, current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
from helper.DateOrder import MonthYearOrder, MonthYearShip
from helper.Customer import CustomerState, CustomerCity
from datetime import datetime

def home_Customer():
    ''' Lấy danh sách khách hàng từ cơ sở dữ liệu MongoDB và hiển thị trang thông tin khách hàng.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, thực hiện truy vấn theo các bộ lọc (City, Segment, Region, State) 
    mà người dùng cung cấp qua URL query parameters. Sau đó, hiển thị danh sách thông tin khách hàng theo bộ lọc tương ứng. '''
    
    # Lấy các bộ lọc từ URL query parameters
    filter_city = request.args.get('City', '')
    filter_segment = request.args.get('Segment', '')
    filter_region = request.args.get('Region', '')
    filter_state = request.args.get('State', '')

    # Kếi nối với cơ sở dữ liệu MongoDB và lấy ra collection 'users'
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  
    states = CustomerState(collection)
    cities = CustomerCity(collection)
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    query = {}

    # Lọc theo City
    if filter_city:
        city = filter_city.split(',')  
        query["City"] = {"$in": city}  
        
    # Lọc theo Segment, tìm kiếm với regex (không phân biệt chữ hoa/thường)
    if filter_segment:
        query["Segment"] = {"$regex": filter_segment, "$options": "i"}

    # Lọc theo Region
    if filter_region:
        query["Region"] = {"$regex": filter_region, "$options": "i"}
        
    # Lọc theo State
    if filter_state:
        query["State"] = {"$regex": filter_state, "$options": "i"}
        
    #Phân trang
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 

    
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
    
    ''' Lấy danh sách đơn hàng từ cơ sở dữ liệu MongoDB và hiển thị trang thông tin đơn hàng.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, thực hiện truy vấn theo các bộ lọc (OrderMonth, ShipMonth) 
    mà người dùng cung cấp qua URL query parameters. Sau đó, hiển thị danh sách thông tin đơn hàng theo bộ lọc tương ứng. '''
    
    # Lấy các bộ lọc từ URL query parameters
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
            order_month, order_year = map(int, filter_orderMonth.split('/'))
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
            ship_month, ship_year = map(int, filter_shipMonth.split('/'))
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
        
    #Phân trang
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
    ''' Lấy danh sách sản phẩm từ cơ sở dữ liệu MongoDB và hiển thị trang thông tin sản phẩm.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, thực hiện truy vấn theo các bộ lọc (Category, Sub-Category) 
    mà người dùng cung cấp qua URL query parameters. Sau đó, hiển thị danh sách thông tin sản phẩm theo bộ lọc tương ứng. '''
    
    #Kếi nối với cơ sở dữ liệu MongoDB và lấy ra collection 'products'
    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    
    # Lấy các bộ lọc từ URL query parameters
    filter_category = request.args.get('Category', '')
    filter_sub = request.args.get('Sub-Category', '')
    if filter_category == "OfficeSupplies": # đổi tên category cho phù hợp với tên trong database
        filter_category = "Office Supplies"

    query = {}
    
    #Lọc theo Category 
    if filter_category:
        category = filter_category.split(',')  
        query["Category"] = {"$in": category}  
        
    #Lọc theo Sub-Category
    if filter_sub:
        query["SubCategory"] = {"$regex": filter_sub, "$options": "i"}
        
    #Phân trang    
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    total_records = collection.count_documents(query)
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find(query).skip(skip).limit(limit))  
    
    return render_template("product.html", records=data, page=page, 
                                           total_pages=total_pages, totalProduct=countProduct(collection), 
                                           totalPurchases=countProductPurchases(collection), product=productMax(collection))