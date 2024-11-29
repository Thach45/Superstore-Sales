import csv
import os
from flask import current_app
def downloadFile(collection, nameFile):
    data = list(collection.find({}, {"_id": 0}))
    
    if not data:
        print("No data found in the collection.")
        return
    
    output_path = os.path.join(current_app.root_path, 'static','download', f'{nameFile}.csv')
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())
    return output_path
