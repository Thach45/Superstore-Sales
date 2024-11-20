import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



if __name__=='__main__':

    # Lấy đường dẫn tuyệt đối đến file hiện tại
    current_file_path = os.path.realpath(__file__)

    # Lần ngược lên các cấp thư mục đến thư mục gốc (ở đây giả sử thư mục gốc có tên là 'project')
    while not os.path.basename(current_file_path) == 'Superstore-Sales':
        current_file_path = os.path.dirname(current_file_path)
    superstore_path = current_file_path
    file_path = os.path.join(superstore_path,'static','file','datacleaned.csv')
    data = pd.read_csv(file_path,sep = ',', header=0, index_col='Row ID')

    monthly_revenue_per_year = data.groupby(['Year','Month'])['Sales'].sum().sort_index()

    # tự động láy danh sách các năm
    years = monthly_revenue_per_year.index.levels[0].values

    months = [
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"
    ]

    data_revenue = {
        "Month": months,
    }
    # them các trường theo từng năm
    for year in years:
        data_revenue.update({f"year_{year}" : monthly_revenue_per_year[(year)]})
    df_revenues = pd.DataFrame(data_revenue)
    df_revenues.set_index('Month',inplace=True)

    # Tạo một subplot với kích thước tùy chỉnh
    #plt.figure(figsize=(12, 8))
    df_revenues.plot(kind= 'line',marker = '.')
    # Chỉnh sửa kích thước của biểu đồ sau khi vẽ
    fig = plt.gcf()  # Lấy đối tượng Figure hiện tại
    fig.set_size_inches(12, 6)  # Chiều rộng 12 inch, chiều cao 8 inch

    plt.xticks(np.arange(0,12,1),labels=months)
    plt.xlabel("Month")
    plt.ylabel("Revenue($)")
    plt.title("Monthly revenue per year",fontsize = 18, fontweight = 'bold')
    plt.grid(True, linestyle="--", alpha=0.7)

    image_path = os.path.join(superstore_path, 'static', 'images', 'monthly_revenue_per_year.png')
    plt.savefig(image_path)
    #plt.show()