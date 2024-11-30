import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


if __name__ == "__main__":

    # Đường dẫn tới thư mục gốc của dự án
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Tạo đường dẫn tới file trong thư mục "data"
    file_path = os.path.join(base_dir, 'train.csv')  
    old_data = pd.read_csv(file_path,sep = ',', header=0)

    # print(old_data.duplicated().sum())
    # print(old_data.isna().sum())

    # 1. XOA TRUONG DU LIEU KO CAN THIET

    new_data={
        'RowID':[i for i in range(1,len(old_data['Row ID'])+1)],
        'OrderID':old_data['Order ID'],
        'OrderDate':old_data['Order Date'],
        'ShipDate':old_data['Ship Date'],
        'ShipMode':old_data['Ship Mode'],
        'CustomerID':old_data['Customer ID'],
        'CustomerName':old_data['Customer Name'],
        'Segment':old_data['Segment'],
        'City':old_data['City'],
        'State':old_data['State'],
        'Region':old_data['Region'],
        'ProductID':old_data['Product ID'],
        'Category':old_data['Category'],
        'SubCategory':old_data['Sub-Category'],
        'ProductName':old_data['Product Name'],
        'Sales':old_data['Sales'],
    }


    df_newdata = pd.DataFrame(new_data)
    df_newdata.set_index('RowID',inplace=True)

    df_newdata['OrderDate'] = pd.to_datetime(df_newdata['OrderDate'], format='%d/%m/%Y')
    df_newdata['ShipDate'] = pd.to_datetime(df_newdata['ShipDate'], format='%d/%m/%Y')
    df_newdata['Month'] = df_newdata['OrderDate'].dt.month
    df_newdata['Year'] = df_newdata['OrderDate'].dt.year

    # 2. XOA DONG DU LIEU BI SAI (VALUE = NONE OR DUPLICATES)

    df_newdata.dropna(inplace=True)
    # duplicated = df_newdata.duplicated()
    # print(duplicated[duplicated==True])
    df_newdata.drop_duplicates(inplace=True)
  
    print(df_newdata.info())

    # xuất file đã làm sạch
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_dir,'datacleaned.csv')
    df_newdata.to_csv(output_file)