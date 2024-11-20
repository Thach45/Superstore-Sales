from flask import Flask, render_template, request , current_app
from helper.infoTopCustomer import countUser, countUserPurchases, userMax
from helper.infoTopProduct import countProduct, countProductPurchases,productMax
from helper.infoTopOrder import countOrder,countOrderPurchases,orderMax
def staticsCustomer():
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Truy cập collection 'users' trong MongoDB
    return render_template("customer.html",totalUser=countUser(collection), totalPurchases=countUserPurchases(collection), user=userMax(collection))
# def staticProduct():
#     mongo = current_app.config['MONGO']
#     collection = mongo.db.products
#     return render_template("product.html",totalProduct=countProduct(collection), totalPurchases=countProductPurchases(collection), product=productMax(collection))
def staticOrder():
    mongo = current_app.config['MONGO']
    collection = mongo.db.orders
    return render_template("order.html",totalOrder=countOrder(collection), totalPurchases=countOrderPurchases(collection), order=orderMax(collection))