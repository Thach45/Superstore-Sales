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

    year_request = 2018
    data_year_2018 = data[data['Year']==year_request]
    chart_revenue_2018 = data_year_2018.groupby(['Month'])['Sales'].sum().sort_index()
    chart_revenue_2018.plot.bar()
    plt.xlabel('month')
    plt.ylabel('revenue')
    plt.title(f"Revenues of {year_request}")
    plt.show()
    