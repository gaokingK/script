## counter类
- link: https://www.cnblogs.com/zhenwei66/p/6593395.html
- 计算值出现的次数, 并能做一些运算

## string 字符串的一些方法
- test_str = "she is a dog"
- endwith 以什么结尾 `test_str.endwith("dog")`

### python 函数中显示声明参数类型也不能强制转换
```
def func(b: int):
    print(b)
func("b") # 照样可以正常运行

```
### 字典生成式
- link: https://www.cnblogs.com/wxj1129549016/p/9515721.html
```
dict(zip('abc', [1, 2, 3]))
dic = {i:2*i for i in range(3)} # {0: 0, 1: 2, 2: 4}
```

## formate 的罕见用法
```
Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
```

## 集合和集合的运算
- link：https://blog.csdn.net/isoleo/article/details/13000975
```
# 交集
a & b
# 并集
a | b
# 差
a - b # {1, 2} - {1, 3} 结果是2
```
