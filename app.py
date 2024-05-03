import ee
import geemap # type: ignore
import os

from flask import Flask, render_template, request
from dtcn import dientich_chunhat
import gee_v1
# from code.lossless import main

app = Flask(__name__)

ee.Initialize()
aoi = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2") \
        .filter(ee.Filter.eq('ADM1_NAME', 'Ho Chi Minh City'))

# Route để hiển thị form nhập giá trị a và b
@app.route('/home')
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

@app.route('/nen', methods=['GET', 'POST'])
def tach_ten_file():
    if request.method == 'POST':
        year = float(request.form['year'])
        kq = gee_v1.nhietdo(year)
        return render_template('index.html', year=year, kq=kq)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
