# def binary_to_png(file_path, output_file):
#     with open(file_path, 'r') as file:
#         binary_data = file.read()

#     with open(output_file, 'wb') as file:
#         file.write(eval(binary_data))

def binary_to_png(file_path, output_file):
    with open(file_path, 'r') as file:
        binary_data = file.read()

    # 刪除 "#" 符號到第一個 "\" 符號之間的內容
    start_index = binary_data.index("#")
    end_index = binary_data.index("\\")
    cleaned_data = binary_data[:start_index] + binary_data[end_index:]

    # 覆蓋原始文字檔內容
    with open(file_path, 'w') as file:
        file.write(cleaned_data)

    with open(output_file, 'wb') as file:
        file.write(eval(cleaned_data))



# 範例使用
# file_path = 'png_test.txt'
file_path = 'binary_data.txt'
output_file = '0606.png'
binary_to_png(file_path, output_file)

##########binary_data