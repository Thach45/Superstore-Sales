from flask import render_template, request, current_app
from pymongo import MongoClient
from helper.infoTopCustomer import countUser, countUserPurchases, userMax

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
