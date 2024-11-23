from . import edit_bp
from .edit_controller import index_Customer, edit_Customer, index_Product, edit_Product, index_Order, edit_Order

@edit_bp.route('/edit/customer/<string:id>', methods=['GET']) #lấy giao diện
def customer_home_route(id):
    return index_Customer(id)

@edit_bp.route('/edit/customer/<string:ids>', methods=['POST']) #xử lý dữ liệu
def edit_C(ids):
    return edit_Customer(ids)

@edit_bp.route('/edit/product/<string:id>', methods=['GET']) #lấy giao diện
def product_home_route(id):
    return index_Product(id)

@edit_bp.route('/edit/product/<string:ids>', methods=['POST']) #xử lý dữ liệu
def edit_P(ids):
    return edit_Product(ids)

@edit_bp.route('/edit/order/<string:id>', methods=['GET']) #lấy giao diện
def order_home_route(id):
    return index_Order(id)

@edit_bp.route('/edit/order/<string:ids>', methods=['POST']) #xử lý dữ liệu
def edit_O(ids):
    return edit_Order(ids)