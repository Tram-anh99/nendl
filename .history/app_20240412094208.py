from flask import Flask, render_template, request

app = Flask(__name__)

# Route để hiển thị form nhập giá trị a và b
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
