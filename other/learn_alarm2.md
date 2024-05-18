snmp
简单网络管理协议（SNMP），由一组网络管理的标准组成，包含一个应用层协议、数据库模型和一组资源对象。该协议支持网络管理系统，用以监测连接到网络上的设备。

1、snmpv1/v2鉴权方式与v3的区别

SNMPv1：简单网络管理协议的第一个正式版本。SNMPv2：基于共同体的管理架构，在RFC1901中定义的一个实验性协议。SNMPv3：简单网络管理协议的第三个正式版本。
SNMPv1和SNMPv2由于自身机制而存在安全隐患，请尽量避免使用。建议使用SNMPv3版本的SNMP服务。
v1和V2没有鉴权算法，使用读写团体名和只读团体名进行登录验证
v3需要提供鉴权算法，初次之外还提供用户名、密码、鉴权方式、加密方式

2、脚本使用v1/v2发送命令时需要哪些预置条件

REDFISH_SNMPRWCommunityEnabled_014
需要把v1/v2的使能打开，读写团体名使能状态打开
使用读写团体名和只读团体名登录
如果有登录规则，需要把登录规则给禁用一下

3、snmp接口实现
```
# REDFISH_SNMPRWCommunityEnabled_014 line 146
self.sysMgt.getiBMCHostName(args)
# UniAutos/Component/ServerField/SystemMgt/Huawei/IntelligentCompute.py  getiBMCHostName line 433
self.dispatch('snmpHostName', params)[0]['parser']
# SystemMgt 父类 ComponentBase 的 dispatch方法
# 那 ComponentBase 的 getDispatcher() 是怎么找到 UniAutos/Wrapper/Tool/SnmpCli/NetSnmpTool.py 中的 snmpHostName 方法呢
# 首先NetSnmpTool被导入到SnmpCli类中 snmpCli 的父类 ToolBase 有一个Can方法 这个方法检查方法methodName是否存在，存在就返回方法的引用 但是又怎么能调用到snmpCli的can方法呢？
# 运行是 UniAutos/Device/Host/HostBase.py 938 runToolWrapperMethod
1164 info = self.run(runParams) 在这里面执行snmp命令
744 if sessionType is not None and sessionType == 'snmpcli':
返回 命令执行结果，然后解析
1220  if "parser" in cmdInfo: 
1229  info["parser"] = cmdInfo["parser"](args) 进行解析 parserSnmpHostName
# UniAutos/Component/ServerField/SystemMgt/Huawei/IntelligentCompute.py  getiBMCHostName line 434
snmphostname = self.dispatch('snmpHostName', params)[0]['parser'] 取出结果
return snmphostname.get('HostName') 
```
4、OID和mib的区别

5、鉴权加密算法的默认值区分
```
getDefaultSnmpAlgorithm
setSnmpV3AuthAndPrivacy
```
开启允许用户弱密码`ipmcset -t user -d weakpwddic -v disabled`

关闭允许弱密码`ipmcset -t user -d weakpwddic -v enabled`

### 怎么解释你会这些
- 给他一个连接让他看文档，然后说明这些内容自己会，只是现在忘了，就比如我现在bmc的很多命令很熟，但最后也会忘记一样。
- 重要的是这些经验能帮助减少漏洞，而且有助于解决古怪的问题，从而不至于浪费太长时间
- 而且像方法怎么调用这些知道就行，用的时候可以知道去哪里能快速的查到，而偏向于原理的知识比如怎么去做，调优的方向、内存回收这种才是要记住的
### 怎么发现呢
- 从类的继承关系
- 从类的初始化代码 搜索时注意className和=之间的空格
# 遗留
- 清除用户规则web方式的代码调用 可以直接去iBmcWeb类里找
```
self.userMgt = self.bmc_controller.find('UserMgt')[0]
self.userMgt.userLoginRule(mode="redfish",
                           ruleName="Rule1",
                           timeStart=start_time,
                           timeEnd=error_time,
                           ruleStatus=True)
```
- 只读团体名的长度是通过什么配置的
  - 关闭密码检查功能时：
    - 若已启用超长口令，则团体名可设置为长度为16～32个字符的字符串，字符串不能包含空格。
    - 若已禁用超长口令，则团体名可设置为长度为1～32个字符的字符串，字符串不能包含空格。
  - 开启密码检查功能时：
    - 若已启用超长口令，则团体名可设置为长度为16～32个字符的字符串。
    - 若已禁用超长口令，则团体名可设置为长度为8～32个字符的字符串。
```
self.userMgt = self.bmc_controller.find('UserMgt')[0]
self.userMgt.setPasswordComplexityState("enabled") # 密码复杂度
self.userMgt.setWeakPwdDicState(state="disabled", mode="cli") # 弱口令校验关闭
# 超长口令
body = {'LongPasswordEnabled': False}
ExpectedInfo = {'LongPasswordEnabled': False}
self.redfish.compareBodyValue(statuscode=200,
                              expectedInfo=ExpectedInfo,
                              function="modifySnmpInfoRedfish",
                              params=body)
```
- 那 ComponentBase 的 getDispatcher() 是怎么找到 UniAutos/Wrapper/Tool/SnmpCli/NetSnmpTool.py 中的 snmpHostName 方法呢
- 像LogMgt,RedFish这些Component(业务)怎么和device进行绑定
```
- Server类的实例添加Component
UniAutos/Device/Server/Huawei/Function/ComponentTypes.py 的  COMPONENTS 里以如下形式存储component的 classFullName 
    ('LogMgt',
     'UniAutos.Component.ServerField.LogMgt.Huawei.IntelligentCompute.LogMgt'),
这些信息在Server类初始化时由其基类DeviceBase类初始化的self.setupEnableComponents()（基类DeviceBase的这个方法被Server类重载了）调用addType()
存入self.classDict[classFullName] = klass # klass为定义类
self.__enableComponentsDict[alias] = [classFullName] # alias: LogMgt.lower()
并且会维护self.__enableComponentsDict中的'uniautos.component.serverfield'值
# 借助 owningDevice 来让Component添加所属的设备 
owningDevice是ComponentBase的属性(component即业务所属的设备对象)，并且在组件初始化时被赋值
UniAutos/Component/ServerField/LogMgt/Huawei/IntelligentCompute.py 
59 __init__ self.owningDevice = device  #  device是DeviceBase的实例
```
- server的set和get
```
# set
FusionUniautos/src/Framework/Dev/bin/UniAutosScript.py line408
resourceObject = Resource(testBedInfo)
UniAutos/Resource.py
229 self.initialize()
331 serverErrorMsg = self.__createServerDevices(rawServers)
2152 serverObj = self.__createServerDeviceObject(server) 
2246 serverObjInfo = Server(**serverObjInfo)
2153 self.servers[server['id']] = serverObj # 把device存入self.servers中，device是Server类的实例
# get
testcase
self.serverDevice = self.resource.getDevice(deviceType="server", deviceId="1") # 获取的是Server的实例
UniAutos/Resource.py 1783
deviceObj = self.__getDeviceById(self.servers, deviceId)
```
- server的controller
```
# set
self.controllers = []
UniAutos/Device/Server/Huawei/Server.py 
152 __init__ self.initComponents()
276 self.controllers.append(hostComponent) # hostComponent是Controller类的实例
# get
testcase
self.serverDevice.getController("B1") # 获取的也是Controller类的实例
UniAutos/Device/Server/Huawei/Server.py 
536 getController() for controller in self.controllers:
```
- Controller的find
```
Controller重写owndevice的find方法，目的是为了让component与host绑定在activecontroller，在component find的时候调用对应的Wrapper方法.
UniAutos/Component/ServerField/Controller/Huawei/IntelligentCompute.py 269 
先调用Device 的 find，然后在绑定
Device 的 find
UniAutos/Device/DeviceBase.py
432
```
- 调试下这个
```
self.bmcHost.runCmd("ipmcset -t sol -d activate -v 1 0",
                    waitstr="[Connect SOL successfully! Use 'Esc(' to exit.]")
```
- 首先NetSnmpTool被导入到SnmpCli类中 snmpCli 的父类 ToolBase 有一个Can方法 这个方法检查方法methodName是否存在，存在就返回方法的引用 但是又怎么能调用到snmpCli的can方法呢？
- MIB brower使用
# redfish调用
### redfish调用
- 流程
  - 打印打印self._cache_data值(是上次请求的self._cache_data)
  - 重新获取self._cache_data值 url: https://70.176.5.82/redfish/v1/Managers/1/SmtpService (这次请求的url)
  - 打印self._cache_data值（这次请求获取的）
  - url: https://70.176.5.82/redfish/v1/Managers/1/SmtpService (还是 这次请求的url,不过是用来获取if_match)
  - getresponse :（就是self._cache_data)
  - url: https://70.176.5.82/redfish/v1/Managers/1/SmtpService (真正执行修改)
  - response ：修改的响应
  - 然后打印格式化的响应
- xmind的图也不全
- 在self.Redfish.deleteCompareSubscriptions()调用的是FusionUniautos/src/Framework/Dev/lib/UniAutos/Component/ServerField/RedFish/Huawei/IntelligentCompute.py 的 deleteCompareSubscriptions 然后又dispatch到FusionUniautos/src/Framework/Dev/lib/UniAutos/Wrapper/Api/RedFish/Function/EventService.py 的 deleteCompareSubscriptions
