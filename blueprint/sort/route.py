from . import sort_bp
from .sort_controller import SortCustomer, SortProduct

@sort_bp.route('/customer/sort', methods=['GET'])
def sort_Customer():
    return SortCustomer()

@sort_bp.route('/product/sort', methods=['GET'])
def sort_product():
    return SortProduct()

