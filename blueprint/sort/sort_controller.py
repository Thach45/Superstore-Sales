from flask import request, jsonify, render_template, current_app
from flask_pymongo import PyMongo as mongo
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
def SortCustomer():
    mongo = current_app.config['MONGO']
    sort_quantity = request.args.get('sort') 

    if sort_quantity not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_quantity = 1 if sort_quantity == 'asc' else -1
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.users
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    sorted_quantity = collection.find().sort("Quantity", mongo_quantity).skip(skip).limit(limit)

    return render_template("customer.html",records=sorted_quantity, page=page, total_pages=total_pages, totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))

    
def SortProduct():
    mongo = current_app.config['MONGO']
    sort_field = request.args.get('field', 'Quantity') #tham số mặc định truyền vào là Quantity
    sort_product = request.args.get('sort') 

    if sort_product not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_product = 1 if sort_product == 'asc' else -1
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.products
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)

    Sorted_product = collection.find().sort(sort_field, mongo_product).skip(skip).limit(limit)

    return render_template("product.html",records=Sorted_product, page=page, total_pages=total_pages,
                           totalProduct=countProduct(collection), 
                           totalPurchases=countProductPurchases(collection), 
                           product=productMax(collection))

def SortOrder():
    mongo = current_app.config['MONGO']
    sort_field = request.args.get('field', 'Frequency') #tham số mặc định truyền vào là Costs
    sort_order = request.args.get('sort') 

    if sort_order not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_order = 1 if sort_order == 'asc' else -1
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.orders
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)

    Sorted_order = collection.find().sort(sort_field, mongo_order).skip(skip).limit(limit)

    return render_template("order.html",records=Sorted_order, page=page, total_pages=total_pages,
                           totalOrder=countOrder(collection), totalPurchases=countOrderPurchases(collection), 
                           order=orderMax(collection))
