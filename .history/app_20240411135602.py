from flask import Flask, jsonify
from geni import calculate_ndvi

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Earth Engine API with Flask!'

@app.route('/ndvi/<aoi>')
def ndvi_route(aoi):
    ndvi_result = calculate_ndvi(aoi)
    return jsonify({'result': ndvi_result})

if __name__ == '__main__':
    app.run(debug=True)
