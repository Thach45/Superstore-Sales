from . import order_bp
from .order_controller import index, download

@order_bp.route('/order')
def home_route():
    return index()
@order_bp.route('/order/download')
def download_route():
    return download()