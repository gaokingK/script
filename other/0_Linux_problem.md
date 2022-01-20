### pt 这个命令为什么不能留在命令历史中?-----------no
### pactl list short sinks ; arecord -------no
### 挂载相关
### 为什么这个后面的一个在文件中找不到
### 验证用户
### 为什么zsh 的read -p 不能用?
```shell
# 原来一个是抖音,一个是豆瓣 艹
/home/huawei/Desktop/autotest/log/20211020/douban_open_004_test-20211020170055
/home/huawei/Desktop/autotest/log/20211020/douban_open_005_test-20211020170226
/home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405 ls 这个 就能find这个
/home/huawei/Desktop/autotest/log/20211020/douyin_open_004_test-20211020171500
/home/huawei/Desktop/autotest/log/20211020/douyin_open_005_test-20211020171933
/home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401 ls 这个, 就能find这个
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401
-rw-r--r-- 1 huawei huawei 49852 10月 20 17:28 /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401                                                                                                                 
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405
-rw-r--r-- 1 huawei huawei 33233 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405                                                                                                                 
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douban_open_006_*
-rw-r--r-- 1 huawei huawei 33233 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405                                                                                                                 
-rw-r--r-- 1 huawei huawei 87648 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test.html
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401
-rw-r--r-- 1 huawei huawei 49852 10月 20 17:28 /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401                                                                                                                 
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douban_open_006_*-rw-r--r-- 1 huawei huawei 33233 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405                                                                                                                 
-rw-r--r-- 1 huawei huawei 87648 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test.html
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405
-rw-r--r-- 1 huawei huawei 33233 10月 20 17:05 /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405                                                                                                                 
huawei@huawei-PC:~/Desktop/autotest$ grep "func_stack" /home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405
huawei@huawei-PC:~/Desktop/autotest$ grep "func_stack" /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401
2021-10-20 17:26:24,194 - exception_handler.py,65 - INFO - click_by_id([(), {'button_text': '搜索按钮', 'resource_id': 'com.ss.android.ugc.aweme:id/c94'}])出错,  func_stack:[['click_by_id']](281473094185288)
2021-10-20 17:26:24,194 - exception_handler.py,37 - INFO - func_stack[['click_by_id', 'click_by_id']]
huawei@huawei-PC:~/Desktop/autotest$ ls -la /home/huawei/Desktop/autotest/log/20211020/douban_open_006_*^C
huawei@huawei-PC:~/Desktop/autotest$
   ```