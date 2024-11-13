from . import filter_bp
from .filter_controller import home
@filter_bp.route('/customer/filter',methods=["GET"])
def searchHome():
    return home()