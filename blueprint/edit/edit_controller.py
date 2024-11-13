from flask import render_template, request, current_app, url_for, redirect
import pandas as pd
from bson.objectid import ObjectId

def index(id):
    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    data = (collection.find_one({'_id': ObjectId(id)}))
    return render_template('edit.html', customer=data)

def edit_P(ids):

    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    data = {
        "Name": request.form.get("name"), 
        "IDCustomer": request.form.get("idcustomer"),
        "Segment": request.form.get("segment"),
        "City": request.form.get("city"),
        "State": request.form.get("state"),
        "Quantity": int(request.form.get("quantity")),
        "Region" : request.form.get("region")
    }
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    return redirect(url_for('customer.home_route'))