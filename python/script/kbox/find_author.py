"""
处理kbox_result 在用例后加上姓名
python3 find_author.py kbox_result_xxx.txt

f.read(1000) 返回1000字节的字符串
f.readlines(1000) 从0开始读, 读1000个字节, 以行为元素返回一个列表
f.readline(1000) 返回当前行, 如果该行大于1000 只显示前1000个字节
f.writelines(collection) 要把换行符写在集合中
f.write()会从文件最后追加内容, 如果seek(0)过, 那个相当于是把前size个字节给覆盖了, 不能直接插入
f.tell() 不能用在next调用的文件对象中, 即不能在for line in f_obj: 中
link: https://www.runoob.com/python/python-files-io.html
"""
import os
import re


def main(file_name):
    file_name = os.path.abspath(file_name)
    new_result = []
    with open(file_name, "r+") as f:
        for line in f:
            if len(line.split()) > 2:
                continue
            testcase_path = os.path.join(
                "/home/huawei/Desktop/people/pc_kbox/pc_kbox/tests", line.split()[0])

            if not (os.path.exists(testcase_path) and os.path.isfile(testcase_path)):
                new_result.append(f"{' '.join(line.split())} file not exist" + "\n")
                continue
            with open(testcase_path) as testcase:
                res = re.findall(r"author:\s*(.*)", testcase.read(), flags=re.I)
                author = res[0] if res else ""
                new_result.append(f"{' '.join(line.split())} {author}" + "\n")
        f.seek(0)
        f.writelines(new_result)


if __name__ == '__main__':
    main("t.txt")
