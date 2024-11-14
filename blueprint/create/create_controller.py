from flask import render_template, request, current_app, url_for
from flask import jsonify
import pandas  as pd
def create():
    return render_template('create.html')
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.csv'):
        # Đọc file CSV
        df = pd.read_csv(file)
        # Chuyển DataFrame thành danh sách dictionary
        data = df.to_dict(orient='records')
        # Lấy đối tượng MongoDB từ config của Flask
        mongo = current_app.config['MONGO']
        # Thêm dữ liệu vào MongoDB
        mongo.db.datastore.insert_many(data)
        return render_template('dashboard.html', message="1")
    else:
        return render_template('create.html', message="0")