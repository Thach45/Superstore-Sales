from flask import render_template, request, current_app, url_for, redirect, flash
import pandas as pd
from bson.objectid import ObjectId
from helper.Customer import CustomerState, CustomerCity
def index_Customer(id):
    '''Lấy thông tin sản khách hàng từ cơ sở dữ liệu MongoDB và hiển thị trang chỉnh sửa khách hàng.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, tìm kiếm khách hàng trong collection 'users' 
    theo '_id' của khách hàng (dựa trên giá trị 'id' được truyền vào).
    Nếu tìm thấy khách hàng, thông tin khách hàng sẽ được truyền tới template 'editCustomer.html'.'''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để lấy dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    states = CustomerState(collection)
    cities = CustomerCity(collection)
    data = (collection.find_one({'_id': ObjectId(id)}))
    return render_template('editCustomer.html', customer=data, states=states, cities=cities)

def edit_Customer(ids):
    ''' Cập nhật thông tin khách hàng trong cơ sở dữ liệu MongoDB.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, nhận thông tin khách hàng từ template 'editCustomer.html',
    và sử dụng phương thức 'update_one' để cập nhật thông tin khách hàng trong collection 'users' 
    theo '_id' của khách hàng (dựa trên giá trị 'ids' được truyền vào). 
    Sau khi cập nhật thành công, người dùng sẽ được chuyển hướng đến trang danh sách khách hàng. '''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để cập nhật dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.users
    
    #Lấy dữ liệu từ template 'editCustomer.html'
    data = {
        "Name": request.form.get("name"), 
        "IDCustomer": request.form.get("idcustomer"),
        "Segment": request.form.get("segment"),
        "City": request.form.get("city"),
        "State": request.form.get("state"),
        "Quantity": int(request.form.get("quantity")),
        "Region" : request.form.get("region")
    }
    
    # Cập nhật collection trên MongoDB dựa trên _id
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    flash('Khách hàng đã được cập nhật thành công!', 'success')

    return redirect(url_for('customer.home_route'))

def index_Product(id):
    '''Lấy thông tin sản sản phẩm từ cơ sở dữ liệu MongoDB và hiển thị trang chỉnh sửa sản phẩm.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, tìm kiếm sản phẩm trong collection 'products' 
    theo '_id' của sản phẩm (dựa trên giá trị 'id' được truyền vào).
    Nếu tìm thấy sản phẩm, thông tin sản phẩm sẽ được truyền tới template 'editProduct.html'.'''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để lấy dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    data = (collection.find_one({'_id': ObjectId(id)})) # Tìm sản phẩm theo _id
    return render_template('editProduct.html', product=data)

def edit_Product(ids):
    ''' Cập nhật thông tin sản phẩm trong cơ sở dữ liệu MongoDB.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, nhận thông tin sản phẩm từ template 'editProduct.html',
    và sử dụng phương thức 'update_one' để cập nhật thông tin sản phẩm trong collection 'products' 
    theo '_id' của sản phẩm (dựa trên giá trị 'ids' được truyền vào). 
    Sau khi cập nhật thành công, người dùng sẽ được chuyển hướng đến trang danh sách sản phẩm. '''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để cập nhật dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.products
    
    #Lấy dữ liệu từ template 'editProdut.html'
    data = {
        "ProductName": request.form.get("ProductName"), 
        "Category": request.form.get("Category"),
        "SubCategory": request.form.get("SubCategory"),
        "Revenue": float(request.form.get("Revenue")),
        "Quantity": int(request.form.get("Quantity"))
    }
    if data['Category'] == "OfficeSupplies":
        data['Category'] = "Office Supplies"
    # Cập nhật collection trên MongoDB dựa trên _id
    collection.update_one(
        {'_id': ObjectId(ids)},
        {'$set': data}  
    )

    flash('Sản phẩm đã được cập nhật thành công!', 'success')

    return redirect(url_for('product.home_route'))

def index_Order(id):
    '''Lấy thông tin sản đơn hàng từ cơ sở dữ liệu MongoDB và hiển thị trang chỉnh sửa đơn hàng.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, tìm kiếm đơn hàng trong collection `orders` 
    theo `_id` của đơn hàng (dựa trên giá trị `id` được truyền vào).
    Nếu tìm thấy đơn hàng, thông tin đơn hàng sẽ được truyền tới template `editOrder.html`.'''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để lấy dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    data = (collection.find_one({'_id': ObjectId(id)})) # Tìm đơn hàng theo _id
    return render_template('editOrder.html', order=data)

def edit_Order(ids):
    ''' Cập nhật thông tin đơn hàng trong cơ sở dữ liệu MongoDB.

    Hàm này kết nối đến cơ sở dữ liệu MongoDB, nhận thông tin đơn hàng từ template 'editOrder.html',
    và sử dụng phương thức 'update_one' để cập nhật thông tin đơn hàng trong collection 'orders' 
    theo '_id' của đơn hàng (dựa trên giá trị 'ids' được truyền vào). 
    Sau khi cập nhật thành công, người dùng sẽ được chuyển hướng đến trang danh sách đơn hàng. '''
    
    #Kếi nối với cơ sở dữ liệu MongoDB để cập nhật dữ liệu
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    
    #Lấy dữ liệu từ template 'editOrder.html'
    data = {
        "OrderID" : request.form.get("OrderID"),
        "OrderDate" : request.form.get("OrderDate"),
        "ShipDate" : request.form.get("ShipDate"),
        "CustomerName" : request.form.get("CustomerName"),
        "CustomerID" : request.form.get("CustomerID"),
        "TotalCost" : float(request.form.get("TotalCost")),
        "Frequency" : int(request.form.get("Frequency"))
    }
    
    # Cập nhật collection trên MongoDB dựa trên _id
    collection.update_one(
    {'_id': ObjectId(ids)},
    {'$set': data}  
    )
    flash('Đơn hàng đã được cập nhật thành công!', 'success')

    return redirect(url_for('order.home_route'))