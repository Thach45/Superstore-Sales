from . import search_bp
from .search_controller import home
@search_bp.route('/customer/search', methods=['GET'])
def searchHome():
    return home()