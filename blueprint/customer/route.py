from . import customer_bp
from .customer_controller import index

@customer_bp.route('/customer')
def home_route():
    return index()