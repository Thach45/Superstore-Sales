import pandas as pd
import os
from file_object.order import Order

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,'datacleaned.csv')
    datacleaned = pd.read_csv(file_path,sep =',',header = 0)

    orders = {}
    for i in range(0,datacleaned.index.values.size):
        order_id = datacleaned.loc[i,'Order ID']
        order_date = datacleaned.loc[i,'Order Date']
        ship_date = datacleaned.loc[i,'Ship Date']
        customer_name = datacleaned.loc[i,'Customer Name']
        customer_id = datacleaned.loc[i,'Customer ID']
        cost = datacleaned.loc[i,'Sales']

        if order_id in orders.keys():
            orders[order_id].addfrequency()
            orders[order_id].addcost(cost)
        else:
            orders.update({order_id:Order(order_id,order_date,ship_date,customer_name,customer_id,cost)})
    
    dataCustomer = {
        'RowID' : [i for i in range(1,len(orders)+1)],
        'OrderID': [orders[order_id].order_id for order_id in orders.keys()],
        'OrderDate': [orders[order_id].order_date for order_id in orders.keys()],
        'ShipDate': [orders[order_id].ship_date for order_id in orders.keys()],
        'CustomerName': [orders[order_id].customer_name for order_id in orders.keys()],
        'CustomerID': [orders[order_id].customer_id for order_id in orders.keys()],
        'Costs' : [orders[order_id].cost for order_id in orders.keys()],
        'Frequency' : [orders[order_id].frequency for order_id in orders.keys()],
        # 'cost' : [orders[order_id].cost for order_id in orders.keys()]
    }
    df_dataCustomer = pd.DataFrame(dataCustomer)
    output_file = os.path.join(base_dir,'dataOrder.csv')
    df_dataCustomer.to_csv(output_file)
    print(df_dataCustomer.head())
