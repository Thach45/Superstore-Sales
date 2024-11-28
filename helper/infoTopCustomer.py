from helper.FormatNumber import format_number

def countUser(collection):
    """Đếm số lượng khách hàng"""  
    unique_names = collection.distinct("IDCustomer")  # Dùng hàm có sẵn distinct để tối ưu
    return format_number(len(unique_names),0)

def countUserPurchases(collection):
    """Lấy ra số lượng đơn hàng cao nhất của khách hàng"""  
    pipeline = [
        {
            "$group": {
                "_id": "$IDCustomer",
                "totalQuantity": {"$sum": "$Quantity"}
            }
        }
    ]
    result = list(collection.aggregate(pipeline))
    total_purchases = {item['_id']: item['totalQuantity'] for item in result}
    max_purchases = max(total_purchases.values())
    return format_number(max_purchases,0)

def userMax(collection):
    """Lấy ra khách hàng mua nhiều nhất"""  
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

