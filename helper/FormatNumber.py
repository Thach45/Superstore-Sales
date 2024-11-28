def format_number(number, decimal_places=2):
    """định dạng lại các số"""
    # Nếu input là số, đảm bảo là chuỗi trước khi loại bỏ dấu phẩy
    if isinstance(number, (int, float)):
        number_str = str(number)
    else:
        # Nếu đầu vào là chuỗi, kiểm tra có dấu phẩy hay không
        number_str = number.replace(",", "")  

    number = float(number_str)

    return f"{number:,.{decimal_places}f}".replace(",", " ")

