from . import product_bp
from .product_controller import index

@product_bp.route('/product')
def home_route():
    return index()