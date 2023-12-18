from PIL import Image
import pytesseract
import os
import sys

def recognize_text(image_path, tesseract_path):
    try:
        # 設定 Tesseract 文件夾的路徑
        if getattr(sys, 'frozen', False):
            # PyInstaller 打包後的情況
            tesseract_path = os.path.join(sys._MEIPASS, "tesseract_files")
        else:
            # 正常運行模式下的情況
            tesseract_path = "tesseract_files"  # 非打包模式下，確保該文件夾在當前工作目錄中或指定完整路徑

        # 設定 Tesseract 的路徑
        pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, "tesseract.exe")

        # 打開圖片
        image = Image.open(image_path)

        text = pytesseract.image_to_string(image, lang='eng')
        print(text)
        # 打印辨識的文字
        # print("辨識結果:")
        # print(text)

    except Exception as e:
        print(f"發生錯誤: {e}")

# 替換成您的圖片路徑和 Tesseract 的路徑
image_path = "123.png"
tesseract_path = r"C:\Users\diowang\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
recognize_text(image_path, tesseract_path)
