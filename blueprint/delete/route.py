from . import delete_bp
from .delete_controller import delCustomer, delProduct, delOrder

@delete_bp.route('/customer/delete/<string:id>', methods=['POST'])
def viewCustomer(id):
    return delCustomer(id)

@delete_bp.route('/product/delete/<string:id>', methods=['POST'])
def viewProduct(id):
    return delProduct(id)

@delete_bp.route('/order/delete/<string:id>', methods=['POST'])
def viewOrder(id):
    return delOrder(id)

