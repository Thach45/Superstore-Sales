from datetime import datetime
from flask import current_app, jsonify
def checkAddOrder(data):
    mongo = current_app.config['MONGO']
    existing_orders = mongo.db.orders.find_one({"OrderID": data['OrderID']})
    existing_customer = mongo.db.orders.find_one({"CustomerID": data['CustomerID']})
    print(existing_orders)
    if existing_orders:
        return "OrderID already exists"
    if existing_customer:
        return "CustomerID already exists"
    if 'OrderDate' in data:
        date_obj = datetime.strptime(data['OrderDate'], '%Y-%m-%d')
        data['OrderDate'] = str(date_obj.strftime('%d/%m/%Y'))
    if 'ShipDate' in data:
        date_obj = datetime.strptime(data['ShipDate'], '%Y-%m-%d')
        data['ShipDate'] = str(date_obj.strftime('%d/%m/%Y'))
    data['TotalCost'] = float(data['TotalCost'])
    data['Frequency'] = int(data['Frequency'])
    return data