from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/custom_endpoint', methods=['GET'])
def custom_endpoint():
    # Xử lý yêu cầu ở đây
    return jsonify({'data': 'Some data'})

if __name__ == '__main__':
    app.run(debug=True)  # Chạy ứng dụng Flask với chế độ debug bật
