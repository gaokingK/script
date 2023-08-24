# grafana
### doc
  - Grafana 实现一个Panel的多数据源告警（PromQL 给指标添加 label）：https://blog.csdn.net/qq_21047625/article/details/127093939
  - 官方文档：https://grafana.com/docs/grafana/latest/
### 官方例子：https://play.grafana.org/d/000000029/prometheus-demo-dashboard?orgId=1&refresh=5m&editview=templating

### Grafana变量及panel links中的变量使用
- link: https://juejin.cn/post/7098581066927046669
- grafana绘图配置查询变量+多级变量联动:https://blog.csdn.net/CleverCode/article/details/104324039
- 怎么使用变量
  - quantdo_memory_dbusage{exported_job="$app", cluster="$cluster"} 
  - ${cluster} 这种可以放在单词中，前后没有空格，还可以格式化变量
    - 格式化语法: https://docs.aws.amazon.com/zh_cn/grafana/latest/userguide/v9-dash-variable-syntax.html
  - 可多选的变量会转义 如 cluster=10.0.0.89  会转义为 `cluster=\"10\\\\.0\\\\.5\\\\.89\"` 这回影响正常查询，可以使用变量格式化 `cluster="${cluster:raw}"` 这样就是`cluster=\"10.0.5.89\"`这样就不会影响了
  - 还有当变量为all或者是选中了多个值时，查询结果查不出来是正常的，这时可以看下网络请求
  - `${var:pipe}`将具有多个值的变量格式化为竖线分隔的字符串。 proc_uptime_up{cluster=~"${cluster:pipe}"} 这样可以使用cluster多选的值作为本变量的查询参数 # 注意是`=~`不是`=`
- 变量定义了后保存重新进来如果没有被引用会提示
- 变量的查询语法 
  - Grafana--变量(label_values)：https://www.cnblogs.com/Xinenhui/p/16188951.html
  - label_values(metric_name, label1_name) 返回metric_name 标签label1_name的值 
    - label_values({__name__=~"metric1|metric2|metric3", service=~"abc.*xyz"}, service)
  - query_result(proc_uptime_up)  query_result 返回prometheus的查询结果 有些metrics删除了还会再grafana里查询出来
- 这样也可以分组
  - `fs_block_available_count{node=~"${node:pipe}"}/fs_block_total{node=~"${node:pipe}"}`


### 数据源
- 数据源在哪里添加：设置>data source
- 数据源的url不要有空格
- 在面板上点击edit 
  - Event/Animation Mappings 根据id 当`What`中的id(simplejson中返回的target值)达到`When`设定的值时，采用`Action的动画`
  - Link Mappings 根据选中的id还是label，当when时always时，点击该按钮达到url中指定的值，url可以是/d/7_MOyG5Vz/appjian-kong?orgId=1&refresh=10s&var-app=qtrade&viewPanel=12,这个url是从哪里看呢？
    - 是点击面板下拉箭头 share里面的值去掉ip：port后的就是

- json API 的数据源在查询时cache time应该设为0s，设置为别的值点击查询后会查询不出来，不知道为啥 返回的结果是json
- simple json 返回的结果按时间序列 去解析的
  - 在Value Options 里面的Fields里选择值后才能显示
#### simplejson
- 根据`Data Source`后面的问号图标来看 帮助，后端需要实现4个接口
- 查询时只能使用{target": "upper_50", "refId": "A", "type": "timeserie" }这三个key吗？

### Dashboards
- 这些dash board 可以点击new新建，然后可以在左边栏的dash board里查看所有的，并且这些打开后在地址栏里的链接可以放到面板的按钮里的link里

### panel 是dashboards里面的面板，一个dashboards可以有好多个panne，点击上方的添加图标，会添加一个pannel ，pannel有好多不同的类型
- https://juejin.cn/post/7099006755513827358
- 可以将根据字符串的值选择不同的颜色，在value mapping里 添加映射规则的时候点击右边的设置颜色
#### legend 
- 可以调整位置在下面还是右面
- 可以调整值为0的不显示


# progress
- 看懂了task.yml
- palybook里面的设置：
    - gather_facts: true # 制默认facts收集（远程系统变量）
    - any_errors_fatal: yes 
    - become: yes # https://blog.csdn.net/u013084266/article/details/105670617
    - max_fail_percentage: 0 # 失败的机器个数占比超过所设定的百分比才会停止，0是不停止

### loki(promtail) + Grafana
-  grafana 公司开发的 loki 日志收集应用。Loki 是一个轻量级的日志收集、分析的应用，采用的是 promtail 的方式来获取日志内容并送到 loki 里面进行存储，最终在 grafana 的 datasource 里面添加数据源进行日志的展示、查询。
#### promtail
- doc
  - https://jishuin.proginn.com/p/763bfbd5863b
  - https://blog.frognew.com/2023/05/loki-04-promtail-intro-and-config-ref.html
- 假如promtail放到rootfs里运行的话，需要把原本的日志目录给mount到promtail的rootfs里面
- 可以根据client里的配置给加label
```
clients:
  - url: http://10.0.5.89:3100/loki/api/v1/push
    external_labels:
      cluster: "mylocal-1"
      ip: "10.0.5.44"

```
- 也可以产生metrics
#### loki too many outstanding requests
- https://github.com/grafana/loki/issues/5123
```
# 配置文件中增加
querier:
  max_concurrent: 2048
query_scheduler:
  max_outstanding_requests_per_tenant: 2048
```
#### Loki QL查询语句
- link
    - https://blog.csdn.net/weixin_44267608/article/details/105264432
    - https://juejin.cn/post/7202557470342316087

- 基本的LogQL查询由两部分组成：log stream selector、filter expression
- Log stream selector
    - 它由一个或多个键值对组成，每个键是一个日志标签，值的话是标签的值 `{app="mysql",name="mysql-backup"}`
    - =：完全相等。
    - !=：不相等。
    - =~：正则表达式匹配。
    - !~：正则表达式不匹配。
- filter expression
    - 写入日志流选择器后，可以使用搜索表达式进一步过滤生成的日志集。搜索表达式可以只是文本或正则表达式：`{job=“mysql”} |= “error”` 在`}`后面的就是filter expressinon
    - |=：日志行包含字符串。
    - !=：日志行不包含字符串。
    - |~：日志行匹配正则表达式。
    - !~：日志行与正则表达式不匹配。

- 指标查询
    - rate：计算每秒的条目数 `rate({job="fluent-bit"} |= "error" != "timeout" [10s]  `
    - count_over_time：计算给定范围内每个日志流的条目。`count_over_time({job="fluent-bit"}[5m])`

- 集合运算符
    - 可用于聚合单个向量的元素，从而产生具有更少元素但具有集合值的新向量
    - 可以通过包含without或 by子句，使用聚合运算符聚合所有标签值或一组不同的标签值：`<aggr-op>([parameter,] <vector expression>) [without|by (<label list>)]`
    - sum：计算标签上的总和
    - min：选择最少的标签
    - max：选择标签上方的最大值
    - avg：计算标签上的平均值
    - stddev：计算标签上的总体标准差
    - stdvar：计算标签上的总体标准方差
    - count：计算向量中元素的数量
    - bottomk：通过样本值选择最小的k个元素
    - topk：通过样本值选择最大的k个元素