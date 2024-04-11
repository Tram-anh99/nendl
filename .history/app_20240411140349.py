from flask import Flask, render_template, request

app = Flask(__name__)

# Route để hiển thị form nhập giá trị a và b
@app.route('/')
def index():
    return render_template('indexs.html')

# Route để xử lý việc nhập giá trị a và b và gọi hàm arithmetic_operations
@app.route('/calculate', methods=['POST'])
def calculate():
    # Lấy giá trị của a và b từ form
    a = float(request.form['a'])
    b = float(request.form['b'])

    # Gọi hàm arithmetic_operations để thực hiện các phép toán
    result_addition, result_subtraction, result_multiplication, result_division = arithmetic_operations(a, b)

    # Hiển thị kết quả
    return f"""
    <h1>Kết quả các phép toán:</h1>
    <p>Cộng: {result_addition}</p>
    <p>Trừ: {result_subtraction}</p>
    <p>Nhân: {result_multiplication}</p>
    <p>Chia: {result_division}</p>
    """

# Hàm thực hiện các phép toán (bạn có thể đặt hàm này trong một file riêng)
def arithmetic_operations(a, b):
    # Các phép toán
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    
    return addition, subtraction, multiplication, division

if __name__ == '__main__':
    app.run(debug=True)
