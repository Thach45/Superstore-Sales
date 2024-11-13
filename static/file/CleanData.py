import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    old_data = pd.read_csv("train.csv")

    # 1. XOA TRUONG DU LIEU KO CAN THIET
    # remove 3 column unnecessary
    new_data = old_data .drop(columns= ['Postal Code','Region'])

    # format date
    #new_data['Order Date'] = pd.to_datetime(new_data['Order Date'])
    # new_data["Ship Date"] = pd.to_datetime(new_data["Ship Date"])

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
    max_price = {
        'Bookcases': 2000,
        'Chairs' : 2000,
        'Labels' : 400,
        'Tables' : 2000,
        'Storage' :1700,
        'Furnishings' : 800,
        'Art'  : 500,
        'Phones' : 2000,
        'Binders' : 2000,
        'Appliances' : 1000,
        'Paper'  : 500,
        'Accessories' : 1200,
        'Envelopes' : 500,
        'Fasteners' :100,
        'Supplies' : 1000,
        'Machines' : 4000,
        'Copiers' :3000
    }
    for i in new_data.index:
        sub_category = new_data.loc[i,'Sub-Category']
        if new_data.loc[i,'Sales'] > max_price[sub_category]:
            new_data.drop(i,inplace= True)    # xoa dong i, inplace = True de ko tao ra ban sao