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
    data = pd.read_csv(file_path,sep=',',index_col='Row ID',header=0)

    annual_revenue = data.groupby(['Year'])['Sales'].sum().sort_index()

    annual_revenue.plot(kind='bar',color='#C3B49C')
    plt.xticks(rotation=0)
    plt.ylabel('Revenue ($)')
    plt.xlabel('Year')
    plt.title("Annual Revenue",fontsize = 16, fontweight = 'bold')
    plt.grid(linestyle='--',alpha = 0.7)
    plt.subplots_adjust(left= 0.15)

    image_path = os.path.join(superstore_path,'static','images','annual_revenue.png')
    plt.savefig(image_path)
    #plt.show()