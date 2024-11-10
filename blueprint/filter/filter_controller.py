from flask import render_template, request, current_app
from pymongo import MongoClient

def home():

    filter_country = request.args.get('Country', '')
    filter_segment = request.args.get('Segment', '')
    
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  

    query = {}

    if filter_country:
        countries = filter_country.split(',')  
        query["Country"] = {"$in": countries}  

    if filter_segment:
        query["Segment"] = {"$regex": filter_segment, "$options": "i"}

    data = list(collection.find(query))  
    
    return render_template("customer.html", records=data)
