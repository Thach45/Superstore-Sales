from . import search_bp
from .search_controller import SearchCustomer,SearchProduct,SearchOrder

@search_bp.route('/customer/search', methods=['GET'])
def Search_Customer():
    return SearchCustomer()

@search_bp.route('/product/search', methods=['GET'])
def Search_Product():
    return SearchProduct()

@search_bp.route('/order/search', methods=['GET'])
def Search_Order():
    return SearchOrder()


