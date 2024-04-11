def arithmetic_operations():
    # Nhập giá trị của a và b từ người dùng
    a = float(input("Nhập giá trị của a: "))
    b = float(input("Nhập giá trị của b: "))

    # Cộng
    addition = a + b
    
    # Trừ
    subtraction = a - b
    
    # Nhân
    multiplication = a * b
    
    # Chia (lưu ý kiểm tra chia cho 0)
    division = a / b if b != 0 else None
    
    return addition, subtraction, multiplication, division

# Sử dụng hàm arithmetic_operations để thực hiện các phép toán
result_addition, result_subtraction, result_multiplication, result_division = arithmetic_operations()

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
