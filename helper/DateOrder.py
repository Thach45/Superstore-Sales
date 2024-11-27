from collections import OrderedDict
import pandas as pd

def MonthYearOrder(collection):
    MonthYearOrder = collection.distinct("OrderDate")
    MonthYearOrder = pd.to_datetime(MonthYearOrder, format='%d/%m/%Y')
    MonthYearOrder = MonthYearOrder.to_period('M').sort_values()
    MonthYearOrder = MonthYearOrder.strftime('%m/%Y')
    MonthYearOrder = list(OrderedDict.fromkeys(MonthYearOrder))
    return MonthYearOrder
def MonthYearShip(collection):
    MonthYearShip = collection.distinct("ShipDate")
    MonthYearShip = pd.to_datetime(MonthYearShip, format='%d/%m/%Y')
    MonthYearShip = MonthYearShip.to_period('M').sort_values()
    MonthYearShip = MonthYearShip.strftime('%m/%Y')
    MonthYearShip = list(OrderedDict.fromkeys(MonthYearShip))
    return MonthYearShip