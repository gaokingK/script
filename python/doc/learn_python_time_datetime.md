# link
- https://www.cnblogs.com/mashuqi/p/11576705.html
# 占位符
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