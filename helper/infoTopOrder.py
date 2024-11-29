from helper.FormatNumber import format_number
def countOrder(collection):  
    """Đếm số lượng đơn hàng"""
    unique_names = collection.distinct("OrderID")  # Dùng hàm có sẵn distinct để tối ưu
    return format_number(len(unique_names),0)

def countOrderPurchases(collection): 
    """Lấy ra số tiền thu về nhiều nhất từ đơn hàng""" 
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
    return format_number(max_purchases,0)

def orderMax(collection):  
    """Lấy ra đơn hàng thu về nhiều tiền nhất"""
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
    """Tính tổng doanh thu"""
    total_revenue = sum(item["TotalCost"] for item in collection.find())
    return format_number(total_revenue)

def topRecent(collection):
    """Lấy ra thông tin của 3 sản phẩm gần nhất"""
    pipeline = [
        {
            '$addFields': {
                'OrderDate': {
                    '$dateFromString': {
                        'dateString': '$OrderDate', 
                        'format': '%d/%m/%Y'  # Định dạng ngày tháng là ngày/tháng/năm
                    }
                }
            }
        },
        {
            '$sort': {
                'OrderDate': -1 
            }
        },
        {
            '$limit': 3 
        },
        {
            '$project': {
                'OrderID': 1, 
                'OrderDate': 1,  
                'CustomerName': 1  
            }
        }
    ]
    
    # Thực thi pipeline trên collection và lấy kết quả
    recent_products = collection.aggregate(pipeline)
    list_recent = []
    for i in recent_products:
        list_recent.append([i['OrderID'], i['OrderDate'].strftime('%d/%m/%Y'), i['CustomerName']])
    return list_recent
