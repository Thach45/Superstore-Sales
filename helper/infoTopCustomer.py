from helper.FormatNumber import format_number

def countUser(collection):  
    unique_names = collection.distinct("Name")  # Dùng hàm có sẵn distinct để tối ưu
    return format_number(len(unique_names),0)

def countUserPurchases(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$Name",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = max(total_purchases.values())
    return format_number(max_purchases,0)

def userMax(collection):  
    pipeline = [
        {
            "$group": {
                "_id": "$Name",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
    user = max_purchases[0][0]
    return user

