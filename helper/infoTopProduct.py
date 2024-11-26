
def countProduct(collection):  
    unique_names = collection.distinct("ProductName")  # Dùng hàm có sẵn distinct để tối ưu
    return (len(unique_names))

def countProductPurchases(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$ProductName",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = max(total_purchases.values())
    return (max_purchases)

def productMax(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$ProductName",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
    product = max_purchases[0][0]
    return product

