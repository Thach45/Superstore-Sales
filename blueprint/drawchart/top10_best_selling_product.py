import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



if __name__=='__main__':
    current_file_path = os.path.realpath(__file__)

    while not os.path.basename(current_file_path) == 'Superstore-Sales':
        current_file_path = os.path.dirname(current_file_path)
    superstore_path = current_file_path
    file_path = os.path.join(superstore_path,'static','file','datacleaned.csv')
    data = pd.read_csv(file_path)

    product_data ={
        'Product Name' : data['Product Name'], #Product Name
        'Sales quantity' : 1,
        'Revenue': data['Sales']
    }

    df_product_data = pd.DataFrame(product_data)
    top10_product_bestselling = df_product_data.groupby(['Product Name'])['Sales quantity'].sum().sort_values(ascending=False)[:11]
    top10_product_bestselling.plot(kind="barh")
    print(top10_product_bestselling)
    plt.subplots_adjust(left= 0.6)
    # fig = plt.gcf()
    # fig.set_size_inches(10,6)
    plt.show()
    #print(top10_product_bestselling)
    #print(product_best_selling)
    