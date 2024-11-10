from flask import render_template, request, current_app
from pymongo import MongoClient

def home():

    filter_country = request.args.get('Country', '')
    filter_segment = request.args.get('Segment', '')
    
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  
    
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    query = {}

    if filter_country:
        countries = filter_country.split(',')  
        query["Country"] = {"$in": countries}  

    if filter_segment:
        query["Segment"] = {"$regex": filter_segment, "$options": "i"}
    total_records = collection.count_documents(query)
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find(query).skip(skip).limit(limit))  
    
    return render_template("customer.html", records=data, page=page, total_pages=total_pages)
