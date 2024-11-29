class Order:
    """OrderID,	OrderDate, ShipDate, CustomerName, CustomerID, Costs, Frequency"""
    def __init__(self,order_id, order_date, ship_date,customer_name, customer_id,cost):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__ship_date = ship_date
        self.__customer_name = customer_name
        self.__customer_id = customer_id
        self.__cost = cost
        self.__frequency = 1
    
    @property
    def order_id(self):
        return self.__order_id
    @property
    def order_date(self):
        return self.__order_date
    @property
    def ship_date(self):
        return self.__ship_date
    @property
    def customer_name(self):
        return self.__customer_name
    @property
    def customer_id(self):
        return self.__customer_id
    @property
    def cost(self):
        return self.__cost

    def addcost(self,value):
        self.__cost=round(value+self.__cost,2)

    @property
    def frequency(self):
        return self.__frequency

    def addfrequency(self):
        self.__frequency+=1
        
