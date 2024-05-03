import file_handling
import huffman_coding
import os

def tach_ten_file(path):
    ten_file = os.path.basename(path) # Lấy tên file từ đường dẫn
    ten_file_khong_mo_rong = os.path.splitext(ten_file)[0] # Tách tên file không kèm phần mở rộng
    return ten_file_khong_mo_rong

image_path = input("Image Path: ")  # inputs/test.tif
fname = tach_ten_file(image_path)

image_bit_string = file_handling.read_image_bit_string(image_path)
compressed_image_bit_string = huffman_coding.compress(image_bit_string, fname)
file_handling.write_image(compressed_image_bit_string, "Outputs/compressed_" + fname + ".bin")
print("Compression Ratio (CR):", (1 - len(compressed_image_bit_string) / len(image_bit_string)) * 100, "%")

decompressed_image_bit_string = huffman_coding.decompress(compressed_image_bit_string)
file_handling.write_image(decompressed_image_bit_string,"Outputs/decompressed_" + fname + ".jpg")
