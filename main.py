from flask import Flask
from blueprint.home import home_bp
from blueprint.search import search_bp
app = Flask(__name__)


app.register_blueprint(home_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)