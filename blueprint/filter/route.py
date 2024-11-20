from . import filter_bp
from .filter_controller import home_Customer, home_Product, filter_orders
@filter_bp.route('/order/filter',methods=["GET"])
def filterOrder():
    return filter_orders()
from .filter_controller import home_Customer, home_Product
@filter_bp.route('/customer/filter',methods=["GET"])
def filterC():
    return home_Customer()

@filter_bp.route('/product/filter',methods=["GET"])
def filterP():
    return home_Product()
