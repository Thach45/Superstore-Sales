from flask import redirect, url_for
from . import home_bp
from .home_controller import home

@home_bp.route('/home')
def home_route():
    return home()
@home_bp.route('/')
def default_route():
    return redirect(url_for('home.home_route'))