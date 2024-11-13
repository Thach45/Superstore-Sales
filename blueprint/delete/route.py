from . import delete_bp
from .delete_controller import index


@delete_bp.route('/customer/delete/<string:id>', methods=['POST'])
def home_route(id):
    return index(id)