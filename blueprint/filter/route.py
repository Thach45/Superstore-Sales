from . import filter_bp
from .filter_controller import homeCustomer_Filter
from .filter_controller import homeProduct_Filter
@filter_bp.route('/customer/filter',methods=["GET"])
def filterCustomer():
    return homeCustomer_Filter()

@filter_bp.route('/product/filter',methods=["GET"])
def filterProduct():
    return homeProduct_Filter()