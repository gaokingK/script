# from paddleocr import PaddleOCR
import easyocr


def use_easyocr(file_path):
    reader = easyocr.Reader(['en', 'ch_sim'])  # 支持中英文
    result = reader.readtext(file_path)
    for box in result:
        print(box[1])  # 打印识别出的文字


def use_paddleocr(file_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='ch') 
    result = ocr.ocr(file_path, cls=True)
    for line in result:
        for word in line:
            print(word[1][0])  # 输出文字内容


if __name__ == "__main__":
    file_path = "C:\\Users\\d1806\\Pictures\\20250416150251.jpg"
    # use_paddleocr(file_path)
    use_easyocr(file_path)


