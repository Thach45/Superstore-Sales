from . import product_bp
from .product_controller import index, download

@product_bp.route('/product')
def home_route():
    return index()
@product_bp.route('/product/download')
def download_route():
    return download()