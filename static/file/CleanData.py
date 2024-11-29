import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def CheckDate(date = ''):
    if len(date) > 10:
        return False
    if date.count('-') == 2:
        date = date.replace('-','/')
    if date.count('/') != 2:
        return False
    date = date.split('/')
    for x in date:
        if(int(x)) < 0:
            return False
    return True


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
    old_data = pd.read_csv(file_path,sep = ',', header=0)

    # 1. XOA TRUONG DU LIEU KO CAN THIET

    new_data={
        'RowID':[i for i in range(1,len(old_data['Row ID']))],
        'OrderID':[old_data['Order ID'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'OrderDate':[old_data['Order Date'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'ShipDate':[old_data['Ship Date'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'ShipMode':[old_data['Ship Mode'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'CustomerID':[old_data['Customer ID'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'CustomerName':[old_data['Customer Name'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'Segment':[old_data['Segment'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'City':[old_data['City'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'State':[old_data['State'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'Region':[old_data['Region'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'ProductID':[old_data['Product ID'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'Category':[old_data['Category'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'SubCategory':[old_data['Sub-Category'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'ProductName':[old_data['Product Name'].loc[i] for i in range(1,len(old_data['Row ID']))],
        'Sales':[old_data['Sales'].loc[i] for i in range(1,len(old_data['Row ID']))],
    }

    df_newdata = pd.DataFrame(new_data)
    df_newdata.set_index('RowID',inplace=True)
    # format date and splitdate
    df_newdata['OrderDate'] = df_newdata['OrderDate'].astype(str)
    for i in range(1,len(df_newdata.index.values)):
        if(CheckDate(df_newdata['OrderDate'].loc[i])==False or CheckDate(df_newdata['ShipDate'].loc[i])==False):
            df_newdata.drop(index=i)
    df_newdata['Month'] = [SplitDate(df_newdata.loc[i,'OrderDate'])[0] for i in df_newdata.index]
    df_newdata['Month'] = df_newdata['Month'].astype(int)
    df_newdata['Year'] = [SplitDate(df_newdata.loc[i,'OrderDate'])[1] for i in df_newdata.index]
    df_newdata['Year'] = df_newdata['Year'].astype(int)

    # 2. XOA DONG DU LIEU BI SAI (VALUE = NONE OR DUPLICATES)
    # remove row  have value = none
    df_newdata.dropna(inplace=True)
    df_newdata.drop_duplicates(inplace=True)
  
    # xuất file đã làm sạch
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_dir,'datacleaned.csv')
    df_newdata.to_csv(output_file)