# link
- https://www.cnblogs.com/mashuqi/p/11576705.html
- https://huaweicloud.csdn.net/63a57338b878a54545947b1f.html
# 占位符
- link: https://www.runoob.com/python/python-date-time.html
`%Y-%m-%d %H:%M:%S`

# 输出时间
`print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))`

# time
- 时间戳 time.time() # 获取从1970年1月1日到现在的时间秒数
```
time.time() # 1642646490.798591
```

- 将时间戳转换为日期格式
```
t = time.localtime(0)
print(type(t)) # <class 'time.struct_time'>
# tm_wday: 星期几(0-6), 0是周一; tm_yday: 一年的第几天(1到366); tm_isdst: 夏令标识(1-夏令时 0-非夏令时 -1-不确定)
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1642613319))
```

# datetime
- 获取日期
```
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d"))
2023-02-20
```
- 字符串转换为datetime对象: strptime()
```
t = "2022-01-16 16:00:00"
ft = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S") # 因该能看的出来吧，源字符串中有-，format—str里也写"-"
print(type(ft)) # <class 'datetime.datetime'>
# utc格式字符串转换
t = "2022-01-16T16:00:00.000Z"
datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
```
- 操作时间 timedelta 
```
local_time = utc_date_obj + datetime.timedelta(hours=8)
```
- 日期间计算
```
a=datetime.datetime.strptime("2023-02-21 07:59:00", "%Y-%m-%d %H:%M:%S")  # 也可以是datetime.datetime()对象
b=datetime.datetime.strptime("2023-02-22 07:59:00", "%Y-%m-%d %H:%M:%S")
c=datetime.datetime.strptime("2023-02-22 20:59:00", "%Y-%m-%d %H:%M:%S")
print(c-a)  # 1 day, 13:00:00 
# 但是(c-a).seconds只会输出小于一天的秒数 (c-a).seconds和(c-b).seconds的结果一样
```