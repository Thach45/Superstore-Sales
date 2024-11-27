class Product:
    """STT,Product Name,	Category,	Sub-Category,	Revenue,  Quantity"""
    def __init__(self,name,category,sub_category,revenue):
        self.__name = name
        self.__category = category
        self.__sub_category = sub_category
        self.__quantity = 1
        self.__revenue = revenue
    
    @property
    def name(self):
        return self.__name
    @property
    def category(self):
        return self.__category
    @property
    def sub_category(self):
        return self.__sub_category
    @property
    def quantity(self):
        return self.__quantity
    def addquantity(self):
        self.__quantity+=1

    @property
    def revenue(self):
        return self.__revenue

    def addrevenue(self,value):
        self.__revenue =  round(value+self.__revenue,2)
        
