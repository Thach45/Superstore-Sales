from flask import render_template, current_app
from flask import jsonify
from model.home import user_schema
def home():
    mongo = current_app.config['MONGO']
    users = mongo.db.user.find({})
    result = []
    for user in users:
        user['_id'] = str(user['_id'])  # Chuyển ObjectId sang chuỗi
        result.append(user)
    return render_template('dashboard.html', users=result)