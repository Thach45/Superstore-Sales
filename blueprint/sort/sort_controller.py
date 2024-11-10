from flask import request, jsonify, render_template, current_app
from flask_pymongo import PyMongo as mongo

def Sort():
    mongo = current_app.config['MONGO']
    #sort_field = request.args.get('field', 'Quantity') 
    sort_quantity = request.args.get('order') 

    if sort_quantity not in ['asc', 'desc']:
        return jsonify({"error": "Invalid sort order. Use 'asc' or 'desc'."}), 400
    
    mongo_quantity = 1 if sort_quantity == 'asc' else -1

    collection = mongo.db.users

    sorted_quantity = collection.find().sort("Quantity", mongo_quantity)

    return render_template("customer.html",records=sorted_quantity)
    
    
