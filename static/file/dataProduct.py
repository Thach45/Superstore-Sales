import pandas as pd
import os
from file_object.product import Product

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,'datacleaned.csv')
    datacleaned = pd.read_csv(file_path,sep =',',header = 0)

    products = {}
    for i in range(0,datacleaned.index.values.size):
        name = datacleaned.loc[i,'ProductName']
        category = datacleaned.loc[i,'Category']
        sub_category = datacleaned.loc[i,'SubCategory']
        revenue = datacleaned.loc[i,'Sales']
        if name in products.keys():
            products[name].addquantity()
            products[name].addrevenue(revenue)
        else:
            products.update({name:Product(name,category,sub_category,revenue)})
    # for name in products.keys():
    #     print(products[name].category)
    dataProduct = {
        'RowID' : [i for i in range(1,len(products)+1)],
        'ProductName': [products[name].name for name in products.keys()],
        'Category': [products[name].category for name in products.keys()],
        'SubCategory': [products[name].sub_category for name in products.keys()],
        'Revenue' : [products[name].revenue for name in products.keys()],
        'Quantity' : [products[name].quantity for name in products.keys()],
        # 'Revenue' : [products[id].revenue for id in products.keys()]
    }
    df_dataProduct = pd.DataFrame(dataProduct)
    df_dataProduct.set_index('RowID',inplace=True)
    output_file = os.path.join(base_dir,'dataProduct.csv')
    df_dataProduct.to_csv(output_file)
    #print(df_dataProduct.head())
