from helper.FormatNumber import format_number
def countOrder(collection):  
    unique_names = collection.distinct("OrderID")  # Dùng hàm có sẵn distinct để tối ưu
    return format_number(len(unique_names),0)

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
    return format_number(max_purchases,0)

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
    return format_number(total_revenue)

def topRecent(collection):
    pipeline = [
        # Chuyển đổi trường OrderDate từ kiểu chuỗi thành kiểu datetime (nếu cần thiết)
        {
            '$addFields': {
                'OrderDate': {
                    '$dateFromString': {
                        'dateString': '$OrderDate',  # Chọn trường OrderDate từ tài liệu
                        'format': '%d/%m/%Y'  # Định dạng ngày tháng là ngày/tháng/năm
                    }
                }
            }
        },
        # Sắp xếp các bản ghi theo OrderDate (mới nhất trước)
        {
            '$sort': {
                'OrderDate': -1  # -1 là sắp xếp giảm dần (mới nhất lên đầu)
            }
        },
        # Giới hạn số lượng bản ghi trả về là 3
        {
            '$limit': 3  # Chỉ lấy 3 bản ghi gần nhất
        },
        # Chọn các trường cần thiết để trả về: OrderID, OrderDate và CustomerName
        {
            '$project': {
                'OrderID': 1,  # Chọn trường OrderID
                'OrderDate': 1,  # Chọn trường OrderDate
                'CustomerName': 1  # Chọn trường CustomerName
            }
        }
    ]
    
    # Thực thi pipeline trên collection và lấy kết quả
    recent_products = collection.aggregate(pipeline)
    
    # Khởi tạo danh sách để lưu kết quả
    list_recent = []
    for i in recent_products:
        # Thêm vào danh sách kết quả theo định dạng: [OrderID, OrderDate, CustomerName]
        list_recent.append([i['OrderID'], i['OrderDate'].strftime('%d/%m/%Y'), i['CustomerName']])
    
    # Trả về danh sách kết quả
    return list_recent
