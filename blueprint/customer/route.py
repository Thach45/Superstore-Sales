from . import customer_bp
from .customer_controller import index, download

@customer_bp.route('/customer')
def home_route():
    return index()
@customer_bp.route('/customer/download')
def download_route():
    return download()