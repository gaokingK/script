# 网络问题
- 麒麟、uos、网络切换自动化有问题（卡、命令无效）
- 打通有线和无线
- 从执行机下发到被测环境
- 应用可以自己设置不让截图
当前自动化测试任务依赖于CIDA，失败用例的分析结果及发现的问题没有平台去承载；和开发对问题时也必须让这个用例的分析者去描述。后续希望进行改进，把人工分析的自动化用例失败原因等有价值的信息结果放在平台上，使问题能被记录下来。

# ovs
- link:
    - http://platformdoc.huawei.com/hedex/hdx.do?v=01%20(2018-07-25)&lib=159779275&homepage=resources/hedex-homepage.html&productId=2708
    - http://www.openvswitch.org/
- Open Vswitch(ovs)是一个虚拟交换机开源实现，它旨在支持标准管理接口和协议的同时，通过编程扩展来实现大规模网络自动化；并且也关注跨多个物理服务器分发数据。
- 基于业务对其做了一些扩展，要测试这些扩展的健壮性
- OpenVswitch守护进程在运行时接收某种命令控制他们的行为和查询他们的设置。ovs-appctl程序提供了一种简单方式调用这些命令。
- ovs-dpctl可以创建、修改和删除OpenVswitch的datapath
- ovs-ofctl命令行可以用来监视和控制OpenFlow交换机
```
ovs-ofctl show 打印交换机的信息包括流表和端口。
ovs-ofctl dump-desc 打印网桥的描述信息。
ovs-ofctl dump-tables 打印交换机使用所有流表的状态。
ovs-ofctl dump-table-features 打印交换机使用所有流表的功能。
```
- ovs-vsctl通过高层次的抽象接口对ovs-vswitchd的数据库进行配置
# 
- 主要有虚拟机管理，docker管理、日志管理、需求管理、里程碑管理、用户管理和组织管理
- 参与二期flask框架设计，统一代码编写风格
- 编写接口文档，功能文档，表设计文档
- 编写sqlalchemy通用添加，删除，更新，查询接口
- 分析docker整改内容，制定实际实施方案并进行编码整改。
- docker部分，实现添加，批量添加，删除，批量删除，更新，查询，模板下载等接口。

# 
- 适配lkp-tests框架支持对docker的测试
# pc
- 实验室蓝区数据平台，聚合蓝区测试中产生的价值数据
- 容纳自动化测试任务
- 接入视频检测，实现视频任务一键下发，后台异步检测、分析、结果看板

# 
- 测试结果不收敛或有疑问，进一步测试