from flask import render_template, request, current_app, url_for
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
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    data = {
        "name": request.form.get("name"), 
        "idcustomer": request.form.get("idcustomer"),
        "segment": request.form.get("segment"),
        "city": request.form.get("city"),
        "state": request.form.get("state"),
        "quantity": request.form.get("quantity"),
        "region" : request.form.get("region")
    }
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    return data