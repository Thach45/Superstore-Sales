import pandas as pd
import os
from file_object.customer import Customer

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,'datacleaned.csv')
    datacleaned = pd.read_csv(file_path,sep =',',header = 0)

    customers = {}
    for i in range(0,datacleaned.index.values.size):
        id = datacleaned.loc[i,'CustomerID']
        revenue = datacleaned.loc[i,'Sales']
        name = datacleaned.loc[i,'CustomerName']
        segment = datacleaned.loc[i,'Segment']
        city = datacleaned.loc[i,'City']
        state = datacleaned.loc[i,'State']
        region = datacleaned.loc[i,'Region']
        if id in customers.keys():
            customers[id].addquantity_purchase()
            customers[id].addrevenue(revenue)
        else:
            customers.update({id:Customer(name,id,segment,city,state,region,revenue)})
    
    dataCustomer = {
        'RowID' : [i for i in range(1,len(customers)+1)],
        'Name': [customers[id].name for id in customers.keys()],
        'IDCustomer': [customers[id].id for id in customers.keys()],
        'Segment': [customers[id].segment for id in customers.keys()],
        'City': [customers[id].city for id in customers.keys()],
        'State': [customers[id].state for id in customers.keys()],
        'Region' : [customers[id].region for id in customers.keys()],
        'Quantity' : [customers[id].quantity_purchase for id in customers.keys()],
    }
    df_dataCustomer = pd.DataFrame(dataCustomer)

    df_dataCustomer.set_index('RowID',inplace=True)
    

    output_file = os.path.join(base_dir,'dataCustomer.csv')
    df_dataCustomer.to_csv(output_file)

