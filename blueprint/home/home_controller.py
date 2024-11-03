from flask import render_template, current_app, url_for
from flask import jsonify
import os
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
def home():
    # Dữ liệu mẫu
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1700]

    # Tạo biểu đồ
    plt.figure(figsize=(10, 5))
    plt.fill_between(month, sales, color="skyblue", alpha=0.4)
    plt.plot(month, sales, color="Slateblue", alpha=0.6)
    image_path = os.path.join(current_app.root_path, 'static', 'images', 'sales.png')
    plt.savefig(image_path)
    plt.close()
    image_url = url_for('static', filename='images/sales.png')
    return render_template('dashboard.html', image_url=image_url)