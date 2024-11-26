
def countOrder(collection):  
    unique_names = collection.distinct("OrderID")  # Dùng hàm có sẵn distinct để tối ưu
    return (len(unique_names))

def countOrderPurchases(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$OrderID",
                "totalFrequency": {"$sum": "$Frequency"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalFrequency'] for item in result}
    max_purchases = max(total_purchases.values())
    return (max_purchases)

def orderMax(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$OrderID",
                "totalFrequency": {"$sum": "$Frequency"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalFrequency'] for item in result}
    max_purchases = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
    product = max_purchases[0][0]
    return product

def totalRevenue(collection):
    total_revenue = sum(item["TotalCost"] for item in collection.find())
    return (total_revenue)

def topRecent(collection):
    pipeline = [
        {
            "$sort": {"OrderDate": -1}
        },
        {
            "$limit": 3
        }
    ]
    result = list(collection.aggregate(pipeline))
    return result