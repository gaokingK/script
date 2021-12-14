"""
处理kbox_result 在用例后加上姓名
python3 find_author.py kbox_result_xxx.txt

f.read([1000]) 返回1000字节的字符串
f.readlines(1000) 从0开始读, 读1000个字节, 以行为元素返回一个列表
f.readline(1000) 返回当前行, 如果该行大于1000 只显示前1000个字节
f.writelines(collection) 要把换行符写在集合中
f.write()会从文件最后追加内容, 如果seek(0)过, 那个相当于是把前size个字节给覆盖了, 不能直接插入
f.tell() 不能用在next调用的文件对象中, 即不能在for line in f_obj: 中

r+: 原文件长度100, seek(0), 写入99, 则文件长度还为100, 包括新写入的99和原来的1
link: https://www.runoob.com/python/python-files-io.html
truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。
如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。(可以在r+模式下把覆盖不了的删除)
"""
import os
import re
import subprocess
import datetime
from functools import reduce

import sys

all_count = 0


def exec_command(cmd):
    # print(f"exec cmd [{cmd}]")
    res = subprocess.Popen(cmd, shell=True, encoding="utf-8",
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result, err = res.communicate(timeout=10)
    if err:
        print(f"err is [{err}]")
    # result = res.stdout.read()
    return result.strip()


def recover_file(file_name):
    file_name = os.path.abspath(file_name)
    new_result = []
    with open(file_name, "r+") as f:
        for line in f:
            if len(line.strip().split(" ")) > 2:
                new_result.append(" ".join(line.split(" ")[:2]) + "\n")
            else:
                new_result.append(line.strip() + "\n")
        f.seek(0)
        f.writelines(new_result)
        f.truncate()


def find_author(kbox_result_file_path, testcase_run_date):
    new_result = []
    with open(kbox_result_file_path, "r+") as f:
        for line in f:
            if len(line.split()) > 2:
                continue
            testcase_name = line.split()[0]
            # testcase_path = os.path.join(
                # "/home/huawei/Desktop/people/pc_kbox/pc_kbox/tests", script_name)
            testcase_path = os.path.join(
                "/home/huawei/Desktop/autotest/pc_kbox/tests", testcase_name)

            if not (os.path.exists(testcase_path) and os.path.isfile(testcase_path)):
                new_result.append(f"{' '.join(line.split())} file not exist" + "\n")
                continue
            with open(testcase_path) as testcase:
                res = re.findall(r"author:\s*(.*)", testcase.read(), flags=re.I)
                author = res[0] if res else ""
                exception_handler_res = ""
                if author == "jwx5319396":
                    exception_handler_res = get_exception_handler_effect(kbox_result_file_path, testcase_name, testcase_run_date)
                new_result.append(f"{' '.join(line.split())} {author} {exception_handler_res}" + "\n")
        f.seek(0)
        f.writelines(new_result)


def get_exception_handler_effect(kbox_result_file_path, testcase_name, testcase_run_date):
    """分析这个用例的日志,  返回弹窗的执行次数"""
    testcase_name = testcase_name.split("/")[-1].split(".py")[0]
    script_log_path = get_script_log_path(kbox_result_file_path, testcase_run_date, testcase_name)

    print(f"log_path is:[{script_log_path}]")
    count = 0
    if script_log_path:
        cmd = f"grep -c \"func_stack\" {script_log_path}"
        count = exec_command(cmd)

        count = count.strip().split()[0][-1] if count else 0
        count = int(int(count)/2)
        global all_count
        all_count += count
    return f" 清除弹窗运行了{count}次" if int(count) > 0 else " 未运行"


def get_script_log_path(kbox_result_file_path, testcase_run_date, testcase_name):
    """获取用例log的正确路径, 一个用例一天可能跑几次"""
    script_log_path = os.path.join("/home/huawei/Desktop/autotest/log/", testcase_run_date)


    current_period_run_start = kbox_result_file_path.split("/")[-1].split("_")[-1].split(".")[0]
    kbox_result_file_pattern = "kbox_result_" + testcase_run_date + "*"
    cmd = f"find /home/huawei/Desktop/autotest -name '{kbox_result_file_pattern}'|sort"
    kbox_result_files = exec_command(cmd)
    kbox_result_files = kbox_result_files.split("\n")
    kbox_result_file_dates = list(map(lambda x: x.split("/")[-1].split("_")[-1].split(".")[0], kbox_result_files))
    if not current_period_run_start in kbox_result_file_dates:
        print(kbox_result_file_path, testcase_name)
        assert False

    start_date = datetime.datetime.strptime(current_period_run_start,"%Y%m%d%H%M")
    if len(kbox_result_file_dates) > 1:
        if kbox_result_file_dates[-1] != current_period_run_start:
            index = kbox_result_file_dates.index(current_period_run_start)
            older_date = kbox_result_file_dates[index+1]
            older_date = datetime.datetime.strptime(older_date, "%Y%m%d%H%M")
            cmd = f"find {script_log_path} -newermt '{start_date}' ! -newermt '{older_date}' -name {testcase_name + '-*'}"
    else:
        cmd = f"find {script_log_path} -newermt '{start_date}' -name {testcase_name + '-*'}"
    log_path = exec_command(cmd)
    return log_path


def main(kbox_result_file_path, full_log):
    kbox_result_file_path = os.path.abspath(kbox_result_file_path)
    testcase_run_date = kbox_result_file_path.split("_")[2][:8]
    log_path = "/home/huawei/Desktop/autotest/exception_res.log"

    cmd = "[ ! -e ${log_path:=/home/huawei/Desktop/autotest/exception_res.log} ] && touch ${log_path}"
    exec_command(cmd)

    find_author(kbox_result_file_path, testcase_run_date)

    cmd = f"grep -ic True.*396.*次 {kbox_result_file_path}"
    success_count = exec_command(cmd)
    success_count = int(success_count) if success_count else 0
    cmd = f"grep -ic false.*396.*次 {kbox_result_file_path}"
    fail_count = exec_command(cmd)
    fail_count = int(fail_count) if fail_count else 0

    if fail_count > 0:
        cmd = f"grep -i false.*396.*次 {kbox_result_file_path}|awk -F '[了次]' '{{print $(NF-1)}}' "
        fail_all_count = exec_command(cmd)
        fail_all_count = reduce(lambda a,b: int(a)+int(b), fail_all_count.split("\n"))
    else:
        fail_all_count = 0

    if success_count > 0:
        cmd = f"grep -i true.*396.*次 {kbox_result_file_path}|awk -F '[了次]' '{{print $(NF-1)}}' "
        success_all_count = exec_command(cmd)
        success_all_count = reduce(lambda a,b: int(a)+int(b), success_all_count.split("\n"))
    else:
        success_all_count = 0

    info = f"""
    {testcase_run_date} exception_exec_result:
        在{success_count + fail_count}个用例中运行{all_count}次, 在{success_count}个成功的用例中运行了{success_all_count}次, 在{fail_count}个失败的用例中运行了{fail_all_count}次
    """
    cmd = f"echo '{info}' >> {log_path}"
    exec_command(cmd)
    if full_log:
        cmd = f"grep \"jwx5319396\" {kbox_result_file_path} >> {log_path}"
        exec_command(cmd)


if __name__ == '__main__':
    # main("kbox_result_202110280318.txt")
    # exec_command("sleep 50")
    full_log = True if len(sys.argv) == 3 else False
    recover_file(sys.argv[1])
    main(sys.argv[1], full_log)
