from flask import Flask, jsonify

app = Flask(__name__)

# Đường dẫn kiểm tra xem một năm có phải là năm nhuận không
@app.route('/nam-nhuan/<int:nam>', methods=['GET'])
def kiem_tra_nam_nhuan(nam):
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        return jsonify({'nam': nam, 'nam_nhuan': True})
    else:
        return jsonify({'nam': nam, 'nam_nhuan': False})

if __name__ == '__main__':
    app.run(debug=True)
