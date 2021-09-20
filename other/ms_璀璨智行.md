### 1. 给定两个大小分别为 m 和 n 的无序数组 nums1 和 nums2，请你找出并返回这两个数组的中位数 。
```python
def func(list_a, list_b):
    all = list_a + list_b
    all.sort()
    length = len(all)
    if length == 0:
        return 0
    if length % 2 != 0:
        return float(all[int(length / 2)])
    else:
        return (float(all[int(length / 2)]) + float(
            all[int(length / 2) - 1])) / 2
```

### 2. 给定一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
```python
def func(nums):
   for i in range(1,len(nums)+1):
       if i not in nums:
           return i
        return len(nums)+1
```

### 3. 参考以下网站的色差计算器：https://www.colortell.com/colorde，编写一个可根据L*a*b*值生成该颜色图片的程序，并可根据2组L*a*b*值求色差值。
分析： 实现一个色差计算器难度太大，而且该网站有提供API
准备：注册一个网站的账号，以此来访问其提供的api
```python
import request

data = {
    "L": ***
    # 接口数据
    }
cookie = {# cookie
    }
header = {#请求格式}

res = requests.post('api_url', data=data, headers=headers, cookies=cookie)
# 根据res的格式进行解析
```