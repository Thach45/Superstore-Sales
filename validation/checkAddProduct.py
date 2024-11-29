from flask import current_app
def checkAddProduct(data):
    mongo = current_app.config['MONGO']
    data['Revenue'] = float(data['Revenue'])
    data['Quantity'] = int(data['Quantity'])
    if data['Category'] == "OfficeSupplies":
        data['Category'] = "Office Supplies"
    existing_product = mongo.db.products.find_one({"ProductName": data['ProductName']})
    existing_category = mongo.db.products.find_one({"Category": data['Category']})
    existing_subcategory = mongo.db.products.find_one({"SubCategory": data['SubCategory']})
    if existing_product and existing_category and existing_subcategory:
        data['Revenue'] += existing_product['Revenue']
        data['Quantity'] += existing_product['Quantity']
    return data 