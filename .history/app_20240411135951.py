# Nhập các thư viện cần thiết
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Đường dẫn đến hình ảnh (đảm bảo bạn đã thay đổi đường dẫn này thành một hình ảnh thích hợp trên máy tính của bạn)
image_path = 'path_to_your_image.jpg'

# Đọc hình ảnh
image = io.imread(image_path)

# Trích xuất các kênh màu từ hình ảnh
red = image[:, :, 0]
nir = image[:, :, 3]

# Chuyển đổi sang kiểu dữ liệu float để tính toán NDVI
red = red.astype(float)
nir = nir.astype(float)

# Tính toán chỉ số NDVI
ndvi = (nir - red) / (nir + red)

# Hiển thị hình ảnh NDVI
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('Normalized Difference Vegetation Index (NDVI)')
plt.show()
