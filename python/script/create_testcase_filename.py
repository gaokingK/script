name_dict = {"dd": "dingding_function_0_test.py",
             "wx": "weixin_function_0_test.py",
             "wxpay": "weixin_payfunction_0_test.py",
             "wxexec": "weixin_exception_0_test",
             "aqy": "aiqiyi_function_0_test.py",
             "qywx": "qiyeweixin_function_0_test.py",
             "txhy": "tengxunhuiyi_function_0_test.py",
             "ths": "tonghuashun_function_0_test.py",
             "xxqg": "xuexiqiangguo_function_0_test.py",
             "mt": "meituan_function_0_test.py",
             "tb": "taobao_function_0_test.py",
             "txsp": "tengxunshipin_hd_function_0_test.py",
             }


def product(app_name, num_list):
    testcase_list = []
    testcase_name = name_dict[app_name]
    testcase_name_l = testcase_name.split("0")[0]
    testcase_name_r = testcase_name.split("0")[1]
    for i in num_list:
        i = '0' + str(i) if len(str(i)) == 1 else str(i)
        testcase_list.append("top_n/high_quality/" + testcase_name.split("_")[
            0] + "/function/" + testcase_name_l + '0' + i + testcase_name_r)
    print('\n' * 3)
    for item in testcase_list:
        print(item)
    print('\n' * 3)


def product_2(name, list):
    # 产生用于代码统计的用例目录
    for i in list:
        i = '0' + str(i) if len(str(i)) == 1 else str(i)
        com_name = "tests/topn/{0}/function/{0}_function_common_0{1}.py".format(
            name, i)
        print(com_name)
    for i in list:
        i = '0' + str(i) if len(str(i)) == 1 else str(i)
        test_name = "tests/topn/{0}/function/release_1/{0}_function_0{1}_test.py".format(
            name, i)
        print(test_name)


if __name__ == "__main__":
    num_list = [42, 41]
    # product_2('meituan', num_list)
    # product_2('taobao', [35, 36])
    # product_2('tengxunshipin', [33, 34, 4])
    # product_2('tengxunhuiyi', [40])
    # product_2('tonghuashun', [16, 17])
    # product("dd", [1, 2, 4, 5, 6, 7, 9, 10, 12, 13, 14, 17, 18, 21, 22])
    # product("mt", [1])
    # product("txhy", [1, 2, 3, 6, 7, 8])
    # product("txsp", [1, 2, 3, 4, 5, 6, 8])
    # product("ths", [1, 2, 3, 4, 5, 6, 7, 11, 12])
    product("wx", [2, 3, 4, 6, 7, 9, 13])
