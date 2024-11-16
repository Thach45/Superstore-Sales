from flask import render_template, request, current_app, url_for, redirect
import pandas as pd
from bson.objectid import ObjectId

def index_Customer(id):
    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    data = (collection.find_one({'_id': ObjectId(id)}))
    return render_template('editCustomer.html', customer=data)

def edit_Customer(ids):

    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    data = {
        "name": request.form.get("name"), 
        "idcustomer": request.form.get("idcustomer"),
        "segment": request.form.get("segment"),
        "city": request.form.get("city"),
        "state": request.form.get("state"),
        "quantity": int(request.form.get("quantity")),
        "region" : request.form.get("region")
    }
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    return redirect(url_for('customer.home_route'))

def index_Product(id):
    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    data = (collection.find_one({'_id': ObjectId(id)}))
    return render_template('editProduct.html', product=data)

def edit_Product(ids):

    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    data = {
        "ProductName": request.form.get("ProductName"), 
        "Category": request.form.get("Category"),
        "SubCategory": request.form.get("SubCategory"),
        "Revenue": int(request.form.get("Revenue")),
        "Quantity": int(request.form.get("Quantity"))
    }
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    return redirect(url_for('product.home_route'))