
from flask import current_app, jsonify
def checkAddCustomer(data):
    mongo = current_app.config['MONGO']
    existing_customer = mongo.db.users.find_one({"IDCustomer": data['IDCustomer']})
    if existing_customer:
        return "CustomerID already exists"
    data["Quantity"] = int(data["Quantity"])
    return data