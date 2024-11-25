from helper.FormatNumber import format_number

def countProduct(collection):  
    unique_names = collection.distinct("ProductName")  # Dùng hàm có sẵn distinct để tối ưu
    return format_number(len(unique_names),0)

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
    return format_number(max_purchases,0)

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

def TopProduct(collection):
    orderDate = list(collection.find({}, {"ProductName": 1, "Revenue": 1, "Quantity": 1}).sort("Revenue", -1).limit(3))
    return orderDate


