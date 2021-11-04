""""
   - subprocess 怎么看阻塞
   - 结果过大会阻塞, 或者是这个命令运行时间过长,看起来阻塞但没有
   ```python

    def exec_command(cmd):
        # print(f"exec cmd [{cmd}]")
        res = subprocess.Popen(cmd, shell=True,     encoding="utf-8",
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        result, err = res.communicate(timeout=10)
        if err:
            print(f"err is [{err}]")
        # result = res.stdout.read()
        return result.strip()
    
    exec_command("grep -c 'func_stack'") # 在全局中搜索, 但使用了communicate 就不会阻塞,
   ```
   -  为什么上面使用了communicate 就不会阻塞呢? -----------------no
    ```python
    huawei@huawei-PC:~/Desktop/autotest$ python3 find_author.py kbox_result_202110201517.txt 
    /home/huawei/Desktop/autotest/log/20211020/douyin_open_004_test-20211020171500
    /home/huawei/Desktop/autotest/log/20211020/douyin_open_005_test-20211020171933
    /home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401



    # 仍然能正常运行
    huawei@huawei-PC:~/Desktop/autotest$ 

    ```
"""