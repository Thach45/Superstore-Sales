from . import sort_bp
from .sort_controller import Sort

@sort_bp.route('/customer/sort', methods=['GET'])
def sort_route():
    return Sort()


