from flask import Flask, render_template, request
from dtcn import dientich_chunhat
from gee_v1 import nhietdo

app = Flask(__name__)

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
        start_date = float(request.form['startDate'])
        end_date = float(request.form['endDate'])
        area = nhietdo(start_date, end_date)
        return render_template('dtcn.html', area=area)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
