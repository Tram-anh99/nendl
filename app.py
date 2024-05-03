import ee
import geemap # type: ignore
import os
import subprocess
from flask import Flask, render_template, request
from dtcn import dientich_chunhat
import gee_v1
# from code.lossless import main

app = Flask(__name__)

ee.Initialize()
aoi = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2") \
        .filter(ee.Filter.eq('ADM1_NAME', 'Ho Chi Minh City'))

# Route để hiển thị form nhập giá trị a và b
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dtcn', methods=['GET', 'POST'])
def dientich():
    if request.method == 'POST':
        side_a = float(request.form['side_a'])
        side_b = float(request.form['side_b'])
        area = dientich_chunhat(side_a, side_b)
        return render_template('dtcn.html', area=area)
    return render_template('dtcn.html')

@app.route('/nhietdo', methods=['GET', 'POST'])
def tinhnhietdo():
    if request.method == 'POST':
        year = float(request.form['year'])
        kq = gee_v1.nhietdo(year)
        return render_template('index.html', year=year, kq=kq)
    return render_template('index.html')

@app.route('/run_main', methods=['POST'])
def run_main():
    try:
        # Nhận dữ liệu từ request
        image_path = request.form['image_path']

        # Đường dẫn tuyệt đối hoặc tương đối đến file main.py
        main_path = os.path.join("path_to_main_directory", "main.py")

        # Gọi file main.py bằng subprocess
        process = subprocess.run(["python", main_path], input=image_path, text=True, capture_output=True)

        # Kiểm tra và trả về kết quả
        if process.returncode == 0:
            output = process.stdout.strip()  # Kết quả trả về từ file main.py
            return output
        else:
            return "Có lỗi xảy ra khi thực thi file main.py"
    except Exception as e:
        return str(e)
    
@app.route('/nen')
def nen():
    return render_template('nen.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
