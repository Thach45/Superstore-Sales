from flask import Flask
from blueprint.home import home_bp
from blueprint.search import search_bp
from blueprint.create import create_bp
from blueprint.customer import customer_bp
from blueprint.sort import sort_bp
from blueprint.filter import filter_bp
from blueprint.edit import edit_bp
from blueprint.delete import delete_bp
from blueprint.product import product_bp
from blueprint.order import order_bp
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("URL_MONGO")
mongo = PyMongo(app)
app.config['MONGO'] = mongo
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.register_blueprint(product_bp)
app.register_blueprint(home_bp)
app.register_blueprint(search_bp)
app.register_blueprint(create_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(sort_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(order_bp)
app.register_blueprint(filter_bp)
if __name__ == '__main__':
    app.run(debug=True, port=8000)