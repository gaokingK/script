# TO: logstash
## link
- 官方文档：https://www.elastic.co/guide/en/logstash/6.5/plugins-filters-translate.html
- 中文:https://doc.yonyoucloud.com/doc/logstash-best-practice-cn/codec/json.html
- https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html
### 主要分为三个部分：读取、过滤、输出。重点在过滤上面，可以丢弃消息，可以替换属性、可以新增属性
# input
input{ 
    stdin{ # 从标准输入读取，运行该logstash后会从当前终端读取，读取后根据output里定义的方式输出
        codec => "json" 必须加上这个才能将结果解析为json，否则会认为是字符串
    }
}
# filter

### mutate
- mutate具有以下几个函数（sql用惯了）https://blog.csdn.net/wu2700222/article/details/89875092
- gsub  `gsub => ["fieldname", "/", "_",]`# replace all forward slashes with underscore 
- translate 定义一个字典类型的映射关系，从原字段中的值根据映射关系生成对应的值放到新字段中
- if判断 https://www.elastic.co/guide/en/logstash/current/event-dependent-configuration.html#conditionals
```
if [kpi_name] in ["value1", "value2"]{ # 列表里不能只有一个值，if [kpi_name] in ["value1"] # 这样永远是False
    drop()
}
if [kpi_name] not in ["value1", "value2"]{
    drop()
}
if [kpi_name] == "value1"{
    drop()
}
if [kpi_name] =~ "value1"{ # 详细的还要去查，只是说有一个这样的模糊匹配逻辑
    drop()
}
if [kpi_name] != "value1"{
    drop()
}
if [kpi_name]{
    drop()
}
```

### date
- https://doc.yonyoucloud.com/doc/logstash-best-practice-cn/filter/date.html
```
date {
        match => ["logdate", "ISO8601"]
        traget => "log_time"
    }
logdate: 2024-11-09T09:34:22.553Z
经过处理后会生成log_time字段，值为2024-11-08T01:34:22.553Z比本地时间早8个小时

```
### output
```
output{
    if [session_active_count] {
        stdout{
            codec => line {
                format => "kpi.%{session_active_count}"
            }
        }
    }
}
```
# logstash 日志
- 默认配置：https://github.com/elastic/logstash/blob/main/config/log4j2.properties
  - https://logging.apache.org/log4j/2.x/manual/appenders.html#CustomDeleteOnRollover
- 有一个自己的处理日志，关于这个日志是使用log4j实现的
- 只有当前生成的日志超过了`appender.deprecation_rolling.policies.size.size = 100MB`所指定的大小是才会进行日志的删除操作
- 正确的配置：https://discuss.elastic.co/t/rotate-and-remove-old-logstash-output-logs/256803/5
```cs
status = error
name = LogstashPropertiesConfig

appender.console.type = Console
appender.console.name = plain_console
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = [%d{ISO8601}][%-5p][%-25c] %m%n

appender.json_console.type = Console
appender.json_console.name = json_console
appender.json_console.layout.type = JSONLayout
appender.json_console.layout.compact = true
appender.json_console.layout.eventEol = true

appender.rolling.type = RollingFile
appender.rolling.name = plain_rolling
appender.rolling.fileName = ${sys:ls.logs}/logstash-${sys:ls.log.format}.log
appender.rolling.filePattern = ${sys:ls.logs}/logstash-${sys:ls.log.format}-%d{yyyy-MM-dd}-%i.log.gz
appender.rolling.policies.type = Policies
appender.rolling.policies.time.type = TimeBasedTriggeringPolicy
appender.rolling.policies.time.interval = 1
appender.rolling.policies.time.modulate = true
appender.rolling.layout.type = PatternLayout
appender.rolling.layout.pattern = [%d{ISO8601}][%-5p][%-25c] %-.10000m%n
appender.rolling.policies.size.type = SizeBasedTriggeringPolicy
appender.rolling.policies.size.size = 100MB
appender.rolling.strategy.type = DefaultRolloverStrategy
appender.rolling.strategy.max = 30
appender.rolling.strategy.delete.type = Delete
appender.rolling.strategy.delete.basePath = ${sys:ls.logs}
appender.rolling.strategy.delete.maxDepth = 1
appender.rolling.strategy.delete.ifLastModified.type = IfLastModified
# Delete files older than 30 days
appender.rolling.strategy.delete.ifLastModified.age = 30d
```

