plt.close()

    # # Bước 1: Lấy dữ liệu từ MongoDB
    # data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả dữ liệu từ collection
    # total_records = collection.count_documents({})
    # total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    # # Bước 2: Chuyển đổi đối tượng ObjectId thành chuỗi (nếu có)
    # for item in data:
    #     item['_id'] = str(item['_id'])


    # return render_template('order.html', records=data, page=page, total_pages=total_pages, totalOrder=countOrder(collection), totalPurchases=countOrderPurchases(collection), order=orderMax(collection))
