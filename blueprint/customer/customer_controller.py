from flask import render_template, request, current_app
import pandas as pd
import os
import matplotlib.pyplot as plt
from helper.infoTopCustomer import countUser, countUserPurchases, userMax

def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.users  # Sử dụng cú pháp dấu chấm để truy cập collection
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    # Bước 1: Lấy dữ liệu từ MongoDB
    data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả dữ liệu từ collection
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)
    # Bước 2: Chuyển đổi đối tượng ObjectId thành chuỗi (nếu có)
    for item in data:
        item['_id'] = str(item['_id'])

    # tạo biểu đồ
    states = list(collection.find({}, {"State": 1, "_id": 0}))
    states = [item['State'] for item in states]
    region = list(collection.find({}, {"Region": 1, "_id": 0}))
    region = [item['Region'] for item in region]
    segment = list(collection.find({}, {"Segment": 1, "_id": 0}))
    segment = [item['Segment'] for item in segment]
    if states:
        state_counts = pd.Series(states).value_counts()
        state_counts = state_counts.sort_values(ascending=False)
        top_states = state_counts.head(5)
        # Sum the rest as 'Others'
        others = state_counts.iloc[5:].sum()
        others_series = pd.Series({'Others': others})
        # Concatenate the top states with 'Others'
        state_counts = pd.concat([top_states, others_series])
        plt.figure(figsize=(6, 6))
        color1 = ['#99C1A9','#CE5C5B','#EBCB78','#73B6E1','#A693C1','#6757D5','#EE7245','#D45834','#A1D1E7']
        explode_state = [0.02]*len(state_counts)
        plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%',colors=color1,explode=explode_state)
        plt.title('Distribution of States')
        # Lưu biểu đồ vào một tệp
        image_path = os.path.join(current_app.root_path, 'static', 'images', 'state_distribution.png')
        plt.savefig(image_path)
        plt.close()
    if region:
        region_counts = pd.Series(region).value_counts()
        plt.figure(figsize=(6, 6))
        color2 = ['#6757D5','#CE5C5B','#EBCB78','#EE7245','#D45834','#99C1A9','#73B6E1','#A693C1','#A1D1E7']
        explode_region = [0.02]*len(region_counts)
        plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%',colors=color2,explode=explode_region)
        plt.title('Distribution of Regions')
        # Lưu biểu đồ vào một tệp
        image_path = os.path.join(current_app.root_path, 'static', 'images', 'region_distribution.png')
        plt.savefig(image_path)
        plt.close()
    if segment:
        segment_counts = pd.Series(segment).value_counts()
        plt.figure(figsize=(6, 6))
        color3 = ['#99C1A9','#73B6E1','#A693C1','#EBCB78','#73B6E1','#CE5C5B','#6757D5','#EE7245']
        explode_segment = [0.02]*len(segment_counts)
        plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%',colors=color3,explode=explode_segment)
        plt.title('Distribution of Segments')
        # Lưu biểu đồ vào một tệp
        image_path = os.path.join(current_app.root_path, 'static', 'images', 'segment_distribution.png')
        plt.savefig(image_path)
        plt.close()

    return render_template('customer.html',
                        records=data,
                        page=page, 
                        total_pages=total_pages, 
                        totalUser=countUser(collection), 
                        totalPurchases=countUserPurchases(collection), 
                        user=userMax(collection), 
                        states=set(states)
                        )

