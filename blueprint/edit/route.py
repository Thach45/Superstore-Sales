from . import edit_bp
from .edit_controller import index, edit_P, editHome

@edit_bp.route('/edit/<string:id>', methods=['GET']) #lấy giao diện
def home_route(id):
    return index(id)

@edit_bp.route('/edit/<string:ids>', methods=['POST']) #xử lý dữ liệu
def edit(ids):
    return edit_P(ids)

@edit_bp.route('/edit/product/<string:id>', methods=['GET']) #lấy giao diện
def edit_home(id):
    return editHome(id)