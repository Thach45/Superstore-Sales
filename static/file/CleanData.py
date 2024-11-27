import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# loc truong name_col theo tu khoa: key
def CheckSales(dataframe :pd.DataFrame,name_field:str,name_category:str):
    list_result = []
    for i in dataframe.index:
        if dataframe.at[i,name_field] == name_category:
            list_result.append(dataframe.loc[i,"Sales"])
    return list_result

# VE BIEU DO THE HIEN SU TAP TRUNG GIA TRI CUA TUNG LOAI SP
def ScatterSales(dataframe :pd.DataFrame,name_field:str,name_category:str):
    """Sub-Category: ['Bookcases' 'Chairs' 'Labels' 'Tables' 'Storage' 'Furnishings' 'Art'
 'Phones' 'Binders' 'Appliances' 'Paper' 'Accessories' 'Envelopes'
 'Fasteners' 'Supplies' 'Machines' 'Copiers']"""
    Y = CheckSales(dataframe,name_field,name_category)
    X = [1]*len(Y)
    plt.scatter(X,Y,color = 'red', s=0.1)
    plt.xticks([1])
    plt.yticks(range(0,4500,500))
    plt.show()

def SplitDate(date=''):
    if(date.count('/')!=2):
        return False
    else:
        date = date.split('/')
        month = date[1]
        year = date[2]
    return month, year

if __name__ == "__main__":

    # Đường dẫn tới thư mục gốc của dự án
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Tạo đường dẫn tới file trong thư mục "data"
    file_path = os.path.join(base_dir, 'train.csv')  
    #old_data = pd.read_csv("D:\VS Code\Python\Github\Superstore-Sales\static\\file\\train.csv",sep = ',', header=0, index_col='Row ID')
    old_data = pd.read_csv(file_path,sep = ',', header=0)

    # 1. XOA TRUONG DU LIEU KO CAN THIET
    # remove 6 column unnecessary
    new_data = old_data .drop(columns= ['Country','Postal Code','Row ID'])

    # format date and splitdate
    new_data['Order Date'] = new_data['Order Date'].astype(str)
    new_data['Month'] = [SplitDate(new_data.loc[i,'Order Date'])[0] for i in new_data.index]
    new_data['Month'] = new_data['Month'].astype(int)
    new_data['Year'] = [SplitDate(new_data.loc[i,'Order Date'])[1] for i in new_data.index]
    new_data['Year'] = new_data['Year'].astype(int)
    new_data['Quarter'] = pd.cut(new_data['Month'], bins= [0,3,6,9,12], labels= ['Quarter1','Quarter2','Quarter3','Quarter4'])

    # 2. XOA DONG DU LIEU BI SAI (VALUE = NONE OR DUPLICATES)
    # remove row  have value = none
    new_data.dropna(inplace=True)

    # Kiem tra du lieu bi trung
    # series_duplicated = new_data.duplicated()
    # for i in range(0,series_duplicated.size):
    #     if(series_duplicated[i] == True):     // True: du lieu da bi trung lap
    #         print(i)
    new_data.drop_duplicates(inplace=True)

    # 3. XOA DONG DU LIEU CO GIA TRI RAT KHAC MIEN GIA TRI TAP TRUNG
    # max_price of sub-category
    # max_price = {
    #     'Bookcases': 2000,
    #     'Chairs' : 2000,
    #     'Labels' : 400,
    #     'Tables' : 2000,
    #     'Storage' :1700,
    #     'Furnishings' : 800,
    #     'Art'  : 500,
    #     'Phones' : 2000,
    #     'Binders' : 2000,
    #     'Appliances' : 1000,
    #     'Paper'  : 500,
    #     'Accessories' : 1200,
    #     'Envelopes' : 500,
    #     'Fasteners' :100,
    #     'Supplies' : 1000,
    #     'Machines' : 4000,
    #     'Copiers' :3000
    # }
    # for i in new_data.index:
    #     sub_category = new_data.loc[i,'Sub-Category']
    #     if new_data.loc[i,'Sales'] > max_price[sub_category]:
    #         new_data.drop(i,inplace= True)    # xoa dong i, inplace = True de ko tao ra ban 
    
    # xuất file đã làm sạch
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_dir,'datacleaned.csv')
    new_data.to_csv(output_file)