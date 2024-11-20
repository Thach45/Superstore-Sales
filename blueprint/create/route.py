
from . import create_bp
from .create_controller import create
from .create_controller import upload
from .create_controller import add_product, add_customer, add_order
@create_bp.route('/create')
def home_route():
    return create()
@create_bp.route('/create/upload', methods=['POST'])
def upload_route():
    return upload()

@create_bp.route('/add/product', methods=['POST'])
def add_product_route():
    return add_product()

@create_bp.route('/add/customer', methods=['POST'])
def add_customer_route():
    return add_customer()

@create_bp.route('/add/order', methods=['POST'])
def add_order_route():
    return add_order()