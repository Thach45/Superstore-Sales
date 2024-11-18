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

    revenue_per_city = data.groupby(['City'])['Sales'].sum().sort_values(ascending=False)
    top10_highest_revenue_cities = revenue_per_city[:11]
    top10_highest_revenue_cities.plot(kind='bar',color = '#12c7d2')
    plt.title("Top 10 highest revenue cities")
    plt.subplots_adjust(left=0.15, bottom=0.25, right=0.9, top=0.9)
    plt.xlabel("")
    plt.ylabel("revenue ($)")
    fig = plt.gcf()  # Lấy đối tượng Figure hiện tại
    fig.set_size_inches(8, 5)  # Chiều rộng 12 inch, chiều cao 8 inch
    image_path = os.path.join(superstore_path, 'static', 'images', 'top10_highest_revenue_cities.png')
    plt.savefig(image_path)
    plt.show()