"""
比较kbox_result和本地用例，找出两边各自的补集
"""
import os
import re
import subprocess
"""
通过stdin 输入命令要加\n
提示输入密码 属于err， 这是stdout.read()/会阻塞
"""
import time


def get_exec_mac_testcase(author="jwx5319396"):
    """
    把111、112、113、114上的用例中属于author的用例生成一个set
    :return:
    """
    # 手动设置kbox_result文件的路径
    kbox_result_file_paths = [os.path.join("/home/huawei/Desktop/", (str(x) + "*.txt")) for x in range(111, 115)]
    cmd = f"cat {' '.join(kbox_result_file_paths)}"
    res = subprocess.Popen(cmd, shell=True, encoding="utf-8", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 首次输入 和后续输入？
    test_case_names = res.stdout.read()
    exec_mac_testcase = re.findall(r".*/(.*.py)\s.*", test_case_names)
    res.stdin.write("echo 'aa'")  # 这个是相当于向cat 这个命令中输入， 所以没有用 如果那是命令是python 这就会有用
    print(res.stdout.read(), res.stderr.read())
    return exec_mac_testcase


def get_local_testcase():
    # 是用bin/sh 作为解释器，pcbox无用
    cmd = f"find /home/huawei/Desktop/people/pc_kbox -regextype posix-extended -regex '.*[[:digit:]]_test.py'"
    res = subprocess.Popen(cmd, shell=True, encoding="utf-8", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    test_case_names = res.stdout.read()
    local_testcase = re.findall(r".*/(.*.py)", test_case_names)
    return local_testcase


def find_author_by_linux(file_path):
    """linux commond"""
    with open(file_path, "r+") as f:
        content = f.read()
        test_cases = re.findall(r".*.py", content)
        for case_name in test_cases:
            cmd = f"find /home/huawei/Desktop/people/pc_kbox -name {case_name} -exec grep  -P 'author' {{}} \;"
            # cmd = f"find /home/huawei/Desktop/people/pc_kbox -name {case_name} -exec grep -exec grep -P 'author' {{}} \;"
            res = subprocess.Popen(cmd, shell=True, encoding="utf-8",
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            author = res.stdout.read()
            author = author.split()[1] if author else "not find"
            content = content.replace(case_name, f"{case_name}   {author}")
        f.seek(0)
        f.write(content)


def main(result_file_path):
    exec_mac_testcase = get_exec_mac_testcase()
    local_testcase = get_local_testcase()
    exec_mac_testcase_set = set(exec_mac_testcase)
    local_testcase_set = set(local_testcase)
    with open(result_file_path, "w") as f:
        f.write(f"执行机用例数量：list为{len(exec_mac_testcase)}, set为{len(exec_mac_testcase_set)}\n")
        f.write(f"本地用例数量：list为{len(local_testcase)}, set为{len(local_testcase_set)}\n\n\n")

        f.write("在执行机存在而本地不存在的用例：\n")
        contents = list(map(lambda x: str(x) + "\n",  exec_mac_testcase_set - local_testcase_set))
        f.writelines(contents)

        f.write("\n\n在本地存在而执行机不存在的用例：\n")
        contents = list(map(lambda x: str(x) + "\n", local_testcase_set - exec_mac_testcase_set))
        f.writelines(contents)
    find_author_by_linux(result_file_path)


if __name__ == '__main__':
    start_time = time.process_time()
    result_file_path = "/home/huawei/Desktop/diff_res.txt"
    main(result_file_path)

    print(f"cost {time.process_time() - start_time}s")
