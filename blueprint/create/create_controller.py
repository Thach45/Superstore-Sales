from flask import render_template, request, current_app, url_for, redirect, flash
from flask import jsonify
import pandas  as pd
from datetime import datetime
from validation.checkAddOrder import checkAddOrder
from validation.checkAddProduct import checkAddProduct
from validation.checkAddCustomer import checkAddCustomer
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
        if request.form['collection'] == 'products':
            mongo.db.products.insert_many(data)
            return redirect(url_for('product.home_route'))
        elif request.form['collection'] == 'customers':
            mongo.db.users.insert_many(data)
            return redirect(url_for('customer.home_route'))
        elif request.form['collection'] == 'orders':
            mongo.db.orders.insert_many(data)
            return redirect(url_for('order.home_route'))
        else:
            mongo.db.datastore.insert_many(data)
            return redirect(url_for('home.home_route'))
    else:
     return render_template('create.html', message="0")
    



def add_product():
    try:
        mongo = current_app.config['MONGO']
        data = dict(request.form)
        data = checkAddProduct(data)
        mongo.db.products.update_one(
            {'ProductName': data['ProductName'], 'Category': data['Category'], 'SubCategory': data['SubCategory']},  
            {'$set': data},  # Cập nhật với dữ liệu mới
            upsert=True  # Chèn nếu không tồn tại
        )
        flash('Sản phẩm đã được thêm thành công!', 'success')

        return redirect(url_for('product.home_route'))
    except :
        return render_template('404.html')
    

def add_customer():
    try:
        mongo = current_app.config['MONGO']
        data = dict(request.form)
        data = checkAddCustomer(data)
        if data == "CustomerID already exists":
            return render_template('404.html', message="CustomerID already exists")
        mongo.db.users.insert_one(data)
        flash('Khách hàng đã được thêm thành công!', 'success')
        return redirect(url_for('customer.home_route'))
    except :
        return render_template('404.html')
    


def add_order():
    try:
        data = dict(request.form)
        data = checkAddOrder(data) # Đã Validate
        if data == "OrderID already exists":
            return render_template('404.html', message="OrderID already exists")
        if data == "CustomerID already exists":
            return render_template('404.html', message="CustomerID already exists")
        mongo = current_app.config['MONGO']
        mongo.db.orders.insert_one(data)
        flash('Đơn hàng đã được thêm thành công!', 'success')
        return redirect(url_for('order.home_route'))
    except Exception as e:
        print(f"Error: {str(e)}")  # Thêm log để debug
        return render_template('404.html')
    