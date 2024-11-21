def format_number(number, decimal_places=2):
    # Nếu input là số, đảm bảo là chuỗi trước khi loại bỏ dấu phẩy
    if isinstance(number, (int, float)):
        number_str = str(number) 
    else:
        # Nếu đầu vào là chuỗi, kiểm tra có dấu phẩy hay không
        number_str = number.replace(",", "")  

    # Chuyển chuỗi đã chuẩn hóa thành float
    number = float(number_str)

    # Trả về chuỗi đã được định dạng
    return f"{number:,.{decimal_places}f}"

def format_number1(number, decimal_places=2):
    # Nếu input là số, đảm bảo là chuỗi trước khi loại bỏ dấu phẩy
    if isinstance(number, (int)):
        number_str = str(number) 
    else:
        # Nếu đầu vào là chuỗi, kiểm tra có dấu phẩy hay không
        number_str = number.replace(",", "")  

    # Chuyển chuỗi đã chuẩn hóa thành float
    number = int(number_str)

    # Trả về chuỗi đã được định dạng
    return f"{number:,}"

