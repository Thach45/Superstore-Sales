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

    top6_subcategory_highest_revenue = data.groupby(['Sub-Category'])['Sales'].sum().sort_values(ascending=False)[:7]
    #revenue_by_category.name = ""
    #print(revenue_by_category)
    colors = ['#99C1A9','#CE5C5B','#EBCB78','#73B6E1','#A693C1','#A1D1E7']
    top6_subcategory_highest_revenue.plot(kind='bar',color = '#A693C1')
    plt.title("Top 6 Sub-Category Highest Revenue",fontsize = 18, fontweight = 'bold')
    plt.xticks(rotation=0)
    plt.ylabel('Revenue ($)')
    plt.xlabel('Sub-Category')
    plt.grid(linestyle='--',alpha = 0.7)
    plt.subplots_adjust(left= 0.15)
    fig = plt.gcf()
    fig.set_size_inches(8,8)
    image_path = os.path.join(superstore_path, 'static', 'images', 'top6_subcategory_highest_revenue.png')
    plt.savefig(image_path,dpi = 300)
    plt.show()

