import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



if __name__=='__main__':

    # Lấy đường dẫn tuyệt đối đến file hiện tại
    current_file_path = os.path.realpath(__file__)

    # Lần ngược lên các cấp thư mục đến thư mục gốc (ở đây giả sử thư mục gốc có tên là 'project')
    while not os.path.basename(current_file_path) == 'Superstore-Sales':
        current_file_path = os.path.dirname(current_file_path)
    superstore_path = current_file_path
    file_path = os.path.join(superstore_path,'static','file','datacleaned.csv')
    data = pd.read_csv(file_path,sep = ',', header=0, index_col='Row ID')

    revenue_by_category = data.groupby(['Category'])['Sales'].sum().sort_values()
    revenue_by_category.name = ""
    colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
    revenue_by_category.plot(kind='pie',colors=colors, autopct='%1.2f%%', startangle=90,radius = 0.9)
    plt.title("Revenue structure by Category")

    image_path = os.path.join(superstore_path, 'static', 'images', 'revenue_structure_by_category.png')
    plt.savefig(image_path)

