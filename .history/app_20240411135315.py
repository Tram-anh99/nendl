# from flask import Flask, jsonify
# import ee
# import geemap
# import os
# app = Flask(__name__)

# # Đường dẫn kiểm tra xem một năm có phải là năm nhuận không
# @app.route('/nam-nhuan/<int:nam>', methods=['GET'])
# def kiem_tra_nam_nhuan(nam):
#     if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
#         return jsonify({'nam': nam, 'nam_nhuan': True})
#     else:
#         return jsonify({'nam': nam, 'nam_nhuan': False})

# if __name__ == '__main__':
#     app.run(debug=True)
#   ====================  
    
from flask import Flask, jsonify
import ee
import geemap
import os

app = Flask(__name__)

# Khởi tạo Earth Engine
# ee.Initialize()

# # Tạo một đối tượng Map từ geemap
# m = geemap.Map()

# @app.route('/')
# def index():
#     return 'Welcome to the Earth Engine API with Flask!'

# @app.route('/ndvi/<aoi>')
# def calculate_ndvi(aoi):
#     # Xử lý tính toán NDVI và trả về kết quả
#     return jsonify({'result': 'NDVI calculated for ' + aoi})

# @app.route('/map')
# def show_map():
#     # Hiển thị bản đồ được tạo từ geemap
#     return m.to_html()

if __name__ == '__main__':
    app.run(debug=True)
    

# ===================
# app = Flask(__name__)

# # Kết nối đến Earth Engine
# ee.Initialize()

# # Chức năng xử lý dữ liệu và xuất dữ liệu LST dưới dạng GeoTIFF
# def process_data_and_export():
#     # Code xử lý dữ liệu và xuất dữ liệu LST tại đây
#     # Bạn có thể sao chép mã từ ứng dụng hiện tại vào đây

#     # Lấy đối tượng AOI
#     aoi = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level2") \
#             .filter(ee.Filter.eq('ADM1_NAME', 'Ho Chi Minh City'))

#     # Tính toán nhiệt độ bề mặt đất (LST)
#     lst = ...  # Code tính toán LST từ ứng dụng hiện tại

#     # Xác định phạm vi cho việc xuất dữ liệu
#     hcm_region = aoi.geometry().bounds()

#     # Xuất dữ liệu LST dưới dạng tệp GeoTIFF
#     out_dir = '/content/'
#     out_file = os.path.join(out_dir, 'lst_hcm.tif')
#     geemap.ee_export_image(lst, filename=out_file, scale=140, region=hcm_region)

# # Định nghĩa endpoint cho API
# @app.route('/export_lst', methods=['GET'])
# def export_lst():
#     # Gọi hàm xử lý dữ liệu và xuất dữ liệu LST
#     process_data_and_export()
#     return jsonify({'message': 'Exporting LST data in progress...'})

# if __name__ == '__main__':
#     app.run(debug=True)
