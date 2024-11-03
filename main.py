from flask import Flask
from blueprint.home import home_bp
from blueprint.search import search_bp
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nguyenhoangthach:Thach18012005@cluster0.hgcnpf3.mongodb.net/Superstore-Sales"
mongo = PyMongo(app)
app.config['MONGO'] = mongo


app.register_blueprint(home_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)