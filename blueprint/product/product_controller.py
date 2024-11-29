from flask import render_template, request, current_app
import pandas as pd
import matplotlib.pyplot as plt
import os
from helper.infoTopProduct import countProduct,countProductPurchases,productMax

def index():
    mongo = current_app.config['MONGO']
    collection = mongo.db.products  # Sử dụng cú pháp dấu chấm để truy cập collection
    page = int(request.args.get('page', 1))
    limit = 20
    skip = (page - 1) * limit 
    categoryFull = list(collection.find({},{"Category":1,"_id":0}))
    Category = [item['Category'] for item in categoryFull]
    subcategoryFull = list(collection.find({},{"SubCategory":1,"_id":0}))
    SubCategory = [item['SubCategory'] for item in subcategoryFull]

    # Biểu đồ phân phối theo Sub-Category
    if SubCategory:
        subcategory_counts = pd.Series(SubCategory).value_counts().sort_values(ascending=False)
        topSubCategory = subcategory_counts.head(6)
        others = subcategory_counts[6:].sum()
        others_series = pd.Series({'Others': others})
        # Concatenate the top states with 'Others'
        subcategory_counts = pd.concat([topSubCategory, others_series])
        plt.figure(figsize=(6, 6))
        color1 = ['#99C1A9','#CE5C5B','#EBCB78','#73B6E1','#A693C1','#6757D5','#EE7245','#D45834','#A1D1E7']
        explode_subcategory = [0.02]*len(subcategory_counts)
        plt.pie(subcategory_counts, labels=subcategory_counts.index, autopct='%1.1f%%',colors=color1,explode=explode_subcategory)
        plt.title('Distribution of SubCategories')
        image_path = os.path.join(current_app.root_path, 'static', 'images', 'subcategory_distribution.png')
        plt.savefig(image_path)
        plt.close()

    # Biểu đồ phân phối theo Category
    if Category:
        category_counts = pd.Series(Category).value_counts()
        plt.figure(figsize=(6, 6))
        color2 = ['#CE5C5B','#EBCB78','#99C1A9','#73B6E1','#A693C1','#6757D5','#EE7245','#D45834','#A1D1E7']
        explode_category = [0.02]*len(category_counts)
        plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',colors=color1,explode=explode_category)
        plt.title('Distribution of Categories')
        # Lưu biểu đồ vào một tệp
        image_path = os.path.join(current_app.root_path, 'static', 'images', 'category_distribution.png')
        plt.savefig(image_path)
        plt.close()
        
    # Bước 1: Lấy dữ liệu từ MongoDB
    data = list(collection.find().skip(skip).limit(limit))  # Trả về tất cả dữ liệu từ collection
    total_records = collection.count_documents({})
    total_pages = (total_records // limit) + (1 if total_records % limit > 0 else 0)


    return render_template('product.html',
                            records=data,
                            page=page, 
                            total_pages=total_pages, 
                            totalProduct=countProduct(collection), 
                            totalPurchases=countProductPurchases(collection), 
                            product=productMax(collection)
                            )
    
    