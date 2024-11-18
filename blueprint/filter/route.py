from . import filter_bp
from .filter_controller import home, filter_orders
@filter_bp.route('/customer/filter',methods=["GET"])
def searchHome():
    return home()

@filter_bp.route('/order/filter',methods=["GET"])
def filterOrder():
    return filter_orders()