from . import order_bp
from .order_controller import index

@order_bp.route('/order')
def home_route():
    return index()