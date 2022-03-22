import base64
image_path = r"C:\Users\jwx5319396\Desktop\20220302-154543.png"
with open(image_path, "rb") as f:
    base_64 = base64.b64encode(f.read())
    print(base_64)