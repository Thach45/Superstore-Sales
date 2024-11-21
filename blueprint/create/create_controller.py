from flask import render_template, request, current_app, url_for, redirect
from flask import jsonify
import pandas  as pd
from datetime import datetime

def create():
    return render_template('create.html')
def upload():

    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.csv'):
        # Đọc file CSV
        df = pd.read_csv(file)
        # Chuyển DataFrame thành danh sách dictionary
        data = df.to_dict(orient='records')
        # Lấy đối tượng MongoDB từ config của Flask
        mongo = current_app.config['MONGO']
        # Thêm dữ liệu vào MongoDB
        mongo.db.datastore.insert_many(data)
        return redirect(url_for('home.home_route'))
    else:
        return render_template('create.html', message="0")
def add_product():
    try:
        mongo = current_app.config['MONGO']
        mongo.db.products.insert_one(dict(request.form))
        return redirect(url_for('product.home_route'))
    except :
        return render_template('404.html')
def add_customer():
    try:
        print(request.form)
        mongo = current_app.config['MONGO']
        mongo.db.users.insert_one(dict(request.form))
        return redirect(url_for('customer.home_route'))
    except :
        return render_template('404.html')
def add_order():
    try:
        data = dict(request.form)
        
        # Chuyển đổi định dạng ngày tháng và đảm bảo tất cả giá trị là string
        if 'OrderDate' in data:
            date_obj = datetime.strptime(data['OrderDate'], '%Y-%m-%d')
            data['OrderDate'] = str(date_obj.strftime('%d/%m/%Y'))
        if 'ShipDate' in data:
            date_obj = datetime.strptime(data['ShipDate'], '%Y-%m-%d')
            data['ShipDate'] = str(date_obj.strftime('%d/%m/%Y'))
            
        # Chuyển tất cả giá trị trong data thành string
        data = {key: str(value) for key, value in data.items()}
            
        mongo = current_app.config['MONGO']
        mongo.db.orders.insert_one(data)
        return redirect(url_for('order.home_route'))
    except Exception as e:
        print(f"Error: {str(e)}")  # Thêm log để debug
        return render_template('404.html')
    