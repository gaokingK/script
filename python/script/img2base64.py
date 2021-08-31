import base64
file_path = r"C:\Users\jwx5319396\Desktop\112112.png"
with open(file_path, "rb") as f:#转为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)

