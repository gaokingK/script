import base64
import string
import random
import os, re
import datetime
import sys
from pathlib import Path
# from functools import fil


def generate_random_string(length=2):
    # 包含所有数字和大小写字母的字符集
    characters = string.ascii_letters + string.digits
    # 随机选择字符并生成字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def gencode(original, encode=True):
    def _is_encode(original, encode):
        if not re.match(r'^=[A-Za-z0-9-_]*$', original):
        # if not re.match(r'^[A-Za-z0-9-_]*$', original):
            return False
        
        # 尝试解码
        try:
            _do(original, False)
        except Exception:
            return False
        return True
        
    def _do(original, encode):
        if encode:
            # 将字符串编码为字节对象（使用 UTF-8 编码）
            text_bytes = original.encode('utf-8')
            # 对字节对象进行 Base64 编码
            # encoded_bytes = base64.b64encode(text_bytes)
            encoded_bytes = base64.urlsafe_b64encode(text_bytes) #URL 和文件名安全的 Base64
            
            encoded_str = encoded_bytes.decode('utf-8').replace("=","")
            res = "=" + generate_random_string()+encoded_str
            res = res
            return res
        else:
            original = original[3:]
            if len(original) % 4 != 0:
                original += '='*(4-len(original)%4)
            decoded_bytes = base64.urlsafe_b64decode(original)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
    if encode:
        if _is_encode(original, encode):
            return original
        return _do(original, encode)
    if _is_encode(original, encode):
        return _do(original, encode)
    return original
            
    
def should_do_something(path):
    files_p = ['.py', '.sh', '.txt', '.md',".conf"]
    return any(path.lower().endswith(ext) for ext in files_p)


def confound_f(file_path, encode=True):
    threat_text = "\n"
    try:
        if encode:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            new_content = (threat_text * 100) + content + (threat_text * 100)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
        else:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()
            new_content = filter(lambda x: x != threat_text,content)
            # new_content = content[100:-99]
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_content)
    except Exception as e:
        print(e)


def rename_f(path,encode=True):
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
    if os.path.isfile(path):
        original_path = path
        dir_path = os.path.dirname(path)
        file = os.path.basename(path)
        basename = file.split(".")[0]
        suffix = ".".join(file.split(".")[1:])
        if suffix:
            new_name = gencode(basename,encode)+f".{suffix}"
        else:
            new_name = gencode(basename,encode)
        if new_name == file:
            return

        if os.path.isfile(original_path) and should_do_something(original_path):
            # print(f"Text file found: {original_path}")
            confound_f(original_path, encode)

        new_path = os.path.join(dir_path, new_name)

        os.rename(original_path, new_path)
        print(f"Renamed: '{original_path}'-> {new_name}")
        return
    # 遍历路径下的所有文件和文件夹
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.endswith("git"):
                continue
            original_path = os.path.join(root, dir)
            new_dir_name = gencode(dir, encode)
            new_path = os.path.join(root, new_dir_name)
            if new_dir_name == dir:
                continue
            if len(new_path.split("\\")) - init_depth > 7:
                continue
            if encode and len(new_dir_name) > 30:
                continue
            os.rename(original_path, new_path)
            print(f"Renamed: '{original_path}'-> {new_dir_name}")

            rename_f(os.path.join(root, new_dir_name), encode)
        for file in files:
            try:
                original_path = os.path.join(root, file)
                basename = file.split(".")[0]
                suffix = ".".join(file.split(".")[1:])
                if suffix:
                    new_name = gencode(basename,encode)+f".{suffix}"
                else:
                    new_name = gencode(basename,encode)
                if new_name == file:
                    continue
                if len(original_path.split("\\")) - init_depth > 7:
                    continue
                if encode and  len(new_name) > 40:
                    continue
                if os.path.isfile(original_path) and should_do_something(original_path):
                    # print(f"Text file found: {original_path}")
                    confound_f(original_path, encode)

                new_path = os.path.join(root, new_name)

                os.rename(original_path, new_path)
                print(f"Renamed: '{original_path}'-> {new_name}")
            except Exception as e:  
                print(f"Renamed: '{original_path}'error, break")
                raise e


if __name__ == "__main__":
    # 测试用例
    # gencode("=5pYm9zemFiYml4", encode=False)
    target_path = "E:\\Deskop\\tmp4\\python-3.8.31\\lib\\python3.8\\site-packages\\tmp"
    # target_path = "E:\\Deskop\\People\\script\\Todo\\test"
    init_depth = len(target_path.split("\\"))
    rename_f(target_path,False)
    exit()
    txt = "abcdefg"
    
    # 测试代码
    # for txt in ["abcdefg", "SHYWJjZGVmZw","bbbsss","XUYmJic3Nz",""]:
    for txt in [generate_random_string(30) for x in range(10)]:
        print(f"{txt}编码结果为{gencode(txt)}, 解码结果为{gencode(gencode(txt),encode=False)}")
        if txt != gencode(gencode(txt), encode=False):
            print("error")
        txt = gencode(txt)
        print(f"{txt}编码结果为{gencode(txt)}, 解码结果为{gencode(gencode(txt),encode=False)}")
        if txt != gencode(txt):
            print("error")
