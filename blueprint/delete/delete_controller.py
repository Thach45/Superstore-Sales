from flask import render_template, request, current_app
import pandas as pd

def index(id):
    #Không được xoá đoạn duới này, đoạn dưới là code để chia thành các trang
    mongo = current_app.config['MONGO']
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    collection = mongo.db.users  
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    data = list(collection.find().skip(skip).limit(limit))  
    #No delete code-------
    ID = id #Lấy IDUser sẵn rồi nha---

    return render_template('customer.html', records=data, page=page, total_pages=total_pages)