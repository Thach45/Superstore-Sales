from . import edit_bp
from .edit_controller import index, edit_P

@edit_bp.route('/edit/<string:id>', methods=['GET']) #lấy giao diện
def home_route(id):
    return index(id)

@edit_bp.route('/edit/<string:ids>', methods=['POST']) #xử lý dữ liệu
def edit(ids):
    return edit_P(ids)