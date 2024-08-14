### 连接查询
|stats count as c1 by date_histogram(@timestamp,1h,format="HH") as ts|join type=inner ts (search source=*:app_cbcs_applog_source* @timestamp >= "-1d#d" and @timestamp < "#d"|stats count as c2 by date_histogram(@timestamp,1h,format="HH") as ts)

### 采集器看板过滤
`ip`!="10.201.81.143"
`process_name` *= "*flow*" NOT `ip` in ("10.201.81.142","10.201.81.142")| stats avg(mem_usage) as avg_mem by `ip`(size=100000),process_name(size=100000)|stats sum(avg_mem) as sm by `ip`|eval Memory=sm/1024/1024|filter Memory >110|table `ip`,Memory

### 日志延时看板
|sort -@storageTime|head 1|eval ct=time_to_millis(@collectiontime)|eval st=time_to_millis(@storageTime)|eval ct=ct/60000|eval ct=cast_to_int(ct)|eval st=st/60000|eval st=cast_to_int(st)|eval dt=st\-ct|eval dt=if(dt>5, dt,0)|table dt

`@ip` in ("10.231.176.139","10.231.176.140","10.201.176.111","10.201.176.112")