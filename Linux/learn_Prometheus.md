
# 指标、样本和时间序列
- https://www.prometheus.wang/promql/what-is-prometheus-metrics-and-labels.html

指标的格式是`<metric name>{<label name>=<label value>, ...}`
- 指标名反应的是被监控样本的含义, 指标名的命名规则是`[a-zA-Z_:][a-zA-Z0-9_:]*`所以`method:http_requests:rate5m`也是一个指标名
- 标签名是反映了当前监控样本的特征维度、Prometheus可以根据标签对数据进行过滤和聚合

样本就是监控指标在某一时刻的具体数据，有三个部分组成
```
<--------------- metric ---------------------><-timestamp -><-value->
http_request_total{status="200", method="GET"}@1434417560938 => 94355
```
- 指标(metric)：metric name和描述当前样本特征的labelsets;
- 时间戳(timestamp)：一个精确到毫秒的时间戳;
- 样本值(value)： 一个float64的浮点型数据表示当前样本的值。

时间序列是一种数据的保存方式，Prometheus会把样本数据以时间序列的方式保存到时序数据库中；time-series是按照时间戳和值的序列顺序存放的，我们称之为向量(vector). 每条time-series通过指标名称(metrics name)和一组标签集(labelset)命名，然后里面每个点就是每个时刻的样本数据


# 配置
- 配置项写在Prometheus.yaml里
## 自定义标签
- 可以自定义标签，有了这些标签可以针对特定的标签去查询，比如根据机房，或者项目查询某些机器
- link：https://blog.csdn.net/qq_34556414/article/details/113503945

# PromQL
PromQL是Prometheus自定义查询语言，通过PromQL用户可以非常方便的对监控样本数据进行统计分析，支持常见的运算操作符，此外还提供了大量的内置函数可以实现对数据的高级处理
- https://www.prometheus.wang/promql/prometheus-query-language.html
## 查看时间序列
- 使用监控指标名称查询,可以查询该指标下的所有时间序列,包括不同的标签，查看的结果是瞬时向量
```
http_requests_total{}
http_requests_total{code="200",handler="alerts",instance="localhost:9090",job="prometheus",method="get"}=(20889@1518096812.326)
http_requests_total{code="200",handler="graph",instance="localhost:9090",job="prometheus",method="get"}=(21287@1518096812.326)
```
- 还支持根据时间序列的标签匹配模式对时间序列进行过滤，匹配模式有完全匹配和使用正则表达式来匹配
  - 通过使用label=value可以选择那些标签满足表达式定义的时间序列；使用label!=value则可以根据标签匹配排除时间序列；
  - 使用label=~regx表示选择那些标签符合正则表达式定义的时间序列；使用label!~regx进行排除；
- 范围查询
直接使用指标名称来查询，结果称为瞬时向量；还可以使用区间向量表达式来查询过去一段时间范围内的样本数据，时间范围通过[]来定义` quantdo_memory_dbusage{}[5m]`，这样的结果成为区间向量
    - 还支持别的时间单位
- 时间位移操作
  - http_request_total{} offset 5m # 查询5min之前的
## 标量和字符串
- 标量使用scalar()将单个瞬时向量转换为标量
- 字符串就是加入我们使用自字符串作为PromQL，就会直接返回字符串
## 合法的PromQL表达式
- 必须包含一个指标名称，或者一个不会匹配到空字符串的标签过滤器如`{code="200"}`
- `{__name__=~"http_request_total"}` 等同于直接使用指标名称
## 操作符
- link：https://www.prometheus.wang/promql/prometheus-promql-operators-v2.html

## PromQL操作符
### 匹配模式
匹配模式应用于向量和向量之间进行运算时，默认的匹配规则是找到与左边向量元素匹配（标签完全一致）的右边向量元素进行运算；但除此之外，还有一对一匹配、一对多匹配和多对一匹配。
  
- 一对一匹配 on ignoring
  >当指标元素不完全一致时，可以使用on或者ignoring来忽略标签的匹配规则
  - ignoring可以在匹配时忽略某些标签
  - on可以将匹配行为限定在某些标签内；如果on()里面没有标签，就是忽略所有的标签
- 一对多和多对一匹配
  > 这种匹配是指"一"侧的每个向量都可以与“多”侧的多个元素进行匹配的情况（一侧的是每个都可以参加，多侧的是必须标签和一侧的匹配的才可以参加。
  > group_left或者group_right来确定哪一个向量具有更高的基数（充当“多”的角色）。group_left是多对一
  > 多对一和一对多两种模式一定是出现在操作符两侧表达式返回的向量标签不一致的情况。因此需要使用ignoring和on修饰符来排除或者限定匹配的标签列表。
  ```
  # 一个多对一的例子
  # 存在样本
  method_code:http_errors:rate5m{method="get", code="500"}  24
  method_code:http_errors:rate5m{method="get", code="404"}  30
  method_code:http_errors:rate5m{method="put", code="501"}  3
  method_code:http_errors:rate5m{method="post", code="500"} 6
  method_code:http_errors:rate5m{method="post", code="404"} 21
  
  method:http_requests:rate5m{method="get"}  600 
  method:http_requests:rate5m{method="del"}  34
  method:http_requests:rate5m{method="post"} 120
  # PromQL表达式：method_code:http_errors:rate5m{code="500"} / ignoring(code) group_left method:http_requests:rate5m
  # 结果
  # method:http_requests:rate5m{method="get"}  600 与 method_code:http_errors:rate5m去匹配，匹配到两个结果，运算后的记录
  {method="get", code="500"}  0.04            //  24 / 600
  {method="get", code="404"}  0.05            //  30 / 600
  # method:http_requests:rate5m{method="del"}  34 与 method_code:http_errors:rate5m指标去匹配，没有匹配的标签
  # method:http_requests:rate5m{method="post"} 120 有匹配产生结果
  {method="post", code="500"} 0.05            //   6 / 120
  {method="post", code="404"} 0.175           //  21 / 120
  ```
## 内置函数
- link：
  - https://www.prometheus.wang/promql/prometheus-promql-functions.html
  - https://blog.csdn.net/qq_42883074/article/details/114965134
- absent 判断瞬时向量是否有值,如果有样本，结果为null，感觉好反常，常用于判断某个标签的指标不存在时发出告警
```
  - alert: NoMarketTrendReport
    expr:  absent(qmarket_topic_flowcount{topicid="{{m.topicid}}"})
    for: 1m
    labels:
      severity: page
      cluster: {{ cluster }}
      instance: market-{{m.name}}
    annotations:
      description: "No active log reporting market {{m.name}}/{{m.topicid}}"
```
- delta 计算指标在给定时间间隔内最大值和最小值的差距 `delta(node_memory_MemAvailable_bytes[2m])`
- rate 计算指标在给定时间内的增长率`rate(mysql_global_status_queries[2m]) > {{ thresholds.mysqlqps_warnmark }}`
- abs 返回绝对值

