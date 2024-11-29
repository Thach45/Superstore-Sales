class Customer:
    """Name, IDCustomer, Segment, CityState, Region, Quantity"""
    def __init__(self,name, id,segment, city, state,region,revenue):
        self.__name = name
        self.__id = id
        self.__segment = segment
        self.__city = city
        self.__state = state
        self.__region = region
        self.__quantity_purchase = 1
        self.__revenue = revenue
    
    @property
    def name(self):
        return self.__name
    @property
    def id(self):
        return self.__id
    @property
    def segment(self):
        return self.__segment
    @property
    def city(self):
        return self.__city
    @property
    def state(self):
        return self.__state
    @property
    def region(self):
        return self.__region
    
    @property
    def quantity_purchase(self):
        return self.__quantity_purchase

    def addquantity_purchase(self):
        self.__quantity_purchase+=1

    @property
    def revenue(self):
        return self.__revenue

    def addrevenue(self,value):
        self.__revenue=round(value+self.__revenue,2)
        
