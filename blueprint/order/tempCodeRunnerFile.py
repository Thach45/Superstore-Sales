collection = mongo.db.orders  # Sử dụng cú pháp dấu chấm để truy cập collection
page = int(request.args.get('page', 1))
limit = 20
skip = (page - 1) * limit 
orderDate = list(collection.find({},{"OrderDate":1,"Frequency":1,"_id":0}))
orderDate = pd.DataFrame(orderDate)
orderDate['OrderDate'] = pd.to_datetime(orderDate['OrderDate'], format='%d/%m/%Y')
orderDate['Year'] = orderDate['OrderDate'].dt.year
orderDate['Month'] = orderDate['OrderDate'].dt.month

order_frequency = orderDate.groupby(['Year', 'Month'])['Frequency'].sum().reset_index()

plt.figure(figsize=(10, 5))
for year in order_frequency['Year'].unique():
    yearly_data = order_frequency[order_frequency['Year'] == year]
    plt.plot(yearly_data['Month'], yearly_data['Frequency'], marker='o', linestyle='-',linewidth=4, label=str(year))

plt.xticks(range(1, 13))
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.title('Order Frequency by Year')
plt.legend(title='Year')
plt.tight_layout()

plt.grid(linestyle='--',alpha = 0.7)
plt.show()