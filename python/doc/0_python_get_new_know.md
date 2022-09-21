### 逻辑运算符的优先级问题
- if "V6" or "V7" in self.productname
    - 会先计算or
### mmap --- 内存映射文件支持
- 打开已加载到内存中的对象
### pprint.pformat(value)
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
### 有序字典 orderdict
- link:https://blog.csdn.net/weixin_42307036/article/details/99294242
- 普通字典的键是排序的，不是按插入的顺序；而有序字典的键是按插入的先后顺序排列的，即使修改键对应的值不能改变它的顺序
- 普通的dict的其中一个区别是 dict.popitem() 会移除最后一个键值对，并返回键值对，不能移除第一个键值对；OrderedDict的popItem()方法可以移除第一个键值对，并返回该键值对。 用法：排序字典.popitem(last=False)
- 将指定键移动到字典头或者尾部move_to_end(key, last=True)
- 可以实现O(1)复杂度的LRU缓存算法
```
# 普通字典
no_order = {}
no_order["b"] = "b"
no_order["a"] = "a"
no_order
{'a': 'a', 'b': 'b'}
# 有序字典
from collections import OrderedDict
order_dict = OrderedDict()
order_dict["b"] = "b"
order_dict["a"] = "a"
order_dict
OrderedDict([('b', 'b'), ('a', 'a')])
```
### all/any 
- link
    - https://www.jianshu.com/p/65b6b4a62071
- all()："有‘假’为False，全‘真’为True，iterable为空是True"
- any()："有‘真’为True，全‘假’为False，iterable为空是False"
- iterable为空指的是 里面的元素都是空
```
bool([[]])
True
bool([[], []])
True
all([[], []])
False
all([]) # 这种指的是iterable为空
True
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
