# link
- https://www.cnblogs.com/mashuqi/p/11576705.html
- https://huaweicloud.csdn.net/63a57338b878a54545947b1f.html
# 占位符
- link: https://www.runoob.com/python/python-date-time.html
```cs
%Y-%m-%d %H:%M:%S
%f 代表毫秒
%F 等于%Y-%m-%d 2023-01-15
```


# some
- ISO format.  yyyy-mm-dd.
- offset-naive型，就是一个不含时区的datetime。含时区的offset-aware型 https://blog.csdn.net/myli_binbin/article/details/94011880
# 输出时间
`print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))`

# 时区
- astimezone: 改变时区
    - 如果对tzinfo属性的日期来修改时区的话也会修改时间，例如 utc 时间 为 2021/04/15 17:00:00 改为 北京时间后，则变为 2021/04/16 01:00:00；如果原本没有时区属性，也会修改
- replace 方法用于操作模块datetime的datetime类的对象。 replace(tzinfo = new_timezone_info) 替换时区, 时间数值不会发生变化，例如 utc 时间为 2021/04/15 17:00:00 改为 北京时间 2021/04/15 17:00:00 ， 或者 没有timezone 的 datetime实例 可以通过这个函数附上 timezone
- stimezone 与 replace 都返回一个全新的datetime实例, 不会修改原有datetime实例

- 时区对象：
    - shanghai_tz = pytz.timezone("Asia/Shanghai")
    - utc_tz = pytz.timezone("utc")
```cs
s_time
datetime.datetime(2023, 6, 5, 3, 4, 48, 740000)
s_time.tzinfo
s_time.astimezone(utc_tz)
datetime.datetime(2023, 6, 4, 19, 4, 48, 740000, tzinfo=<UTC>)
s_time.astimezone(shanghai_tz) //根据的是本地时区向utc转换的
datetime.datetime(2023, 6, 5, 3, 4, 48, 740000, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
s_time.replace(tzinfo=utc_tz).astimezone(utc_tz) # 应该这样
datetime.datetime(2023, 6, 5, 3, 4, 48, 740000, tzinfo=<UTC>)
```
# time 
### 时间戳 time.time() # 获取从1970年1月1日到现在的时间秒数 timestamp
```
time.time() # 1642646490.798591
```

### 将时间戳转换为日期格式字符串
```
t = time.localtime(0)
print(type(t)) # <class 'time.struct_time'>
# tm_wday: 星期几(0-6), 0是周一; tm_yday: 一年的第几天(1到366); tm_isdst: 夏令标识(1-夏令时 0-非夏令时 -1-不确定)
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1642613319))
```

# datetime
### 获取指定格式的日期
```py
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d")) #%Y-%m-%d %H:%M:%S
2023-02-20
```
### 字符串转换为datetime对象: strptime()
```py
t = "2022-01-16 16:00:00"
ft = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S") # 因该能看的出来吧，源字符串中有-，format—str里也写"-"
print(type(ft)) # <class 'datetime.datetime'>
# utc格式字符串转换
t = "2022-01-16T16:00:00.000Z"
datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%fZ")
```
### 操作时间 timedelta 
```python
local_time = utc_date_obj + datetime.timedelta(hours=8)
local_time = datetime.datetime.now() + datetime.timedelta(hours=8)
```
### 日期间计算
```python
a=datetime.datetime.strptime("2023-02-21 07:59:00", "%Y-%m-%d %H:%M:%S")  # 也可以是datetime.datetime()对象
b=datetime.datetime.strptime("2023-02-22 07:59:00", "%Y-%m-%d %H:%M:%S")
c=datetime.datetime.strptime("2023-02-22 20:59:00", "%Y-%m-%d %H:%M:%S")
print(c-a)  # 1 day, 13:00:00 
# 但是(c-a).seconds只会输出小于一天的秒数 (c-a).seconds和(c-b).seconds的结果一样
```

### 日期转换为时间戳
```py
import datetime
import time
# 获取当前时间
dtime = datetime.datetime.now()
un_time = time.mktime(dtime.timetuple())
print(un_time)
# 将unix时间戳转换为“当前时间”格式
times = datetime.datetime.fromtimestamp(un_time)
print(times)

```
