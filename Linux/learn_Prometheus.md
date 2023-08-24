# 入手：
### 可配置的地方
- 并且根据这些规则计算是否向外部发送通知
- 定义自己的告警计算周期
- 告警的配置文件位置和现有的告警可以在ip:9090/alerts里面看
- 告警规则在ip:9090/页面上的status-> rules里看
### 文档
- 中文文档：https://hulining.gitbook.io/prometheus/guides/go-application
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

# 告警 和 altermanager
### 可配置的地方
- 并且根据这些规则计算是否向外部发送通知
- 定义自己的告警计算周期
- 告警的配置文件位置和现有的告警可以在ip:9090/alerts里面看
- 告警规则在ip:9090/页面上的status-> rules里看
### 告警规则：https://www.prometheus.wang/alert/prometheus-alert-rule.html
- 在Prometheus全局配置文件中通过rule_files指定一组告警规则文件的访问路径
### 时区转换
- prometheus 使用的是utc时间
- 建议自己在prometheus内更改时间吗：https://huaweicloud.csdn.net/63311ae5d3efff3090b52316.html
> Can I change the timezone? Why is everything in UTC?
  To avoid any kind of timezone confusion, especially when the so-called daylight saving time is involved, we decided to exclusively use Unix time internally and UTC for display purposes in all components of Prometheus. A carefully done timezone selection could be introduced into the UI. Contributions are welcome. See issue #500 for the current state of this effort.
  - 不建议，可以在ui中更换时间；prometheus的自带面板里的use local time 就是utc时间输出后，前端js做了一次转换。
### 告警的状态
- Inactive: 表示没有达到告警的阈值，即expr表达式不成立。
- pengding: 表示达到了告警的阈值，即expr表达式成立了，但是未满足告警的持续时间，即for的值。
- firing: 已经达到阈值，且满足了告警的持续时间。如果同一个告警数据达到了Firing，那么不会再次产生一个告警数据，除非该告警解决了。
- 如果重启，firing会消失
- 如果配置了发送，只有firing才会发送，直到firing状态消失，如果没有消失就会一直发送
### endpoint
在 Prometheus Alertmanager 中，`endpoint` 用于定义警报通知的目标。通过配置 `endpoint`，你可以指定警报通知要发送到的目标位置，例如电子邮件、Slack、PagerDuty 等。

要配置 `endpoint`，你需要编辑 Alertmanager 的配置文件（通常是 `alertmanager.yml`）。在该配置文件中，你可以定义一个或多个 `receiver`（接收器），并为每个接收器指定 `endpoint`。

以下是一个示例配置文件的片段，展示了如何配置 `endpoint`：

```yaml
receivers:
  - name: 'email-notifications'
    email_configs:
      - to: 'your-email@example.com'
        from: 'alertmanager@example.com'
        smarthost: 'smtp.example.com:587'
        auth_username: 'your-username'
        auth_password: 'your-password'
  - name: 'slack-notifications'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK'
```

在上述示例中，我们定义了两个接收器：`email-notifications` 和 `slack-notifications`。`email-notifications` 使用电子邮件作为 `endpoint`，而 `slack-notifications` 使用 Slack 作为 `endpoint`。

根据不同的 `endpoint` 类型，你需要提供相应的配置参数。在示例中，我们提供了使用电子邮件的配置参数（`to`、`from`、`smarthost`、`auth_username` 和 `auth_password`），以及使用 Slack 的配置参数（`api_url`）。

一旦你编辑好 Alertmanager 的配置文件，保存并重新加载配置。Alertmanager 将根据配置发送警报通知到指定的 `endpoint`。

请注意，具体的配置参数和设置可能因 Alertmanager 版本和使用的 `endpoint` 类型而有所不同。在实际使用中，你应该参考 Alertmanager 的官方文档或特定 `endpoint` 的文档，以了解详细的配置方式和要求。 

# 配置
- 配置项写在Prometheus.yaml里
- 修改配置后重启prometheus
  - 可以ps-ef|grep prometheus查看prometheus的启动命令
- 清空删除meteric https://blog.frognew.com/2021/08/how-to-delete-prometheus-metrics.html
  - prometheus启动时需要加上--web.enable-admin-api（如果是配置文件，需要使用\来换行 然后systemctl daemon-reload ）
  - curl -X PUT -g 'http://127.0.0.1:9090/api/v1/admin/tsdb/delete_series?match[]=up{app="someapp"}&start=2021-08-01T00:00:00.000Z'
  - 可以使用match[]={kubernetes_name="redis"}'删除与某个标签匹配的所有时间序列指标
  - 需要注意使用数据删除接口将metric数据删除后，只是将数据标记为删除，实际的数据(tombstones)仍然存在于磁盘上，可以通过数据清理接口显式地清除。
    - PUT /api/v1/admin/tsdb/clean_tombstones
## 标签
- 可以自定义标签，有了这些标签可以针对特定的标签去查询，比如根据机房，或者项目查询某些机器
- link：
  - Prometheus 一文带你搞懂标签label的作用 https://blog.csdn.net/qq_34556414/article/details/113503945
  - 
- 不同的配置文件中（告警规则的配置，prometheus的配置）怎么读取label可以读取的lable有哪些https://www.cnblogs.com/gered/p/14376868.html
- 告警规则中读取label
  - $labels 读取metric中的标签，但是如果出现了by，就只能读取by（）里面的了
  - {{ $labels.xxx }} 一定要使用双引号包括
- metric_relabel_configs 中为啥不能使用__address__ 作为replace的源标签（不起作用）换成relabel_configs就好了呢？
- global：external_labels
  - 配置项external_labels是用于外部系统标签的，不是用于metrics数据
- job：honor_labels
  - honor_labels主要用于解决prometheus server的label与exporter端用户自定义label冲突的问题。

## Prometheus-配置解析  https://www.cnblogs.com/liujiliang/p/10080849.html
- 可以写多个target： https://blog.51cto.com/u_12227788/5422953

## 告警规则的配置：
- description: "{{ $labels.node }} have {{ printf \"%.0f\" $value }} processes in zombie/dead/waitingIO state."
- 一个告警文件里面可以有同名的告警规则
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
- 字符串就是假如我们使用自字符串作为PromQL，就会直接返回字符串
## 合法的PromQL表达式
- 必须包含一个指标名称，或者一个不会匹配到空字符串的标签过滤器如`{code="200"}`
- `{__name__=~"http_request_total"}` 等同于直接使用指标名称
## with 和 by
- link：https://wiki.eryajf.net/pages/87c873/
by: 向量中只保留列出的标签(维度)，其余标签则移除，必须指明标签列表。
```cs
proc_pid_stat_rss_kb
proc_pid_stat_rss_kb{cluster="cluster1", comm="AliSecGuard", instance="10.0.5.89:9999", ip="10.0.5.89", job="procexporter-cluster2", node="10.0.5.89-tag", pid="1704"}  1449984
proc_pid_stat_rss_kb{cluster="cluster1", comm="AliYunDun", instance="10.0.5.89:9999", ip="10.0.5.89", job="procexporter-cluster2", node="10.0.5.89-tag", pid="21243"}  7909376
proc_pid_stat_rss_kb{cluster="cluster2", comm="AliSecGuard", instance="10.0.5.44:9999", ip="10.0.5.44", job="procexporter-cluster2", node="cluster2-10.0.5.44", pid="2443"} 864256
proc_pid_stat_rss_kb{cluster="cluster2", comm="AliYunDun", instance="10.0.5.44:9999", ip="10.0.5.44", job="procexporter-cluster2", node="cluster2-10.0.5.44", pid="21566"} 6758400
sum(prometheus_http_requests_total) 1449984 + 7909376 + 864256 + 6758400
sum(prometheus_http_requests_total) by (cluster,) # 根据cluster进行分组，相同的值为1组，sum计算这一组里的值；为cluster1的为一组，值为 1449984 + 7909376；cluster2的为一组，值为 864256 + 6758400
sum(prometheus_http_requests_total) by (cluster, comm) 会根据cluster和comm的值分组，共有四组
```
without: 用于从计算结果中移除列举的标签(维度)，而保留其它标签。
通常如上两个函数都配合sum()函数一同出现，by用于聚合我们关心的列，而without则可以直接理解为by的相反用法。
## 操作符
- link：https://www.prometheus.wang/promql/prometheus-promql-operators-v2.html
- 这样也可以分组
  - `fs_block_available_count{node=~"${node:pipe}"}/fs_block_total{node=~"${node:pipe}"}`
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
- 内置函数的对象区分range vector 和instant vector
  - https://blog.csdn.net/hugo_lei/article/details/113400270
- absent 判断瞬时向量是否有值,如果有样本，结果为null，感觉好反常，常用于判断某个标签的指标不存在时发出告警
```

#先获取一个瞬时向量作为参数，然后判断这个瞬时向量是否有值
#如果该向量存在值，则返回空向量
#如果该向量没有值，则返回不带标签名称的时间序列 并返回值为1
 
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

