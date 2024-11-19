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
    
    segments = {
        'Segment': data['Segment'],
        'count': 1
    }
    df_segment = pd.DataFrame(segments)
    segment_structure = df_segment.groupby(['Segment'])['count'].sum()

    segment_structure.name = ''
    colors = ['#73B6E1','#99C1A9','#CE5C5B','#A693C1','#A1D1E7','#EBCB78']
    explode = [0.015]*len(segment_structure.index)
    segment_structure.plot(kind='pie',colors=colors, autopct='%1.2f%%', startangle=90,radius = 1,explode = explode)
    plt.title("Segment Structure",fontsize = 16, fontweight = 'bold')
    
    image_path = os.path.join(superstore_path, 'static', 'images', 'segment_structure.png')
    plt.savefig(image_path)
    plt.show()