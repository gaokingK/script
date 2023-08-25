"""
TO: 使用ddddocr 识别验证码
doc：https://github.com/sml2h3/ddddocr
"""
from flask import Flask
from flask import request
import ddddocr
import json


app = Flask(__name__)
ocr = ddddocr.DdddOcr()
from PIL import Image

@app.route("/", methods=["POST"])
def parse_img():
    # file = request.files["img"]
    # image = Image.open(file.stream)
    # res = ocr.classification(image)

    # with open("./test.png", 'rb') as f:
    #     image = f.read()
    # res = ocr.classification(image)

    img_base64 = request.json["file"]
    res = ocr.classification(img_base64)

    return json.dumps({"code": res})


if __name__ == '__main__':
    app.run(debug=True)
