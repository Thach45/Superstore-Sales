

def TopRecent(collection):
    #sản phẩm gần nhất
    pipeline = [
    # Chuyển đổi trường "OrderDate" từ chuỗi thành datetime (nếu cần thiết)
    {
        '$addFields': {
            'OrderDate': {
                '$dateFromString': {
                    'dateString': '$OrderDate',
                    'format': '%d/%m/%Y'
                }
            }
        }
    },
    # Sắp xếp các bản ghi theo "OrderDate"
    {
        '$sort': {
            'OrderDate': -1  # Sắp xếp theo thứ tự tăng dần (1) hoặc giảm dần (-1)
        }
    },
    # Giới hạn số lượng bản ghi trả về là 3
    {
        '$limit': 3
    },
    # Chọn các trường bạn muốn (nếu cần thiết)
    {
        '$project': {
            'OrderID': 1,
            'CustomerName': 1,
            'Sales': 1,
            'OrderDate': 1,
            'ProductName': 1
        }
    }
]
    # Thực thi aggregate pipeline
    recent_products = collection.aggregate(pipeline)
    list_recent = []
    for i in recent_products:
        list_recent.append([i['OrderID'],i['CustomerName'],i['ProductName'],i['Sales']])
    return list_recent
    
def TotalSales(collection):
    #tổng doanh thu
    total_sales = collection.aggregate([
        {
            '$group': {
                '_id': None,  # Không phân nhóm, tính tổng cho tất cả các phần tử
                'total_sales': {'$sum': '$Sales'}  # Tính tổng trường 'sale'
            }
        }
    ])
    total_sales_result = list(total_sales)  # Chuyển CommandCursor thành danh sách
    total_sales_value = total_sales_result[0]['total_sales']
    total_sales_value = (total_sales_value)
    return total_sales_value
    
def TopProduct(collection):
    orderDate = list(collection.find({}, {"ProductName": 1, "Revenue": 1, "Quantity": 1}).sort("Revenue", -1).limit(3))
    return orderDate

    