import os.path

pass_str = """"""

online_str = """"""

import re


def format_print(case_list, prompt=""):
    _prompt = f" 该用例数一共{len(case_list)}个"
    prompt = prompt + _prompt if prompt else _prompt
    print(prompt)
    for case in case_list:
        print(case)


def file2str(file_path, start_index=None, end_index=None):
    """
    :param end_index: 到第几批结束（包括）
    :param file_path:
    :param start_index: 第几批用例(int > 0)
    :return:
    """
    file_path = os.path.abspath(file_path)
    with open(file_path, "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()
    if start_index:
        end_index = end_index + 1 if end_index else start_index + 1
        return re.findall(r"(?:# \b{}th\b.*?\n)(.*)(?:# \b{}th\b.*?\n)".format(start_index, end_index), content, re.S)[0]
    return content


def str2list(all_str: str, filter_null_line=True):
    case_list = all_str.splitlines()
    if filter_null_line:
        case_list = filter(lambda x: re.findall(r"^\w+_\w+_.*\d+\b", x, re.I), case_list)
    return list(case_list)


def get_case_result(case_list):
    v5_pass_list = list()
    v5_fail_list = list()
    v5_no_env_list = list()
    v6_pass_list = list()
    v6_fail_list = list()
    v6_no_env_list = list()
    # case_list = str2list(case_str, filter_null_line=False)

    for line in case_list:
        if line:
            if re.findall(r"V5\s*pas.*?\b", line, re.I):
                v5_pass_list.append(line.split()[0])
            elif re.findall(r"V5\s*fail.*?\b", line, re.I):
                v5_fail_list.append(line.split()[0])
            elif re.findall(r"V5\s*ev.*?\b", line, re.I):
                v5_no_env_list.append(line.split()[0])

            if re.findall(r"V6\s*pas.*?\b", line, re.I):
                v6_pass_list.append(line.split()[0])
            elif re.findall(r"V6\s*fail.*?\b", line, re.I):
                v6_fail_list.append(line.split()[0])
            elif re.findall(r"V6\s*ev.*?\b", line, re.I):
                v6_no_env_list.append(line.split()[0])

    assert len(v5_pass_list) + len(v5_fail_list) + len(v5_no_env_list) + len(v6_pass_list)\
           + len(v6_fail_list) + len(v6_no_env_list) == len(case_list) * 2

    return v5_pass_list, v5_fail_list, v5_no_env_list, v6_pass_list, v6_fail_list, v6_no_env_list


def get_pass_case(v5_pass_list, v6_pass_list):
    all_pass_case = set(v5_pass_list) & set(v6_pass_list)
    format_print(list(all_pass_case), prompt="\n\n全部通过的用例:")

    only_v5_pass = set(v5_pass_list) - set(v6_pass_list)
    format_print(list(only_v5_pass), prompt="\n\n只有V5通过的用例:")

    only_v6_pass = set(v6_pass_list) - set(v5_pass_list)
    format_print(list(only_v6_pass), prompt="\n\n只有V6通过的用例:")

    return len(all_pass_case) + len(only_v5_pass) + len(only_v6_pass)


def get_fail_list(v5_fail_list, v6_fail_list):
    all_fail_case = set(v5_fail_list) & set(v6_fail_list)
    format_print(list(all_fail_case), prompt="\n\n全部失败的用例:")

    only_v5_fail = set(v5_fail_list) - set(v6_fail_list)
    format_print(list(only_v5_fail), prompt="\n\n只有V5失败的用例:")

    only_v6_fail = set(v6_fail_list) - set(v5_fail_list)
    format_print(list(only_v6_fail), prompt="\n\n只有V6失败的用例:")
    

def get_no_env_list(v5_no_env_list, v6_no_env_list):
    """只用获取 都没有环境的用例"""
    all_no_env_case = set(v5_no_env_list) & set(v6_no_env_list)
    format_print(list(all_no_env_case), prompt="\n\n全部没有环境的用例:")

    return len(all_no_env_case)


def case_outlook(case_list):
    """
    输出成功（成功和部分成功）、失败（全部失败）、没有环境（全部没有环境）、一个失败一个没有环境 的用例
    :return: 
    """
    v5_pass_list, v5_fail_list, v5_no_env_list, v6_pass_list, v6_fail_list, v6_no_env_list = get_case_result(case_list)

    pass_count = get_pass_case(v5_pass_list, v6_pass_list)

    all_fail_case = set(v5_fail_list) & set(v6_fail_list)
    format_print(list(all_fail_case), prompt="\n\n全部失败的用例:")
    fail_count = len(all_fail_case)

    no_env_count = get_no_env_list(v5_no_env_list, v6_no_env_list)

    # V5失败V6没有环境
    v5_fail_v6_no_env = set(v5_fail_list) & set(v6_no_env_list)
    format_print(list(v5_fail_v6_no_env), prompt="\n\nV5失败V6没有环境的用例:")
    fail_count += len(v5_fail_v6_no_env)

    # V6失败但是V5没有环境
    v6_fail_v5_no_env = set(v6_fail_list) & set(v5_no_env_list)
    format_print(list(v6_fail_v5_no_env), prompt="\n\nV6失败V5没有环境的用例:")
    fail_count += len(v6_fail_v5_no_env)

    assert len(case_list) == pass_count + fail_count + no_env_count


def find_toline_case(pass_str, online_str):
    """输出需要上线的用例"""
    case_list = str2list(pass_str)
    online_list = str2list(online_str)
    v5_pass_list, v5_fail_list, v5_no_env_list, v6_pass_list, v6_fail_list, v6_no_env_list = get_case_result(case_list)

    pass_set = set(v5_pass_list) | set(v6_pass_list)
    online_set = set(online_list)

    format_print(list(pass_set - online_set), prompt="\n\n需要上线的用例:")
    format_print(list(online_set - pass_set), prompt="\n\n上线过却没成功的用例:")


def sync_case_result():
    """
    有一批任务，我们两个人分头搞，但是我在最开始时把用例排序了一下，后面我们对的时候就很难对，所以要把排序后的用例结果对应到未排序的用例上去
    :return:
    """
    sorted_str = """"""
    origin_str = """"""
    origin_list = origin_str.splitlines()
    for index in range(len(origin_list)):
        if re.findall(r"%s.*" % (origin_list[index]), sorted_str):
            origin_list[index] = re.findall(r"%s.*" % (origin_list[index]), sorted_str)[0]

    for case in origin_list:
        print(case)


def filter_case():
    all_case = """"""
    old_case = """"""
    all_set = set(all_case.splitlines())
    old_case = set([case.split()[0] for case in old_case.splitlines()])
    print("ok")

if __name__ == '__main__':
    # case_str = file2str(r"../tran/case_result.md")
    # case_list = str2list(case_str)
    # v5_pass_list, v5_fail_list, v5_no_env_list, v6_pass_list, v6_fail_list, v6_no_env_list = get_case_result(case_list)
    # get_pass_case(v5_pass_list, v6_pass_list)
    # get_fail_list(v5_fail_list, v6_fail_list)
    # get_no_env_list(v5_no_env_list, v6_no_env_list)
    # case_outlook(case_list)

    # 从文件读取通过的用例，和已上线的用例进行比较
    # pass_str = file2str(r"../tran/case_result.md")
    # online_str = file2str(r"../tran/蒋金伟_用例上线_all.txt")
    # find_toline_case(pass_str, online_str)

    # sync_case_result()
    filter_case()