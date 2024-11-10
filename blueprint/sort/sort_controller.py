from flask import request, jsonify, render_template, current_app
from flask_pymongo import PyMongo as mongo

def Sort():
    mongo = current_app.config['MONGO']
    #sort_field = request.args.get('field', 'Quantity') 
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

    return render_template("customer.html",records=sorted_quantity, page=page, total_pages=total_pages)
    
    
