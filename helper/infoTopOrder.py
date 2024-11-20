def countOrder(collection):  
    unique_names = collection.distinct("OrderID")  # Dùng hàm có sẵn distinct để tối ưu
    return len(unique_names)

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
    return max_purchases

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

