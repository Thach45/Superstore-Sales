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
    
    ship_mode = {
        'Ship Mode': data['Ship Mode'],
        'count': 1
    }
    df_shipmode = pd.DataFrame(ship_mode)
    shipmode_structure = df_shipmode.groupby(['Ship Mode'])['count'].sum()

    shipmode_structure.name = ''
    colors = ['yellowgreen', 'lightcoral', 'lightskyblue','gold']
    shipmode_structure.plot(kind='pie',colors=colors, autopct='%1.2f%%', startangle=90,radius = 0.9)
    plt.title("Ship Mode sructure")
    
    image_path = os.path.join(superstore_path, 'static', 'images', 'shipmode_structure.png')
    plt.savefig(image_path)
    #plt.show()