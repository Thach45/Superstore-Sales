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
    file_path = os.path.join(superstore_path,'static','file','dataCustomer.csv')
    data = pd.read_csv(file_path)#,sep=',',index_col='Row ID',header=0)
    
    data['count_people_in_state'] = 1
    top3_state_mostpeople = data.groupby(['State'])['count_people_in_state'].sum().sort_values(ascending=False)[:3]
    top3_states = top3_state_mostpeople.index.values.tolist()
    count_people_in_top3state = top3_state_mostpeople[:3].tolist()

    top3_states.append('other')
    sum_top3 = sum(top3_state_mostpeople)
    count_people_in_top3state.append(data['CustomerID'].size-sum_top3)

    colors = ['#EBCB78','#99C1A9','#A693C1','#CE5C5B','#73B6E1','#A1D1E7']
    explode = [0.015]*len(top3_states)
    plt.pie(count_people_in_top3state,labels=top3_states,colors=colors,autopct='%1.2f%%', startangle=90,radius = 0.9, explode = explode, textprops={'fontsize': 10})
    plt.title("Top 3 cities with the most shoppers")
    image_path = os.path.join(superstore_path,'static','images','pieState.png')
    plt.savefig(image_path)