from flask import Flask, render_template, request
from pymongo import MongoClient

def home():
    search_name = request.args.get('Name', '').lower()  # Lấy tham số 'name' từ URL và chuyển về chữ thường
    print(search_name)
    return render_template("customer.html",data=search_name)
    