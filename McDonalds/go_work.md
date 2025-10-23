### TODO
- office-vc 变成office
- 那就是那个salary的消费者挂了嘛，就那个进程挂了。然后进程挂了，是不是因为其他原因或者说比如说在Siri work运行的过程当中，连接不上red了，然后他就挂了。但是他自己不会把自己拉起来呢。
- other改成未知
- 集群分配优先根据满的
- 实例规格加载速度
- 0418
- 资源概览首页内存/cpu/磁盘增加单位
- 资源概览首页虚拟机维度为什么还有office-vc
- 资源概览虚拟机创建时间散点图 改为所属账户
- 0421
- 改为redis和kafka的费用预估
- 服务器预估修改
- 0530
- 把虚拟机Aws换成全大写的
- 把虚拟机关机换成已关机
- 存储设备关联哪些集群 关联哪些lun 一个存储设备分了哪些硬盘 
- 0627e
- 实例规格 靠左对齐
- 标签筛选首字母大写  
- IP子网
- 机柜 设备类型 没有详细信息
- VPC IPv6不放 所属域 = 项目 包含二层网络下·
- 6200  6201(多) 高速轴承不是看盖的材质，看精度，一般p4和p5的就行
- 多个物理机组成一个vsphere集群 一个宿主机挂多个lun 一个lun挂多个虚拟机
- 去idc msp 问手动管理了哪些数据？每个云账号使用了哪些资源 和gitlab/netbox
### 0922-1012
- 文件管理开发 剩余加密解密
- 增加费用文件上传类型检查
- 
- finops dev 配置更新 tob-dev-rke集群权限申请
- 增加费用文件上传接口，增加上传加密，优化临时文件处理
- 优化费用文件上传接口参数校验
- 文件下载下来为空 排查
- 新增读取费用文件公共参数
- ip信息检索问题修复 
- 修复获取宿主机关系时无所属物理机时的bug
- 增加对多年份数据的支持，增加月份的可读性转换，增加年月维度切换
- 优化cse费用看板infra分摊
- 优化cse费用看板数据，保留为0的数据
- cse看板适配前端传参
- 要看到每种资源的具体费用
  - 要从项目费用的表格中那到这些数据
  - 只能从cmp中拿到每月里各种资源的比例，然后再用项目费用去计算每种资源具体费用
  - 知道每种资源在每个项目里的费用，可以按资源类型聚合得出每种资源的总费用
  - 查看云账号维度时，可以将项目的云账号映射到资源类型上
  - 查看云服务商维度时，将项目的云服务商映射到资源类型上
### 0908-0921
- 修复宿主机查出来的虚拟机里面ip没有分开的问题
- 更新虚拟机状态映射
- 创建集群流程检查dns和创建vault的方法合到一个方法中
- 修改CASE A集群创建流程，增加valut校验
1. Vault 信息由使用IP改为使用网段
2. 创建Vault前校验k8s node IP是否为同一个网段，不是就卡流程，+重试
- CASE A集群增加网段字段（创建流程中没有，支持修改和查询）

- 给case 查询门店集群的方法里要加上valut信息吗？不加

- PAAS查询集群信息接口中增加vault_secret_id/vault_rold_id/vault_token/cluster_cidr，CASE查询门店和集群信息接口中删去这些字段


- 拉取项目维度的账单
- 数据筛选（保留云上的数据）
- 数据分类
  - 根据项目的business_scope进行分类，分为TOC TOS TOE 和其他四个维度
- 加不加infra
  - 影响总费用的值，如果勾选“加infra" 总费用需要包括标签中business_scope为infra的一些项目费用；如果不勾选，总费用的值等于所有标签中business_scope不为infra的项目费用和。
- DATA 
  - business_scope为DCOE
- 分摊费用或实际费用
  - 分摊费用（两个开关都打开） 实际费用（只打开项目分摊）两个都不打开的不要
- 所属域
  - 可以根据多个所属域进行聚合（多个项目对应一个所属域）
  - 可以根据所属域进行筛选
- 修复同步集群ip时使用同一数据库连接容易超时
### 0825-0906
- 需求  ip信息检索新增支持多资源查询的接口定义
- 需求  将ip信息检索中负载均衡/网络设备/eip的查询逻辑放到service中
- 需求  修改定时更新case A集群k8s ip，增加非云上集群，修改定时任务时间为0:10
- 需求  修改owner/tags接口的返回数据结构，增加tags 解析出的system/module/product
- 需求  修改ip资源表结构，将唯一索引扩展为ip和resource_type
- 需求  增加从资源表同步ip到ip_resource_type表的公共函数，并将弹性IP/负载均衡/网络设备/宿主机/物理机的ip同步到ip_resource_type表中
- 需求  新增宿主机详情接口
- 需求  更新lun采集逻辑，之前采集存储类型为nas的现在采集所有的
- 需求  增加宿主机-块存储的映射关系到资源关系表中
- 需求  宿主机详情开发 
- 需求  新增宿主机关联磁盘/关联虚拟机接口
- 优化  获取宿主机关联虚拟机时适配宿主机字段类型更改
- 新增宿主机关系接口
- 支持 处理同步k8s ip同步任务告警
- 修改ip信息检索返回数据结果
- 修改ip信息检索返回数据结果，返回ip查询同一资源的所有实例
- 新增申请集群的roleID和secretID的方法
- 新增ClusterVaultAPI类
- 修改ip信息检索虚拟机返回数据结构，增加云订阅
- 优化tags接口指定标签key查询时无法返回分列的system/module/product信息
  
- 2019
    - 0504 -300
    - 0505 -100
    - 0509 +400 wx
    - 1231 -300 wx
- 2020
  - 0523 -110 wx 应该是吃饭
  - 0713 -300 wx
  - 0824 -1000 wx
  - 0901 +1000
- 2021 截图
  - 0512 +600
  - 1218 -1000 wx
  - 1220 -1000 收钱码
- 2022 截图
  - 0829 -1000
- 2024
  - 1008 +2000 wx
hms
- 2022
  - 0720 -3000
  - 1121 -3000
  - 1216 -5000
- 2023
  - 0126 -500 wx
  - 0215 -3000
  - 0425 -2000
### 0811-0824
- 优化 新增ip资源检索2，并回退到之前的ip检索
- 问题优化：
    1. 宿主机采集内存cpu超售比修改
    2. ip资源检索时去除ip空格
    3. 修改获取宿主机时内存/存储信息
- 优化 关联关系表数据波动检查
- 需求 新增更新云上集群k8s ip方法
- 需求 新增定时任务同步云上集群k8s ip
- 需求 和金荣华沟通云上账号 云上找王井伟 aure 田田 aws 找长qian   
- 需求 将虚拟机的多种ip都存放到ip资源表中
- 需求 ip资源检索支持虚拟机private_ip/eip/private_ipv6查询
- 需求 ip资源检索中宿主机关联虚拟机的信息里返回虚拟机的private_ip/eip/private_ipv6
- 优化 拼接查询条件公共函数(同步数据告警修复)
- 优化 二层网络接口sql调优
- 优化 修改资源查询获取字段可选值重复公共方法
- 优化 修改资源查询公共方法, 可以查询空值
- 需求 ip信息检索时负载均衡可以用多个ip搜索
- 测试 定时更新case A 集群k8s ip
- 沟通 云上集群权限申请
- 优化 负载均衡增加eip/虚拟机的ip在列表页中显示多个ip的列表
- 优化  优化cmdb公共查询，可以模糊查询
- 优化  优化定时更新k8s ip的前后ip对比逻辑
### 0728-0810
- 联调  安全组关联实例分页
- 需求  安全组规则增加总条数
- 需求  安全组关联实例增加统一值
- 优化  优化wukong审计日志用户名筛选
- 支持  netbox vpn权限申请
- 支持  听培训会
- 需求  宿主机增加cpu超售比/内存超售比/型号/虚拟存储/已使用存储字段
- 优化  虚拟机获取idc ACL的逻辑优化
- 优化  修改虚拟机采集逻辑，将ip_subnet更换为子网名称
- 优化  优化虚拟机磁盘信息和安全组信息获取
- 需求  虚拟机增加获取宿主机信息/获取同宿主机的所有虚拟机
- 需求  信息检索中将虚拟机ip检索替换为从数据库
- 需求  为资源概览的视图函数增加注释
- 需求  信息检索中将物理机p检索替换为从数据库
- 需求  新增网段采集
- 需求  ip资源检索增加负载均衡
- 需求  优化虚拟机关联关系的数据波动检查
- 需求  增加网段同步定时任务，增加数据波动校验
- 需求  ip资源检索修改网络设备数据结构
- 需求  ip资源检索增加虚拟机/物理机关联的pod和cluster列表
- 需求  优化获取虚拟机宿主机方法，不查询host_ip为空
### 0714-0727
- 运维 发版
- 需求  宿主机增加/vm_count/sn/cpu_commit_rate/mem_commit_rate字段
- 排查  IP子网无数据 增加ip子网采集定时任务
- 需求  资源关联表增加d_version字段，二层网络关联宿主机信息存放在关联表中
- 需求  增加查询关联信息公共函数
- 需求  增加关联信息数据来源，修改二层网络关联宿主机信息为数据库
- 排查  李英明创建集群无权限
- 支持  集群列表修改查询结果为按updated_at排序
- 支持  集群增加location字段
- 需求  安全组增加vpc/实例数量/状态字段采集
- 需求  安全组增加列表页查询/我的/导出/详情页接口和关联实例接口定义
- 需求  ip子网增加ip使用情况字段
- 需求  增加虚拟机和安全组和磁盘的关联关系

- 需求  虚拟机详情里获取安全组和磁盘改为从数据库查询
- 优化  数据波动检查函数，支持关系表部分修改
- 需求  磁盘增加平台字段
- 需求  安全组关联虚拟机查询
- 支持  审计日志新增操作名称筛选，筛选参数接口增加操作名称枚举
- 需求  虚拟机增加vpc名称采集
- 需求  修改关联关系表查询关联属性公共方法，支持反向查询
- 需求  安全组关联实例接口增加关联虚拟机数据
- 需求  安全组关联实例接口增加关联负载均衡数据
- 需求  关联关系表中增加负载均衡和安全组关联关系
- 需求  关联关系表中增加关系数据库和安全组关联关系
- 需求  修改原有关联关系同步脚本清除数据逻辑
- 需求  安全组关联实例接口增加关联数据库和Redis数据
- 需求  安全组关联实例查询功能增加，增加公共方法
- 负载均衡增加网络类型字段
- 数据库增加外网地址和数据库端口字段
- redis增加外网地址
- 支持 协助修改新建集群填写错误的名称
- 导出功能
- pvc详情
- 
- 资源概览细化
- 中间件的详情
- 信息检索增加功能 改为从数据库
- 费用报告 根据项目 查下面有哪些功能？
- 
二层网络关联的宿主机数据格式
二层网络导出
vpc关联的安全组接口报错
vpc详情里去掉所在可用区
VPC菜单改为全大写
把ip子网关联搜索去掉 保留ip和资源名称
虚拟机无ip的加斜杠
虚拟机磁盘信息平台字段确认



ptovs-tosp-iot-01 安全组（idc至少有一个10.0.0.0的安全组，云上的是都有的）
安全组 hdvs-dev-etcd-04就没有


详情名称和其他字段没有对应
备注的列宽
状态前加小绿点
系统用图标替代文字
搜索提示改为 ip和名称

虚拟机关联实例标签调窄
表格样式和列表页保持一致

关联虚拟机中的磁盘字段确认

标签和费用预估里的标签的0，1，2...去掉

pod详情里的数据中心图标太大了导致行距不一致



### 0630-0713
- 协助 排查1450988门店查不到集群信息问题
- 需求  IP子网接口定义
- 需求  排查IP子网缺失字段 
- 需求  IP子网详情接口开发
- 
- 优化  审计日志，解决非json返回body报错
- 优化  rds费用预估校验和全局异常处理方法
- 测试  测试云服务器费用预估
- 优化  审计日志 处理未匹配路由
- 优化  增加云服务器/Redis/rds/lb预估必填参数校验
- 优化  统一rds实例规格为nCnG
- 
- 修改  虚拟机cpu/内存/磁盘总量单位
- 新增  IP子网IP使用情况接口
- 需求  二层网络增加宿主机信息字段
- 需求  二层网络列表页增加宿主机信息字段
- 优化  rds费用预估参数获取
- 优化  ip子网增加ipv6网关 ip子网增加线路类型
- 需求  增加vpc 列表页相关接口 ，增加采集字段
- 优化  修改云服务器/Redis/rds/lb预估必填参数校验
- 需求  数据同步任务增加告警
- 需求  关系数据库数据源改为cmp
### 0616-0629
- 修改  redis 增加port字段   
- 修改  redis 增加owner解析逻辑
- 优化  审计日志访问ip获取逻辑
- 修改  redis 中Qcloud改为Tencent Cloud

- 发版sql整理
- 优化虚拟机 ip 取数逻辑 解决某些虚拟机因 该IP地址无归属IP子网， 请添加包含该IP地址的IP子网并重新同步云账号 导致ip为空的问题
- 需求  IP子网搜索字段定义

- 修改 外部接口接口定义
- 需求 网络设备详细信息接口定义

- 
- 404的原因是没有resourcce_uid
- 需求 网络设备增加env/business_area字段
- acl 接口 端口连接信息接口 问网络
- 需求 门店集群信息接口改

- 优化 虚拟机resource_uid获取逻辑，解决虚拟机详情404
- 需求 修改网络设备1. 增加随购维保年限字段 2增加查询条件tags/env和随购维保年限

- 需求 新增网络设备关系图定义
- 需求 lb费用去除媒体类型，增加区域，支持多规格 lb费用预估新增规格费用明细 
- 修改 审计日志不记录/user
- 需求 更新网络设备acl和关系图接口

- 修改 审计日志过滤功能
- 优化 Redis Aws转为全大写 节点备份类型增加映射
- 优化 虚拟机数据采集修改无ip子网的获取ip
  
- 优化 Redis 可用区重复
- 需求 测试用例编写
- 修改 阿里云服务器可选镜像接口修改，根据系统过滤
- 优化 pgsql实例规格接口获取
- 优化 审计日志记录

- 优化 云费用预估实例规格排序
- 修改 阿里云服务器镜像排序
- 优化 格式化费用预估浮点数
- 优化 网络设备关系图增加数据中心
- 需求 新增IP子网关系图接口
- 需求 了解vpc/ip子网/二层网络的区别和联系
### 0603-0615
- 支持 手动新建一个字段不全的集群
- 需求 新增网络设备获取可选值接口
- 发版 发版提sql
- 支持 修改一个云上集群属性
- 联调 网络设备列表页联调

- 需求变更
Location 选择Putuo/Hedan 填写字段不变 去除sku 和OB IP 和K8s IP的数量校验
Location 选择Ali/AWS 只去掉k8s IP输入框，新增LB ID 和K8s ID （两个都是必填的），并由K8s ID获取k8s IP
- 排查门店信息通知case A 数据不同步问题 原因是门店修改集群里未添加
- 支持 新建cn-wukong-pt-ack.mcd.cloud DNS解析工单
- 优化 优化do_request公共方法异常处理
- 需求 case A集群新增根据k8s_id获取k8s_ip功能；编辑工单时支持根据k8s_id重新获取k8s_ip
- 需求 网络设备的我的功能
- 测试发现 某些请求返回体太大导致审计日志报错，优化日志并修改表字段属性
- 修改 修改网络设备owner取值逻辑，将u位为0的改为-1
- 优化 owner筛选时改为大小写不敏感
- 修改 网络设备增加出厂日期 u位为0改为-1
- 修改 更新网络设备 设备类型映射
- 修改 网络设备修改制造商取数逻辑
- 需求 虚拟机中cloud=Qcloud的改为Tencent Cloud
- 优化 删除网络设备无用代码
- 优化 修改使用字符集搜索大小写改为使用ilike
- 问题排查 排查虚拟机数据不是最新的 发现是镜像不是最新的
- 修改 网络设备增加出厂日期字段
- 需求 扩展腾讯云香港云服务器可选实例规格
- 需求 云费用预估修改：     1. 将现有规格更换为最新一代规格族     2. 修改前端显示human_name
- 需求 PAAS查询集群接口返回增加id/k8s_id/lb_id新字段
- 需求 修复编辑工单时支持根据k8s_id未重新获取k8s_ip中bug

完整性 
对象存储 网络设备 项目 详情页


### 0519-0601

- 支持  pass接口优化，增加集群其他信息返回
- 修复  修复虚拟机cloud取值为office的计算逻辑
- 优化  虚拟机数据采集，修复存储容量/owner字段采集逻辑
- 需求  新增审计日志接口定义
- 支持  门店信息修改时，hd和prod的集群可以互相改
- 测试发现 腾讯云rds实例规格无法获取
- 优化  优化虚拟机数据采集中多次创建cmp链接
- 测试发现 去除阿里云rds mssql 停售实例规格
- 测试发现 阿里云rds mssql 某些实例不支持当前版本，修改默认版本并修复
- 需求 新增rds/redis/ecs费用预估每种规格费用明细
- 优化 优化cmdb全局异常处理
- 需求 修改审计日志接口校验
- 需求 审计日志 获取用户名
- 需求 审计日志 增加自定义记录url 
- 测试发现 运费预估 ecs镜像名称重复 增加去重
- 优化 云服务器镜像关联实例规格
- 需求 新增虚拟机筛选/导出接口
- 需求 新增网络设备列表查询/筛选/导出接口
- 需求 新增虚拟机字段可选值接口
- 优化 虚拟机采集将状态改为中文
- 优化 虚拟机采集将计费方式改为中文，云上资源宿主机应为空
- 优化 修改虚拟机/网络设备参数校验模型
- 支持 由于zone00网络设备调整，需要变更下生产boss平台zone00集群的vip地址  
- 优化 云服务器费用预估返回接口数据名修改;云服务器规格按cpu/memory排序后返回
- 优化 定价策略添加时去除空格
- eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFtZlRzSjlZVmE1a2tRLXk5cmFJa1dZd1V0MCJ9.eyJhdWQiOiI4ZWJmOTRkZi1mMDA4LTQwZmMtODU3OS1mMWUyYTVjOTMzZTEiLCJpc3MiOiJodHRwczovL2xvZ2luLnBhcnRuZXIubWljcm9zb2Z0b25saW5lLmNuLzJiYmRkZjFkLTQwZDctNDBlMC1hZjQ3LTc5NTk1N2FiMGUwOS92Mi4wIiwiaWF0IjoxNzQ4MjI2Mzc1LCJuYmYiOjE3NDgyMjYzNzUsImV4cCI6MTc0ODI2OTg3NSwiYWlvIjoiQVZRQXEvOFBBQUFBc0lPZHhab2pqY0J0bVRGZnhkdVJBK3BXejdUbVkwcTRhVHlEazAreHk0VGxva0NzWWo5c2oralh2NjYrR1JqSklSVGJLYzFnNmJ6bElSSUhLUnNhaXdrR1A4bUZDcEpMbXhXbVZvWDBiMWM9IiwiYXpwIjoiOGViZjk0ZGYtZjAwOC00MGZjLTg1NzktZjFlMmE1YzkzM2UxIiwiYXpwYWNyIjoiMCIsImluX2NvcnAiOiJ0cnVlIiwiaXBhZGRyIjoiNTguMzguNDcuMTkwIiwibmFtZSI6ImppbndlaSBqaWFuZyIsIm9pZCI6ImE5OGU1YjlkLTFjYTAtNGY5Yy05ZWIxLWY1YTQxM2UzYTU0ZCIsInByZWZlcnJlZF91c2VybmFtZSI6ImppbndlaS5qaWFuZ29kQGNuLm1jZC5jb20iLCJyaCI6IjAuREFVQUhkLTlLOWRBNEVDdlIzbFpWNnNPQ2QtVXY0NEk4UHhBaFhueDRxWEpNLUVCQUdRLiIsInNjcCI6ImFjY2Vzc19hc191c2VyIiwic2lkIjoiMDA1MDRhYzktZDZmOC02OTUwLWY2YzctNWE4YTQ4MDcxYWVlIiwic3ViIjoiakxGZWZaVUdlc3RPVUgyei1HMGVKam5hNmcxaVlacWtIQmY1dXY2SzVhMCIsInRpZCI6IjJiYmRkZjFkLTQwZDctNDBlMC1hZjQ3LTc5NTk1N2FiMGUwOSIsInV0aSI6ImRmZE9iakt6QlV5WEktMVB6M01vQUEiLCJ2ZXIiOiIyLjAiLCJlbXBsb3llZU51bWJlciI6IlAwMDA4NTAwIiwiZW1wbG95ZWVUeXBlIjoiVmVuZG9yIn0.ZWRUlHdAb_SpR8kYtzb72_RcWJqeGXVBye9wv1galnjizLIHpr6kvxlVXfFUtY8iIGZxa8LLmzdPzXlGdbL-ldZkLOq4IB20CnLCF8AaiedLxpJ1iYJvqooXBL1NbRZL-0NRvabMkky51JjTM3t2QUkFGvcnSATG3xc8bjlgU76dzkXkyQV7kaC0leH0qAGo4t_I05Owt17Ov2rLleutUTD5y8kZkVwkJrHfFYXjrup2D0D2t-f-5Pbsw3qkW45CXSapC5gT8fGTE8BjBzt8A0yT2tq1IZoWaik_4X8QQSRc4usd0iuB3q-7uvHYNywGNiMt3nhJchjycnsB58GdHA.TWNELUJPU1M7UEM
- 
eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjbi1qaW53ZWlqaWFuZ29kIiwibmlja25hbWUiOiLokosq5LyfIiwiZWlkIjoiIiwiZW1wbG95ZWVOdW1iZXIiOiIxODgzNzI1NTM1MCIsInNpdGUiOiJNY0QtQk9TUyIsInRlcm1pbmFsIjoiUEMiLCJsb2dpblRpbWUiOiIyMDI1LTA1LTI2IDEwOjA4OjUxIiwidXNlclR5cGUiOiIxIiwiZXhwIjoxNzQ4MjMyNTMxfQ.Bxlnya2wtEg6O8xzpTWCJVANUz7rWjr5QbZXVVIQeQkv_bfUHW3N5UyryZMlpdbugh8il5X-uC_7cEcDtFX8xQ
### 0506 - 0518
- 一些问题
  - 需求预估准确的问题
  - 修改的内容涉及到别人做过需求的问题 （通知人）
  - 记录 阿里云各种资源共用的接口数据结构差别不大 方法基本可以复用 但腾讯云每个资源都有单独的接口 数据结构上有很大的差别 而且在获取当前的默认参数比如售卖区 是否有默认的版本上也有很大的差别 
  - 周末加班
  - 数据结构和接口需要综合考虑两朵云的四种数据比较耗时
  - 要看参数有哪些取值，是什么意思 哪些是自己需要的
- 修复 虚拟机详情中磁盘挂载和状态字段计算逻辑
- 修改 默认模糊查询逻辑修改
- 修改 虚拟机详情接口数据名 更新虚拟机数据采集逻辑
- 修复 cmp连不上导致主程序启动失败 修改cmp初始化
- 修改 增加虚拟机关联关系数据，并移除宿主机中其他虚拟机的数据
- 修改 虚拟机详情数据结构和资源检索一致
- 需求  新增虚拟机详情信息获取接口安全组/磁盘
- 需求 更新虚拟机详情查询接口
- 修改 更新虚拟机运行状态映射
- 优化 腾讯云rds实例规格获取接口 按human_name排序
- 优化 阿里云rds实例规格获取接口，去重同class_group规格，并按human_name排序
- 优化 阿里云ecs费用预估异常处理
- 需求 新增腾讯云rds mariadb费用预估
- 需求 新增腾讯云rds pgsql费用预估
- 需求 新增腾讯云rds sqlserver费用预估
- 优化 优化阿里云rds mysql资源规格获取， 只按照cpu/memory去重
- 优化 优化阿里云rds资源规格显示名称
- 优化 优化阿里云rds资源规格获取过滤
- 优化 优化阿里云rds参数获取逻辑
- 修改 修改rds费用预估时前端数据为json格式
- 需求 新增腾讯rds mysql规格参数获取/可用zone获取/价格预估接口
- 修改 修改rds询价数据结构
- 测试发现 阿里云ecs ecs.xn4.small不支持ESSD云盘 修复
- 测试发现 阿里云ecsecs.c8y.small指定image报错 修复
- 优化 cmp 连接失败会阻塞程序 修复
- 协作 secret_key 加密
- 修改 修改返回信息和资源检索一样数据结构
- 优化 某些属性为null会校验失败 修复
- 优化 虚拟机多种状态映射中文
- 问题 生产虚拟机采集数据失败的问题
- 需求 阿里云rds费用预估pgsql/mssql/mariadb费用预估
- 需求 阿里云mysql规格参数获取
- 需求 阿里云mysql费用预估
- 需求 腾讯云mysql规格参数获取
- 需求 腾讯云mysql费用预估
- 优化 测试发现腾讯云mysql费用预估时使用默认zone和默认版本出错频率太多 改为动态查询可用zone和支持verison 
- 修改 虚拟机和物理机的关联关系不完美
- 需求 阿里云RDS定价
  - https://next.api.aliyun.com/api/Rds/2014-08-15/DescribePrice?spm=api-workbench.api_explorer.0.0.22e45f24aEoFjJ
  - 地区（上海和香港）
  - 购买时长 1个月
  - zone (不暴露 查询未售空的接口)
  - 资源类型（MySQL SQLServer PostgreSQL MariaDB)
  - 实例类型（主实例/只读实例；maria DB只有主实例）需要获取两次
  - 系列（集群版/高可用版/基础版）mariaDB只有高可用 SQL server只有基础版
  - 实例规格 由上面三个参数确定可选的实例规格列表 映射成类似 2C8GB（独享套餐）mssql.x4.medium.s1 的里列表
  - 数据库版本 因为SQLServer的会影响价格
  - 存储类型（不暴漏）
  - 存储容量（20-64000）步长5
- 阿里云RDS定价最终
  - 地区（上海和香港）
  - 资源类型（MySQL SQLServer PostgreSQL MariaDB)
  - 实例类型（主实例/只读实例；maria DB只有主实例）
  - 系列（集群版/高可用版/基础版）mariaDB只有高可用 SQL server只有基础版
  - 实例规格 类似 类似2C8G/4C16G的列表
  - 数据库版本 因为SQLServer的会影响价格
  - 存储容量（20-64000）步长10

- 腾讯云RDS定价
- 腾讯云RDS定价最终
  - 地区（上海和香港）
  - 资源类型（MySQL SQLServer PostgreSQL MariaDB)
  - 实例规格 类似 类似2C8G/4C16G的列表
  - 存储容量（25-3000）步长10 

- mysql
  - 地域
  - zone(不暴露 查询未售空的接口)
  - 购买时长 1个月
  - 内存 cpu（需要动态获取）类似2C8G/4C16G的组合列表 不同的组合可能对应单节点/双节点/三节点 无法通过接口分辨
  - 存储容量（25-3000）步长5 最大值和最小值与机器型号有关
  - 磁盘类型 不同的实例规格支持的类型不一样 不暴露
- PostgreSQL
  - 地域
  - 购买时长 1个月
  - 购买数量
  - 架构（只有双机高可用）
  - zone(不暴露 查询未售空的接口)
  - 内存cpu 类似2C8G/4C16G的组合列表
  - 存储容量 （10-8000）步长10 最大值与机器型号有关
- SQLServer
  - 地域
  - 购买时长 1个月
  - 购买数量
  - 类型（只有独享型）
  - zone(不暴露 查询未售空的接口)
  - 内存cpu 类似2C8G/4C16G的组合列表
  - 存储容量 （10-8000）步长10 最大值与机器型号有关
- MariaDB（无询价接口，提供了计价规则）
  - 地域
  - 购买时长 1个月
  - 购买数量
  - 内存大小 
  - 存储空间大小
- 相同参数
  - 地区（上海和香港）
  - 资源类型（MySQL SQLServer PostgreSQL MariaDB)
  - 实例规格 类似 类似2C8G/4C16G的列表
  - 存储容量（20-64000）步长10
  - 实例数量

- 阿里云RDS独有参数
  - 实例类型（主实例/只读实例；maria DB只有主实例）
  - 系列（集群版/高可用版/基础版）mariaDB只有高可用 SQL server只有基础版
  - 数据库版本 因为SQLServer的会影响价格

### 0421-0430
- 排查 域名采集是不是只采集A记录和CNAME的 
- SELECT SUM(cnt) FROM ( SELECT COUNT(*) AS cnt  FROM third_domain td   GROUP BY td.dns_value   HAVING COUNT(*) > 1) AS sub; 
- 集群新增ob_user_name属性
- alter table server_cluster_create_ticket_data add column ob_user_name varchar(128) not null default "";
- alter table store_cluster  add column ob_user_name varchar(128) not null default "";
- 再次整理腾讯云和阿里云常用主机
- {'ecs.c6.8xlarge': 99, 'ecs.c6.4xlarge': 35, 'ecs.c7.xlarge': 23, 'ecs.g6.8xlarge': 10, 'ecs.g7.8xlarge': 6, 'ecs.g6.4xlarge': 5, 'ecs.c7.8xlarge': 3, 'ecs.c6.large': 3, 'ecs.c6.2xlarge': 2, 'ecs.c8y.small': 2, 'ecs.g6.xlarge': 2, 'ecs.gn7i-c8g1.2xlarge': 2, 'ecs.c6.xlarge': 2, 'ecs.gn7i-c16g1.4xlarge': 1, 'ecs.s6-c1m2.small': 1, 'ecs.c7.large': 1, 'GN10Xp.2XLARGE40': 1, 'ecs.xn4.small': 1, 'ecs.g7.16xlarge': 1, 'ecs.g5.16xlarge': 1, 'ecs.c5.large': 1, 'ecs.s6-c1m1.small': 1}
- {'S5.LARGE8': 173, 'S5.4XLARGE32': 141, 'S6.8XLARGE64': 88, 'S5.2XLARGE16': 88, 'S5.8XLARGE64': 82, 'S5.MEDIUM4': 78, 'S6.LARGE8': 41, 'S5.4XLARGE64': 28, 'S4.LARGE8': 19, 'S5.LARGE16': 19, 'S5.2XLARGE32': 17, 'S4.4XLARGE32': 15, 'D2.4XLARGE64': 13, 'S6.2XLARGE16': 12, 'IT5.21XLARGE320': 11, 'S4.MEDIUM4': 11, 'S6.4XLARGE32': 10, 'S4.2XLARGE32': 10, 'IT3.8XLARGE128': 10, 'S3.MEDIUM4': 8, 'S5.MEDIUM2': 7, 'M5.LARGE32': 7, 'SA3.4XLARGE64': 6, 'S4.2XLARGE16': 6, 'IT5.16XLARGE256': 6, 'S5.8XLARGE128': 5, 'S4.LARGE16': 5, 'SA3.8XLARGE64': 4, 'S3.LARGE8': 4, 'S3.3XLARGE24': 3, 'SA2.4XLARGE64': 3, 'S5.MEDIUM8': 3, 'MA2.LARGE32': 3, 'IT5.8XLARGE128': 3, 'IT5.4XLARGE64': 3, 'S4.SMALL2': 3, 'M4.2XLARGE64': 3, 'S6.2XLARGE32': 2, 'SA3.4XLARGE32': 2, 'S3.2XLARGE16': 2, 'S5.SMALL2': 2, 'S3.MEDIUM8': 2, 'S6.MEDIUM4': 1, 'S4.SMALL1': 1, '实例规格': 1, 'ITA5.16XLARGE256': 1, 'GN7.2XLARGE32': 1, 'S5.16XLARGE256': 1, 'M6.31MEDIUM470': 1, 'GN10X.2XLARGE40': 1, 'S3.16XLARGE256': 1, 'S2.MEDIUM2': 1, 'S3.4XLARGE32': 1}
- 修改 集群管理图表页标识分配了集群却没有市场的门店
- 修改 云服务器接口改为异步加速
- 需求 云服务器region_id 修改为可变
- 整理实例对应的cpu内存
{'S4.2XLARGE32': '8C32G (S4.2XLARGE32)', 'S6.2XLARGE32': '8C32G (S6.2XLARGE32)', 'S5.MEDIUM8': '2C8G (S5.MEDIUM8)', 'MA2.LARGE32': '4C32G (MA2.LARGE32)', 'S5.8XLARGE64': '32C64G (S5.8XLARGE64)', 'S5.8XLARGE128': '32C128G (S5.8XLARGE128)', 'SA2.4XLARGE64': '16C64G (SA2.4XLARGE64)', 'S5.2XLARGE32': '8C32G (S5.2XLARGE32)', 'S5.MEDIUM2': '2C2G (S5.MEDIUM2)', 'S6.8XLARGE64': '32C64G (S6.8XLARGE64)', 'S5.SMALL2': '1C2G (S5.SMALL2)', 'ITA5.16XLARGE256': '64C256G (ITA5.16XLARGE256)', 'S4.4XLARGE32': '16C32G (S4.4XLARGE32)', 'IT5.21XLARGE320': '84C320G (IT5.21XLARGE320)', 'S4.MEDIUM4': '2C4G (S4.MEDIUM4)', 'GN10X.2XLARGE40': '8C40G (GN10X.2XLARGE40)', 'GN7.2XLARGE32': '8C32G (GN7.2XLARGE32)', 'S6.2XLARGE16': '8C16G (S6.2XLARGE16)', 'IT5.16XLARGE256': '64C256G (IT5.16XLARGE256)', 'IT5.8XLARGE128': '32C128G (IT5.8XLARGE128)', 'S3.2XLARGE16': '8C16G (S3.2XLARGE16)', 'S3.3XLARGE24': '12C24G (S3.3XLARGE24)', 'S3.MEDIUM4': '2C4G (S3.MEDIUM4)', 'S6.4XLARGE32': '16C32G (S6.4XLARGE32)', 'S6.MEDIUM4': '2C4G (S6.MEDIUM4)', 'S4.LARGE16': '4C16G (S4.LARGE16)', 'S3.4XLARGE32': '16C32G (S3.4XLARGE32)', 'GN10Xp.2XLARGE40': '10C40G (GN10Xp.2XLARGE40)', 'S3.MEDIUM8': '2C8G (S3.MEDIUM8)', 'S4.LARGE8': '4C8G (S4.LARGE8)', 'S5.MEDIUM4': '2C4G (S5.MEDIUM4)', 'S3.LARGE8': '4C8G (S3.LARGE8)', 'S5.4XLARGE64': '16C64G (S5.4XLARGE64)', 'M4.2XLARGE64': '8C64G (M4.2XLARGE64)', 'S5.4XLARGE32': '16C32G (S5.4XLARGE32)', 'S5.16XLARGE256': '64C256G (S5.16XLARGE256)', 'S4.2XLARGE16': '8C16G (S4.2XLARGE16)', 'S5.LARGE16': '4C16G (S5.LARGE16)', 'S5.LARGE8': '4C8G (S5.LARGE8)', 'S6.LARGE8': '4C8G (S6.LARGE8)', 'S3.16XLARGE256': '64C256G (S3.16XLARGE256)', 'SA3.4XLARGE32': '16C32G (SA3.4XLARGE32)', 'S4.SMALL2': '1C2G (S4.SMALL2)', 'M6.31MEDIUM470': '62C470G (M6.31MEDIUM470)', 'S2.MEDIUM2': '2C2G (S2.MEDIUM2)', 'SA3.4XLARGE64': '16C64G (SA3.4XLARGE64)', 'IT5.4XLARGE64': '16C64G (IT5.4XLARGE64)', 'S4.SMALL1': '1C1G (S4.SMALL1)', 'M5.LARGE32': '4C32G (M5.LARGE32)', 'S5.2XLARGE16': '8C16G (S5.2XLARGE16)', 'SA3.8XLARGE64': '32C64G (SA3.8XLARGE64)'}
{'ecs.c7.8xlarge': '32C64G (ecs.c7.8xlarge)', 'ecs.c7.large': '2C4G (ecs.c7.large)', 'ecs.c6.4xlarge': '16C32G (ecs.c6.4xlarge)', 'ecs.s6-c1m2.small': '1C2G (ecs.s6-c1m2.small)', 'ecs.s6-c1m1.small': '1C1G (ecs.s6-c1m1.small)', 'ecs.c7.xlarge': '4C8G (ecs.c7.xlarge)', 'ecs.c6.xlarge': '4C8G (ecs.c6.xlarge)', 'ecs.c6.8xlarge': '32C64G (ecs.c6.8xlarge)', 'ecs.c5.large': '2C4G (ecs.c5.large)', 'ecs.c6.large': '2C4G (ecs.c6.large)', 'ecs.g6.4xlarge': '16C64G (ecs.g6.4xlarge)', 'ecs.g5.16xlarge': '64C256G (ecs.g5.16xlarge)', 'ecs.c6.2xlarge': '8C16G (ecs.c6.2xlarge)', 'ecs.c8y.small': '1C2G (ecs.c8y.small)', 'ecs.g6.8xlarge': '32C128G (ecs.g6.8xlarge)', 'ecs.g7.8xlarge': '32C128G (ecs.g7.8xlarge)', 'ecs.gn7i-c16g1.4xlarge': '16C60G (ecs.gn7i-c16g1.4xlarge)', 'ecs.g6.xlarge': '4C16G (ecs.g6.xlarge)', 'ecs.gn7i-c8g1.2xlarge': '8C30G (ecs.gn7i-c8g1.2xlarge)', 'ecs.g7.16xlarge': '64C256G (ecs.g7.16xlarge)', 'ecs.xn4.small': '1C1G (ecs.xn4.small)'}
- 阿里
['16C32G (ecs.c6.4xlarge) 35', '16C60G (ecs.gn7i-c16g1.4xlarge) 1', '16C64G (ecs.g6.4xlarge) 5', '1C1G (ecs.s6-c1m1.small) 1', '1C1G (ecs.xn4.small) 1', '1C2G (ecs.c8y.small) 2', '1C2G (ecs.s6-c1m2.small) 1', '2C4G (ecs.c5.large) 1', '2C4G (ecs.c6.large) 3', '2C4G (ecs.c7.large) 1', '32C128G (ecs.g6.8xlarge) 10', '32C128G (ecs.g7.8xlarge) 6', '32C64G (ecs.c6.8xlarge) 99', '32C64G (ecs.c7.8xlarge) 3', '4C16G (ecs.g6.xlarge) 2', '4C8G (ecs.c6.xlarge) 2', '4C8G (ecs.c7.xlarge) 23', '64C256G (ecs.g5.16xlarge) 1', '64C256G (ecs.g7.16xlarge) 1', '8C16G (ecs.c6.2xlarge) 2', '8C30G (ecs.gn7i-c8g1.2xlarge) 2']
- 腾讯
['10C40G (GN10Xp.2XLARGE40) None', '12C24G (S3.3XLARGE24) 3', '16C32G (S3.4XLARGE32) 1', '16C32G (S4.4XLARGE32) 15', '16C32G (S5.4XLARGE32) 141', '16C32G (S6.4XLARGE32) 10', '16C32G (SA3.4XLARGE32) 2', '16C64G (IT5.4XLARGE64) 3', '16C64G (S5.4XLARGE64) 28', '16C64G (SA2.4XLARGE64) 3', '16C64G (SA3.4XLARGE64) 6', '1C1G (S4.SMALL1) 1', '1C2G (S4.SMALL2) 3', '1C2G (S5.SMALL2) 2', '2C2G (S2.MEDIUM2) 1', '2C2G (S5.MEDIUM2) 7', '2C4G (S3.MEDIUM4) 8', '2C4G (S4.MEDIUM4) 11', '2C4G (S5.MEDIUM4) 78', '2C4G (S6.MEDIUM4) 1', '2C8G (S3.MEDIUM8) 2', '2C8G (S5.MEDIUM8) 3', '32C128G (IT5.8XLARGE128) 3', '32C128G (S5.8XLARGE128) 5', '32C64G (S5.8XLARGE64) 82', '32C64G (S6.8XLARGE64) 88', '32C64G (SA3.8XLARGE64) 4', '4C16G (S4.LARGE16) 5', '4C16G (S5.LARGE16) 19', '4C32G (M5.LARGE32) 7', '4C32G (MA2.LARGE32) 3', '4C8G (S3.LARGE8) 4', '4C8G (S4.LARGE8) 19', '4C8G (S5.LARGE8) 173', '4C8G (S6.LARGE8) 41', '62C470G (M6.31MEDIUM470) 1', '64C256G (IT5.16XLARGE256) 6', '64C256G (ITA5.16XLARGE256) 1', '64C256G (S3.16XLARGE256) 1', '64C256G (S5.16XLARGE256) 1', '84C320G (IT5.21XLARGE320) 11', '8C16G (S3.2XLARGE16) 2', '8C16G (S4.2XLARGE16) 6', '8C16G (S5.2XLARGE16) 88', '8C16G (S6.2XLARGE16) 12', '8C32G (GN7.2XLARGE32) 1', '8C32G (S4.2XLARGE32) 10', '8C32G (S5.2XLARGE32) 17', '8C32G (S6.2XLARGE32) 2', '8C40G (GN10X.2XLARGE40) 1', '8C64G (M4.2XLARGE64) 3']
- 支持 rancher检查集群失败告警支持
- 需求 阿里云redis预估时需要将参数转为不同的实例规格id
- 需求 阿里云redis参数枚举
- 需求 prod环境：新增修改能选择范围[3+3,5+3,9+6];dev/ut/pt/sit/hd新增时能选择[3+3,5+3],修改时能选择[3+3,5+3]其中之前是9+6的话可以改成9+6，
### 0407-0420
- 修改 资源概览首页虚拟机维度修改，去掉office-vc
- 联调 云服务器询价
- 修改 修改云服务器数据结构
- 测试发现 云服务询价 某些实例规格不支持高效云盘 修复
- 测试发现 云服务询价 磁盘大小无效会请求失败 修复
- 测试发现 阿里云某些可用区可用实例类型 获取不准确导致请求失败 修复
- 测试发现 腾讯云image接口获取到的有重复的image，修复
- 修改 腾讯云接口不返回磁盘单价，了解磁盘定价规则并自定义计算
- 修改 向井伟要数据 云服务器镜像和实例规格，过滤不需要的类型
- 修改 资源定价新增时增加资源类型/环境/宿主环境/云/idc重复校验
- 修改 资源定价新增时增加资源字段小写和单位大写的校验
- 修改 费用预估 费用为0的不回显
- 需求 新增虚拟机概览接口
- 需求 Redis 采集/查询/单元测试
- 需求 LB费用预估
- 
- 修改 虚拟机采集解析逻辑虚拟机cloud_account为office-vc 将cloud映射为office 
- 修改 腾讯云磁盘价格计算逻辑 接口不反回磁盘单价 自定义
- 修改 网络设备缺失数据 修改网络设备解析逻辑适配云账户字段变更
- 支持 给iaas新建aws集群
- 修改 删除虚拟机data_center\machine_room字段 
- 修改 新增虚拟机、网络设备、项目、域名同步脚本
- 修改 格式化项目标签字符串
- 整理和讨论 从cmp上拉取负载均衡往期数据 编写脚本进行数据清洗和分析 整理出价格分布的图表

### 问题记录
- 检查生产门店分配集群的数据
- 更换wukong chardet包为支持许可证的开源软件
- 处理puppet配置修改工单申请权限的bug

- 项目表字段清洗，去掉多余的字符 
- 如果有异常的事务未回滚，会影响别的请求吗

### 0324
- 费用预估 所有人
- 审计日志查看- idc只能看idc的 cloud看clound
- 定价策略 修改 infra-admin 查看rts
- 
- sqlalchemy 有失败时，影响范围有哪些 本会话，其他会话 mysql客户端 如果时本会话，本会话的什么操作会影响
```
riase exception_a from exception_b

db.bulk_save_objects(all_data)
 File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\pymysql\err.py", line 150, in raise_mysql_exception
    raise errorclass(errno, errval)
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1364, "Field 'id' doesn't have a default value")
db.query(VirtualMachine).count()
File "c:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-cmdbserv\lib\site-packages\sqlalchemy\orm\session.py", line 973, in _raise_for_prerequisite_state
    raise sa_exc.PendingRollbackError(
sqlalchemy.exc.PendingRollbackError: This Session's transaction has been rolled back due to a previous exception during flush. To begin a new transaction with this Session, first issue Session.rollback(). Original exception was: (pymysql.err.OperationalError) (1364, "Field 'id' doesn't have a default value")
```
### 0319
- 区域default变换值
### 0317
- office-vc归到hedan还是putuo
- onecloud 归到哪里呢
### 0314
- clound为空的字段怎么办
- start_fail running ready unknown
### 0313
  #842323 - 

rgb(0, 214, 65)
rgb(26, 164, 72)
rgb(14, 111, 47)
rgb(8, 84, 33)
i5-8300h 7408
i7-8750H 9854
i5-6300U 3222
i5-9300H 7529
i7-9750H 10750
i5-10200H 8028



### 0307
1. cluster新增编辑里没有新增标签 修改里没有删除标签  表头k8s_ip里不对


1. 补偿dev环境集群改为生产导致的未校验属性
2. 修改用户填写错误的集群属性
3. 
### 0305
- ip校验 最后一个,号分割
- 校验失败提示
- market改成只能是一个维度的

- domain的数据放到clound_account 
- resource_id删去
- 把tags里的数据再拿出来
- domain、group_count、user_count/description/mcd_project/clound/cloud_subscription/resource_uid


- 虚拟机取得时候不包括调度失败的

### 0304
- 修改表结构
alter table server_cluster_create_ticket_data add column k8s_ip varchar(128) not null default ""  comment "k8s ip", 
add column ob_ip varchar(128) not null default ""  comment "ob ip",
add column ob_vip varchar(128) not null default ""  comment "ob vip";

alter table store_cluster add column k8s_ip varchar(128) not null default ""  comment "k8s ip", 
add column ob_ip varchar(128) not null default ""  comment "ob ip",
add column ob_vip varchar(128) not null default ""  comment "ob vip";
### 0221
- 加data_center 和机房room
- cloud_account 为空
- hd pt tengxun ali store office 
- 网络设备
- cloud_manager -> cloud_subscription
- cloud
- cloud_account
- data_center
- 
### 0219
- cpu_count -> cpu
- os_type - > os_version
- image 删去
- 宿主机 取名字
- 二层网络和ip子网关联 删去
- auto_start 删除
- external_ip -> eip
- owner不要
- created_by update_by 删去


- 平台字段内容换一下 换成hd pto ali tengxun
- 安全组 null 去掉；改成名字
- vpc 不要 换成ip子网
- 
- resource_id -> 云上id

# 网络设备
- 加date_center数据中心 putuo、hedan
- 
- 加一个字段放房间信息

### 0217
- 看puppet子流程发布申请人权限问题
- 改使用率校验
  - 是校验新机器放进去后集群的使用率，但是挪到第一步的时候这个机器还没有真正放进去，因为后面工单可能会审批决绝，而且有可能同时有多个工单都分配的这个集群
- 改堡垒机跳转

### 0214 Q!@34mcd  Q!@34mcn
- 修改模型定义
- 沟通根据集群查询门店接口信息
- 堡垒机授权问题
cn-wukong-rstorets05-edge01.mcd.store
### puppet配置修改流程发布回滚
- 尽量不要回滚
- 回滚后这个工单就不能继续发布了，只能回滚完全部已发布的子流程并取消工单
- 当工单回滚后，在下次工单提交前要同步各分支，否则在下次合并的时候会发生从冲突
```cs
回滚的顺序：
从临时分支合并到了uat
从uat合并到了production
从production合并到了第一批的分支（zone01 zone02 zone03 zone04) 
假如此时发现需要回滚
第一批分支回滚production合过来的merge
production回滚uat合过来的merge
uat回滚临时分支合过来的merge
点击取消工单
然后需要提一个uat到production分支的merge request用来将uat上的revert记录同步到production
提一个production到zone01分支的merge request用来将uat和production上的revert记录同步到zone01
提一个production到zone02分支的merge request用来将uat和production上的revert记录同步到zone01
...
提一个production到zone04分支的merge request用来将uat和production上的revert记录同步到zone01

然后再提交新的puppet配置修改工单
....

```
### 0212
- production上的合并请求revert不了
```shell
# 回滚production 没操作
git checkout production
git pull
git revert 65d706267 9bb9ba15
git push

# 回滚uat的改动
git checkout uat
git pull 
git revert 3d7883
git push

# 将production合并到了uat
# 又将uat合并到了production
```
### 0211
- 版本发布
- 模型设计
- 根据集群查询门店接口文档
- puppet问题排查
- https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/merge_requests?scope=all&utf8=%E2%9C%93&state=all
- puppetfile 提交历史https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/commits/production/Puppetfile
- puppet 文件内容 https://gitlab-ex.mcd.com.cn/infra/wukong-iaas/puppet-control/blob/uat/Puppetfile
- 392
- Merge newbranch392 into uat 267 
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
- Merge uat into production 266
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'

- 393
- Merge newbranch393 into uat 268
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- Merge uat into production 269 closed 2025-02-11 17:17:40
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d' uat是403d
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- Merge uat into production -- 271
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- 当前合并冲突 Merge uat into production 276
  :commit => '09977aff00d6413b5f20ba9ff92dbde80b1bd00a' ours 3d7883c4 
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5' theirs

- uat 提交
- 3d7883c4 yanyan 
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
  :commit => '09977aff00d6413b5f20ba9ff92dbde80b1bd00a'
- 4df57e0e infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'

- production提交
- 65d70626 yanyan
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- 4df57e0e infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => '2c2fd9a0f64db5fb0925002be7cbf987f3ca1fbc'
- ac55e8dc Revert "Merge branch 'newbranch392' into 'uat'"
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- a590733c Revert "Merge branch 'uat' into 'production'"
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
- c4179cfe infra update Puppetfile
  :commit => '60eb34be6d5744f5bb7d60579e934285908e00c5'
  :commit => 'c50264f4f5a75e39d31414b8bc319a84b85e403d'

- 
- 为什么合并又回滚的内容再次合并到uat能成功，而合并到production就不成功，是因为到uat的merge_request是一个新分支提的，而到production的还是uat

- merge request 268合并成功 回滚失败
问题原因 是因为从!269可以看到uat中内容和prod内容不一致，因为prod回滚分支后，uat未和prod同步
### 0210
- hedan puduo 
- 


### 0122
- 数据中心一致
- 生产环境才校验编号，其他不校验


### 0115
1. 集群容量预警逻辑修改
2. 集群使用率计算需适配不同容量
3. 集群查询时使用率过滤逻辑修改
4. 由于需要获取store_count 需要把之前表中的store_count删除
5. 首页集群查询加上分页
```sql
-- 修改store_cluster
ALTER TABLE store_cluster DROP COLUMN store_count, drop column market_count, drop column do_count, drop column utilization;
-- 修改store_cluster
alter table store_cluster add column sku varchar(24) not null default "" comment "集群sku";
alter table store_cluster add column rancher_cluster_id varchar(100) not null default "" comment "rancher集群id";
-- 修改server_cluster_create_ticket_data
alter table server_cluster_create_ticket_data add column sku varchar(24) not null default "" comment "集群sku";
alter table server_cluster_create_ticket_data add column rancher_cluster_id varchar(100) not null default "" comment "rancher集群id";
```
### 0106
- 那个设备，了解在网络边界中处于那个位置
- 申请人有几个 5 个
- 可以把操作人加到消息通知里
- dev 没有标签 删除集群的数据，只保留1个
- 改成中文

ingress_ip DTO store_cluster ticket里
env = fields.String(required=True, 
                    validate=validate.OneOf(["sit", "uat", "pt", "prod"]),
                    error='env可选值为["sit", "uat", "pt", "prod"]')

### 0103
- 修改acl 
alter table acl_rule modify source_port varchar(512) not null comment '源cidr port',  modify dest_port varchar(512) not null comment '目标cidr port';

-- 修改server_config_release_ticket_data
alter table server_config_release_ticket_data add column op_users varchar(256) not null default "" comment "可操作发布回滚的用户";
-- 修改AccessRecordData中user_account 为 nickname
alter table access_record_data change user_account nickname varchar(64) NOT NULL COMMENT '访问用户账号';
alter table access_record_data change user_name username varchar(64) NOT NULL COMMENT '访问用户名';

-- 修改ip字段
alter table store_cluster add column ingress_ip varchar(25) not null default "" comment "ip信息";
alter table server_cluster_create_ticket_data change ip ingress_ip varchar(25) not null default "" comment "ip信息";


1
411024199504278567 18737329773
411024199801290765 13963966532
411024199801290765 18237497786
411024199801290765 
3
411024199801290765 15290618188
411024199801290765 15290618188
411024199801290765 18237497786
411024199801290765 15290618188
411024199801290765 15290618188



### 0102
- 有些规则的protocol解析成了source
- 需要将反掩码转换成正掩码
- 有的协议还没有算出来
### 1225
- DNS自动化配置新建申请 -> WuKong CaseA集群申请DNS-{集群名称}
- cluster id 排序
- celery 消息补偿

### 120
提示词工程  编排 工作流
- alter table server_cluster_create_ticket_data add column domain varchar(100) not null default "";


### 1219
- 修改数据库
```sql
alter table store_cluster add tags json comment "标签信息";
alter table store_cluster change gateway domain varchar(100);

alter table server_cluster_create_ticket_data drop column gateway;
alter table server_cluster_create_ticket_data add column data_center varchar(32) not null default "" comment "机房中心" after env;
alter table server_cluster_create_ticket_data add tags json comment "标签信息" after domain;
```
### 1205
- 申请人也会修改吗
修改查询集群接口结果为倒序
- 修改集群 生产对应生产、uat/dev 随便选
- 返回dns检查信息
- 集群日期查询过滤
- 添加集群后添加集群表
- 图表中空数据怎么办
### 1203
- 版本上线 
  - 添加case a 外部接口token
- 修改数据库
```sql
-- 新增集群流程 注意更新id
INSERT INTO wukong_iaas.approval_processes
(id, created_at, updated_at, is_deleted, process_name)
VALUES(9, '2024-11-07 13:23:22', '2024-11-07 15:34:52', 0, 'CASE_A集群修改流程');
INSERT INTO wukong_iaas.approval_processes
(id, created_at, updated_at, is_deleted, process_name)
VALUES(10, '2024-12-06 14:40:43', '2024-12-06 14:40:43', 0, '创建集群流程');


INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(49, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '用户填写信息', 0, 1, 'CASE_A集群修改流程第一步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(50, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, 'infra审批', 0, 2, 'CASE_A集群修改流程第二步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(51, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '执行变更', 0, 3, 'CASE_A集群修改流程第三步');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(52, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '完成', 0, 4, 'CASE_A集群修改流程完成');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(58, '2024-11-15 14:35:24', '2024-11-15 14:35:24', 0, 9, '已取消', 0, -1, 'CASE_A集群修改流程取消');

INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(53, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '已取消', 0, -1, '已取消');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(54, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '用户提交信息', 0, 1, '工单提交');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(55, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, 'Infra审批', 0, 2, 'Infra审批');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(56, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, 'DNS生效中', 0, 3, 'DNS生效中');
INSERT INTO wukong_iaas.approval_process_nodes
(id, created_at, updated_at, is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES(57, '2024-12-06 14:41:25', '2024-12-06 14:41:25', 0, 10, '完成', 0, 4, '完成');

-- wukong_iaas.server_cluster_create_ticket_data definition

-- wukong_iaas.server_cluster_create_ticket_data definition

CREATE TABLE `server_cluster_create_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `cluster_name` varchar(100) NOT NULL COMMENT 'cluster name',
  `env` varchar(24) NOT NULL COMMENT 'cluster env',
  `gateway` varchar(100) NOT NULL COMMENT '网关信息',
  `ip` varchar(25) NOT NULL COMMENT 'ip信息',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `domain` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
)COMMENT '新建集群工单详情';

--
alter table store_info add column cluster_id int NOT NULL default '-1' after store_id, add index idx_cluster_id (cluster_id);
alter table store_info add column do_name varchar(64) NOT NULL default '' after market_city_name_cn;
alter table store_info add column ownership varchar(32) NOT NULL default '' after do_name;

-- wukong_iaas.store_cluster definition

CREATE TABLE `store_cluster` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `cluster_name` varchar(100) NOT NULL COMMENT 'cluster name',
  `env` varchar(24) NOT NULL COMMENT 'cluster env',
  `store_count` int NOT NULL COMMENT '门店数量',
  `market_count` int NOT NULL COMMENT '市场数量',
  `do_count` int NOT NULL COMMENT 'DO数量',
  `utilization` float NOT NULL COMMENT '集群使用率',
  `gateway` varchar(100) NOT NULL COMMENT '网关信息',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`)
) COMMENT '集群信息';

-- wanglin
ALTER TABLE server_foreman ADD COLUMN model VARCHAR(100) DEFAULT '' COMMENT 'model_name';
ALTER TABLE store_info ADD COLUMN node_num INT NOT NULL DEFAULT 0 COMMENT '节点数量';
ALTER TABLE store_apply_ticket_data ADD COLUMN node_num INT NOT NULL DEFAULT 0 COMMENT '节点数量';
ALTER TABLE store_apply_ticket_data ADD COLUMN store_cluster VARCHAR(100) DEFAULT ''COMMENT '门店所属集群';
ALTER TABLE store_info ADD COLUMN in_process  tinyint NOT NULL DEFAULT '0' COMMENT '是否在流程中';

插入流程
INSERT INTO wukong_iaas.approval_processes
(id,  is_deleted, process_name)
VALUES(9,  0, 'CASE_A集群修改流程');

INSERT INTO wukong_iaas.approval_process_nodes
(is_deleted, process_id, node_name, approval_role, node_order, node_description)
VALUES (0, 9, '用户填写信息', 0, 1, 'CASE_A集群修改流程第一步')
VALUES (0, 9, 'infra审批', 0, 2, 'CASE_A集群修改流程第二步')
VALUES(0, 9, '执行变更', 0, 3, 'CASE_A集群修改流程第三步')
VALUES(0, 9, '完成', 0, 4, 'CASE_A集群修改流程完成')
VALUES(0, 9, '已取消', 0, -1, 'CASE_A集群修改流程取消');


CREATE TABLE change_cluster_ticket_data (
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    is_deleted INT NOT NULL DEFAULT '0' COMMENT '是否删除',
    id BIGINT NOT NULL AUTO_INCREMENT COMMENT 'id',
    ticket_id INT NOT NULL COMMENT '关联的工单id',
    store_id VARCHAR(256) NOT NULL COMMENT '门店id',
    store_name_cn VARCHAR(256) NOT NULL COMMENT '门店中文名',
    group_name VARCHAR(128) NOT NULL COMMENT 'group',
    node_num INT NOT NULL DEFAULT '0' COMMENT '节点数',
    cluster_id INT NOT NULL COMMENT '集群id',
    cluster_name VARCHAR(128) NOT NULL COMMENT '集群名字',
    province_name VARCHAR(128) NOT NULL COMMENT 'gis info 省',
    market_city_name_cn VARCHAR(128) NOT NULL COMMENT 'gis info 市场名',
    do_name VARCHAR(64) NOT NULL DEFAULT '' COMMENT 'do姓名',
    ownership VARCHAR(32) NOT NULL DEFAULT '' COMMENT '所有权',
    open_status VARCHAR(50) NOT NULL COMMENT 'gis info 市场名', 
    change_cluster_id INT NOT NULL COMMENT '改变的集群id',
    change_cluster_name VARCHAR(100) NOT NULL COMMENT '改变的集群名字',
    PRIMARY KEY (id)
) COMMENT='Store Change Cluster Ticket Data';
```
### 1020
- dev uat 手动填 prod自动分配 
- 512 算占用率 可以大于100% 
- 大于80% 发消息提醒 4000 1100 cl x00 
- 
- do分散
- 一个集群保证有两个市场
- 一个集群里直营、dl、cl是有比例的

- 分配逻辑
- 集群展示功能 查询可以先不做 新建流程也先不做
- 门店管理筛选功能先不做 展示功能先做
- 查询有哪些集群、 集群内有哪些门店、门店在哪个集群
- 门店申请流程里的可以先不上
- puppet发布批次里没有门店增加一行没有门店信息
- 消息通知里流程名改成发布计划名称
- 修改f5返回
- 1节点域名信息要在申请门店第一步就展示吗？
```json

				"id": 3392, 1
				"name": "ITO-2117", 1
				"destination": ":443", 
				"partition": "VRF_Test",
				"full_path": "/VRF_Test/ITO-2117",
				"virtual_ip": "10.126.152.21",
				"route_domain": "1",
				"servers_port": "443",
				"ip_protocol": "tcp",
				"source": "0.0.0.0%1/0",
				"last_modifiedTime": "",
				"enabled": "1",
				"master": "hedan-F5/NDC-Test-LB01/172.18.129.252",
				"pool_name": "tob_sit_443",
				"pool_full_path": "/VRF_Test/tob_sit_443",
				"pool_monitor": "/Common/tcp",
				"created_at": "2024-11-05T14:30:49",
				"updated_at": "2024-11-05T14:30:49",
				"pools": [
					{
						"id": 27817,
						"name": "10.126.156.165:30443",
						"partition": "VRF_Test",
						"fullPath": "/VRF_Test/10.126.156.165:30443",
						"monitor": "default",
						"address": "10.126.156.165%1",
						"ip_addr": "10.126.156.165",
						"port": "30443",
						"master": "hedan-F5/NDC-Test-LB01/172.18.129.252",
						"pool_full_path": "/VRF_Test/tob_sit_443"
					},

```

### 1113
https://ninja-dev.mcdchina.net/api/stores?page=1&page_size=50
https://ninja-dev.mcdchina.net/iaas_swagger
![alt text](imgs/go_work.image.png
- 但用这样的连接这样才能访问：https://boss.dev.mcdonalds.cn/api/inner/devops/devops-wukongiaasserv/api/inner/devops/devops-wukongiaasserv/iaas_swagger/index.css
```
CREATE TABLE `msg_notice` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `msg` text NOT NULL COMMENT '消息详情',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`)
) ;
```
### 1108
```py
'ip_addr':virtual_ip, # 可以用原来的virtualip代替 = f5_vip_pool.virtual_ip
'file_name':file_name,  #  可以用原来的代替 = f5_vip_pool.master
'port':port,   # 可以用原来的代替 = f5_vip_pool.server_port
'pools':pools, 对应的f5_node里的ip和port
'account':FILE_ENV_MAP.get(file_name,'')
```
- 数据的处理使用fastapi内置的方法
- port 是从 destination 里解析出来的，新数据没有该字段 可以用lbconfig中的port代替，部分时一样的可能时更新的日期不一样导致的
- 缺少pool表（一对多）缺少member_ip和member_port
### 1106
- 修改审计日志获取信息逻辑
- 将user信息放到g对象中 发现有些用户在user中不存在 继续修改
- 处理大小写
- puppet流程增加权限校验
- 修改审计日志解析用户信息逻辑
- 修改puppet发布子流程企微通知样式 修复门店重复
- 
### 1104
```sql
-- 审计日志新增表
CREATE TABLE `access_record_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `opt_module` varchar(64) NOT NULL COMMENT '操作模块',
  `opt_type` tinyint NOT NULL DEFAULT '0' COMMENT '请求类型',
  `opt_desc` varchar(256) NOT NULL COMMENT '操作描述',
  `opt_module_path` varchar(128) NOT NULL COMMENT '方法路径',
  `url` varchar(256) NOT NULL COMMENT '请求url',
  `ip` varchar(15) NOT NULL COMMENT '请求url',
  `require_args` text NOT NULL COMMENT '请求参数',
  `res_code` int NOT NULL COMMENT '返回状态码',
  `res_msg` varchar(256) NOT NULL COMMENT '返回信息',
  `res_body` text NOT NULL COMMENT '返回data',
  `user_name` varchar(64) NOT NULL COMMENT '访问用户名',
  `user_account` varchar(64) NOT NULL COMMENT '访问用户账号',
  PRIMARY KEY (`id`)
)COMMENT '审计日志数据';
-- 修改server_config_release_data
ALTER TABLE server_config_release_data modify batch_res text NOT NULL Default "" Comment "发布详情";
ALTER TABLE server_config_release_data modify merge_id varchar(256) NOT NULL Default "" Comment "合并iid";
-- wanglin
ALTER TABLE server_state ADD COLUMN out_band_ip  VARCHAR(20) NOT NULL DEFAULT '' COMMENT '带外ip';
```
### 1030
- 代理ip不准、操作人不准ok、操作类型换成请求方式ok、操作名称 ok
- 分页 排序是倒序 ok
- 重置报错 ok
- 分页报错
- 回滚完不能再次发布把发布按钮置灰
- 流程完成 取消 按钮灰色 
- 加日志 ok
- uat发布失败的不能是已回滚

```py
def test(self, branch_name):
    code, msg, data = self.puppet_service.merge_branch_service(branch_name, "uat")
    if not data:
        logger.error("{source_branch}发布失败: " + msg.strip())
        return "第一次发布失败"
    else:
        merge_id = data["merge_request_id"]
    code, msg, res = self.puppet_service.rollback_branch_service(int(merge_id))
    code, msg, data = self.puppet_service.merge_branch_service(branch_name, "uat")
    if not data:
        logger.error("{source_branch}发布失败: " + msg.strip())
        return "{source_branch}发布失败: " + msg.strip()
    return "success"
```

### 1025
将每个mergid分别放到回滚任务队列中；将状态改为回滚中，返回
任务逻辑：如果回滚失败，写入msg和mergeid到表 回滚成功，将msg回写
如何识别回滚部分失败和全部失败呢，此函数只注册一个任务、由这个任务里去循环调用回滚任务，每个任务执行完后将结果写回表，这样前端页面就可以实时刷新
所有任务完成后，判断批次的结果

### 1023
- 修改server_config_change_data
- 需要安装jwt
```sql
-- wukong_iaas.server_config_release_data definition
ALTER TABLE server_config_release_data modify batch_res text NOT NULL Default "" Comment "发布详情";
ALTER TABLE server_config_release_data modify merge_id varchar(256) NOT NULL Default "" Comment "合并iid";

```
### 1021
- 首页增加一个工单状态(ticket_status)，现在状态改为发布状态(release_status) ok
- 新建申请页面和审批页面修改批次时会报错，获取到的内容直接填到输入框里，批次内容不包括uat和dev（我会在接口里去掉这两个） ok
- 编辑分批的时候将批次1的内容删除后不在其他批次的可选框中 ok
- 发布计划名称和变更内容左对齐，其他列居中 
- 发布页面详情默认不展开 ok
- 发布步骤中需要判断是否可以取消（后端会加）必须要把临时分支删除掉 ok

- 未修改不能提交 ok
- 修改详情接口优化 
- 校验完模板后如果再次修改文件就不用校验了
- 取消里都要加入删除分支 ok
- 发布时判断发布时间过期 ok
- 时间判断大于一个小时 ok
- 分批不包括uat dev ok
- infra审批页面编辑 ok
- 配置详情 
- 首页排序从大到小 ok
- 修改详情美化
- 合并从prod合并到第一批，第二批 ok
- 加一个弹窗显示分批的信息，里面有该批是zone几 ok
- 发布详情换行 ok
- 改成异步
- ALTER TABLE server_config_release_ticket_data MODIFY COLUMN branch_name VARCHAR(32) DEFAULT '';
- ALTER TABLE server_config_release_ticket_data MODIFY COLUMN first_commit VARCHAR(32) DEFAULT '';
- ALTER TABLE server_config_release_data MODIFY COLUMN batch_res VARCHAR(512);
### 1008
```sql
# store_server_ticket_data 新增role puppet_status两列
alter table store_server_ticket_data add role varchar(50) not null default "" after ticket_id,add puppet_status  varchar(50) not null default ""  after role;
INSERT INTO approval_processes  (process_name)  VALUES('Puppet证书删除流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '完成', 0, 4, '工单完成');

INSERT INTO approval_processes  (process_name)  VALUES('Group修改流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '完成', 0, 4, '工单完成');

INSERT INTO approval_processes  (process_name)  VALUES('新建发布流程');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '修改配置', 0, 2, '修改配置');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, 'infra审批', 0, 3, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '发布配置', 0, 4, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '完成', 0, 5, '工单完成');
```
# 新增change_server_group_ticket_data存储修改group工单数据
```sql
-- wukong_iaas.change_server_group_ticket_data definition

CREATE TABLE `change_server_group_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `dn` varchar(120) NOT NULL COMMENT 'LDAP的DN',
  `store_id` varchar(256) NOT NULL COMMENT '门店id',
  `env` varchar(50) NOT NULL COMMENT 'env',
  `store_name` varchar(256) NOT NULL COMMENT '门店中文名',
  `hostname` varchar(256) NOT NULL COMMENT 'hostname',
  `ip_addr` varchar(128) NOT NULL COMMENT 'ip_addr',
  `group` varchar(128) NOT NULL,
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `role` varchar(50) NOT NULL COMMENT 'role',
  `puppet_status` varchar(50) NOT NULL COMMENT 'puppet status',
  `new_group` varchar(128) NOT NULL COMMENT '要修改的group',
  PRIMARY KEY (`id`),
  KEY `idx_group` (`group`),
  KEY `idx_dn` (`dn`)
);
```
新增server_config_release_ticket_data存储puppet发布流程数据
```sql
-- wukong_iaas.server_config_release_ticket_data definition

CREATE TABLE `server_config_release_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `title` varchar(256) NOT NULL COMMENT '发布流程标题',
  `batch_num` int NOT NULL COMMENT '分批次数',
  `batch_detail` varchar(512) NOT NULL COMMENT '发布批次详情',
  `user_name` varchar(64) NOT NULL COMMENT '申请用户名',
  `change_desc` varchar(256) NOT NULL COMMENT '修改内容描述',
  `plan_time_l` timestamp NOT NULL COMMENT '计划开始时间',
  `plan_time_r` timestamp NOT NULL COMMENT '计划结束时间',
  `branch_name` varchar(32) NOT NULL,
  `first_commit` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
);
```

# 新增server_config_release_data存储puppet发布子流程数据
```sql
-- wukong_iaas.server_config_release_data definition

CREATE TABLE `server_config_release_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `is_activate` tinyint NOT NULL DEFAULT '0' COMMENT '是否是当前子流程',
  `batch_res` varchar(256) NOT NULL COMMENT '发布详情',
  `merge_id` varchar(64) NOT NULL COMMENT '发布详情',
  `batch_name` varchar(32) NOT NULL COMMENT '批次名',
  `batch_order` tinyint NOT NULL COMMENT '批次顺序',
  `batch_status` tinyint NOT NULL COMMENT '当前批次状态0待发布、1发布中、2发布失败、3发布成功、4回滚中、5回滚失败',
  PRIMARY KEY (`id`)
);
``` 
### 0928
```py
@ticket_bp.route("/test", methods=["GET"])
def test():
    """
    获取修改详情
    :return:
    """
    try:
        data = {
            "process_name": SERVER_PUPPET_SSL_DELETE_PROCESSNAME,
            "desc": "xxxxx-desc",
            "env": "dev",
            "ticket_id": 49
        }
        send_msg2qw(**data)
        ticket_service = TicketService()
        res = ticket_service.is_server_config_process()
        return create_response(200, "ok", data={})
    except Exception as e:
        return create_response(500, str(e), {})
```
### 0919
- 重新编译python
- 编译报错，Could not import runpy module 升级gcc
### 0903
- 删除puppet流程
- 修改server信息的流程
  - 点击某条信息旁边的修改，进入新页面，展示对改server信息的查询结果，数据库中不做任何修改
  - 门店Server信息修改页面：如果点击取消，数据库中也没有任何修改；点击确定，tickiet中插入一条，current为2，同时server_state表中in_process状态为1，把工单数据插入到store_server_ticket_data中
  - 审批页面点击取消：数据库中没有任何修改；点击拒绝，tickiet中current变为-1，同时server_state表中in_process变为0；点击同意，current变为4同时server_state表中in_process变为0
- 执行结果去哪里获取呢？
- group分区中审批角色
### 0822
- k8s相关表加上属性后，假如查询表Ingress，那么结果中可能有该匹配条件的多行，那么需要根据版本进行去重
- 如果某行没有最新版本的数据呢？要展示老数据吗？

### 1008
```sql
store_server_ticket_data 新增role puppet_status两列
# alter table store_server_ticket_data add role varchar(50) not null default "" after ticket_id,add puppet_status  varchar(50) not null default ""  after role;
# INSERT INTO approval_processes  (process_name)  VALUES('Puppet证书删除流程');

INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, 'infra审批', 0, 2, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '工单执行', 0, 3, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(5, '完成', 0, 4, '工单完成');

# INSERT INTO approval_processes  (process_name)  VALUES('Group修改流程');

# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '已删除', 0, -1, '申请取消');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '用户提交信息', 0, 1, '工单提交');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, 'infra审批', 0, 2, '工单审批');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '工单执行', 0, 3, '工单执行');
# INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(6, '完成', 0, 4, '工单完成');

# INSERT INTO approval_processes  (process_name)  VALUES('新建发布流程');
# 
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '已删除', 0, -1, '申请取消');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '用户提交信息', 0, 1, '工单提交');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '修改配置', 0, 2, '修改配置');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, 'infra审批', 0, 3, '工单审批');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '发布配置', 0, 4, '工单执行');
INSERT INTO approval_process_nodes  (process_id, node_name, approval_role, node_order, node_description)  VALUES(7, '完成', 0, 5, '工单完成');
```
# 新增change_server_group_ticket_data存储修改group工单数据
```sql
-- wukong_iaas.change_server_group_ticket_data definition

CREATE TABLE `change_server_group_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `dn` varchar(120) NOT NULL COMMENT 'LDAP的DN',
  `store_id` varchar(256) NOT NULL COMMENT '门店id',
  `env` varchar(50) NOT NULL COMMENT 'env',
  `store_name` varchar(256) NOT NULL COMMENT '门店中文名',
  `hostname` varchar(256) NOT NULL COMMENT 'hostname',
  `ip_addr` varchar(128) NOT NULL COMMENT 'ip_addr',
  `group` varchar(128) NOT NULL,
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `role` varchar(50) NOT NULL COMMENT 'role',
  `puppet_status` varchar(50) NOT NULL COMMENT 'puppet status',
  `new_group` varchar(128) NOT NULL COMMENT '要修改的group',
  PRIMARY KEY (`id`),
  KEY `idx_group` (`group`),
  KEY `idx_dn` (`dn`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
```
新增server_config_release_ticket_data存储puppet发布流程数据
```sql
-- wukong_iaas.server_config_release_ticket_data definition

CREATE TABLE `server_config_release_ticket_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `title` varchar(256) NOT NULL COMMENT '发布流程标题',
  `batch_num` int NOT NULL COMMENT '分批次数',
  `batch_detail` varchar(512) NOT NULL COMMENT '发布批次详情',
  `user_name` varchar(64) NOT NULL COMMENT '申请用户名',
  `change_desc` varchar(256) NOT NULL COMMENT '修改内容描述',
  `plan_time_l` timestamp NOT NULL COMMENT '计划开始时间',
  `plan_time_r` timestamp NOT NULL COMMENT '计划结束时间',
  `branch_name` varchar(32) NOT NULL,
  `first_commit` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
```
新增server_config_release_data存储puppet发布子流程数据
```sql
-- wukong_iaas.server_config_release_data definition

CREATE TABLE `server_config_release_data` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除',
  `ticket_id` int NOT NULL COMMENT '关联的工单id',
  `is_activate` tinyint NOT NULL DEFAULT '0' COMMENT '是否是当前子流程',
  `batch_res` varchar(256) NOT NULL COMMENT '发布详情',
  `merge_id` varchar(64) NOT NULL COMMENT '发布详情',
  `batch_name` varchar(32) NOT NULL COMMENT '批次名',
  `batch_order` tinyint NOT NULL COMMENT '批次顺序',
  `batch_status` tinyint NOT NULL COMMENT '当前批次状态0待发布、1发布中、2发布失败、3发布成功',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
```
