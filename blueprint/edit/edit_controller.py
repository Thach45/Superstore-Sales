from flask import render_template, request, current_app
import pandas as pd
from bson.objectid import ObjectId

def index(id):
    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    data = (collection.find_one({'_id': ObjectId(id)}))
    return render_template('edit.html', customer=data)

def edit_P(ids):

    #Viết code ở đây 
    data = request.form # đã lấy dữ liệu của request chạy thử để xem dữ liệu đã truyền qua chưa
    return data