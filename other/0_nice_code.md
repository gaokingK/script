# 好的代码
1. ##### 关键的日志最好有标识
```python
    print(script_log_path) 
    print(f"get path is: [{script_log_path}])
    # 否则日志中的这种情况就会puzzle
huawei@huawei-PC:~/Desktop/autotest$ python3 find_author.py kbox_result_202110201517.txt 
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_004_test-20211020152149
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_005_test-20211020152423
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_006_test-20211020152602
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_004_test-20211020155833
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_005_test-20211020160110
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_006_test-20211020160409
/home/huawei/Desktop/autotest/log/20211020/dingding_open_004_test-20211020164144
/home/huawei/Desktop/autotest/log/20211020/dingding_open_005_test-20211020164422
/home/huawei/Desktop/autotest/log/20211020/dingding_open_006_test-20211020164643
/home/huawei/Desktop/autotest/log/20211020/douban_open_004_test-20211020170055
/home/huawei/Desktop/autotest/log/20211020/douban_open_005_test-20211020170226
/home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405
/home/huawei/Desktop/autotest/log/20211020/douyin_open_004_test-20211020171500
/home/huawei/Desktop/autotest/log/20211020/douyin_open_005_test-20211020171933
/home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401



# 上面的几行就会迷惑, 而实际是log_path是空
huawei@huawei-PC:~/Desktop/autotest$ 
# 调试这个错误时, 应该直接把命令打出来
```