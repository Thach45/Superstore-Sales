from flask import Flask, render_template, request

def home():
    search_name = request.args.get('key', '')  # Lấy tham số 'name' từ URL và chuyển về chữ thường
    print(search_name)
    return render_template("customer.html",data=search_name)
    