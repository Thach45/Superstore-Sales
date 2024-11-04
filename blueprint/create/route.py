
from . import create_bp
from .create_controller import create
from .create_controller import upload
@create_bp.route('/create')
def home_route():
    return create()
@create_bp.route('/create/upload', methods=['POST'])
def upload_route():
    return upload()
