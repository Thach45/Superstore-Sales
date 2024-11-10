from flask import Flask
from blueprint.home import home_bp
from blueprint.search import search_bp
from blueprint.create import create_bp
from blueprint.customer import customer_bp
from blueprint.sort import sort_bp
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nguyenhoangthach:Thach18012005@cluster0.hgcnpf3.mongodb.net/Superstore-Sales"
mongo = PyMongo(app)
app.config['MONGO'] = mongo


app.register_blueprint(home_bp)
app.register_blueprint(search_bp)
app.register_blueprint(create_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(sort_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8000)