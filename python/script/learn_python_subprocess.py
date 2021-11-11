#!/usr/bin/python3
"""
- subprocess的参数
    https://www.cnblogs.com/zhoug2020/p/5079407.html
- 一些知识:
    可以p.poll() 获取命令运行后的状态 0: 成功; 1 超时; 2 失败 #noqa
- 问题:
    Python的问题解决: IOError: [Errno 32] Broken pipe: https://www.cnblogs.com/icejoywoo/p/3908290.html
- communicate()和wait()区别
    - 使用 subprocess 模块的 Popen 调用外部程序，如果 stdout 或 stderr 参数是 pipe，并且程序输出超过操作系统的 pipe size时，
    如果使用 Popen.wait() 方式等待程序结束获取返回值，会导致死锁，程序卡在 wait() 调用上
    -  Popen.communicate()。这个方法会把输出放在内存，而不是管道里，所以这时候上限就和内存大小有关了，一般不会有问题。
    而且如果要获得程序返回值，可以在调用 Popen.communicate() 之后取 Popen.returncode 的值。
- subprocess 怎么看阻塞
- 调用之后直接阻塞到子程序调用结束?
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
import logging
import subprocess
logger = logging.getLogger()


def exec_cmd(cmd, timeout=10):
    logger.info(f"cmd: [{cmd}]")
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding="utf-8")
    stdout, stderr = p.communicate(timeout=timeout)
    status = p.poll()
    status = p.returncode
    return stdout.strip(), stderr.strip()


if __name__ == '__main__':
    cmd = "grep 'func_stack' -r ./"
    exec_cmd(cmd)
