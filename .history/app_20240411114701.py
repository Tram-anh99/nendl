from flask import Flask, jsonify
import ee
import geemap
import os

app = Flask(__name__)

# Kết nối đến Earth Engine
ee.Initialize()

# Chức năng xử lý dữ liệu và xuất dữ liệu LST dưới dạng GeoTIFF
def process_data_and_export():
    # Code xử lý dữ liệu và xuất dữ liệu LST tại đây
    # Bạn có thể sao chép mã từ ứng dụng hiện tại vào đây

    # Lấy đối tượng AOI
    aoi = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2") \
            .filter(ee.Filter.eq('ADM1_NAME', 'Ho Chi Minh City'))

    # Tính toán nhiệt độ bề mặt đất (LST)
    lst = ...  # Code tính toán LST từ ứng dụng hiện tại

    # Xác định phạm vi cho việc xuất dữ liệu
    hcm_region = aoi.geometry().bounds()

    # Xuất dữ liệu LST dưới dạng tệp GeoTIFF
    out_dir = '/content/'
    out_file = os.path.join(out_dir, 'lst_hcm.tif')
    geemap.ee_export_image(lst, filename=out_file, scale=140, region=hcm_region)

# Định nghĩa endpoint cho API
@app.route('/export_lst', methods=['GET'])
def export_lst():
    # Gọi hàm xử lý dữ liệu và xuất dữ liệu LST
    process_data_and_export()
    return jsonify({'message': 'Exporting LST data in progress...'})

if __name__ == '__main__':
    app.run(debug=True)
