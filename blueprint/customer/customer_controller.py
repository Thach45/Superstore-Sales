from flask import render_template, request, current_app, url_for
from flask import jsonify
import pandas as pd
def index():
    return render_template('customer.html')