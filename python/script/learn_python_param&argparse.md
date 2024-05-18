# TO: argparse模块和python 函数参数的一些
## 函数参数
```py
# 传参
class A:
    def __init__(self, ip, passwd=None):
        self.ip = ip
        self.passwd = passwd
        self.use_parm(self.ip, self.passwd)

    def use_parm(self, ip, passwd):
        if not ip:
            print("no ip parm")
        else:
            print(ip, passwd)


if __name__ == '__main__':
    a = A(4, passwd=5)
```
## argparse
### link: 
- https://blog.csdn.net/Monster_H7/article/details/110823453
### hello_world
```py
# 创建解析器
parser = argparse.ArgumentParser(description='Process some integers.')
# 添加参数
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# 解析参数
parser.parse_args(['--sum', '7', '-1', '42'])
```
### 参数
- 
```
```
