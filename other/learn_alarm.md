learn_alarm.md
- 不挑机型的模拟告警
```
ipmcset -t precisealarm -d mock -v 0x12000013 assert
```
- snmpwalk -t 10  -v3 -l priv -a  SHA  -x AES -u Administrator -A Admin@9000 -X Admin@9000 70.176.25.14:161  HUAWEI-SERVER-IBMC-MIB::systemHealthEventDescriptionEntry  
HUAWEI-SERVER-IBMC-MIB::systemHealthEventDescriptionEntry = No Such Object available on this agent at this OID 如果没有告警就会这样，有告警了就能查出来了
### 根据告警码获取告警属性
- 先确定告警的事件信息：在platform_v5里搜索告警码，class为EventInformation对应的就是要找的事件信息的属性名
- 根据五元组找到板卡xml：从板卡xml里寻找告警属性；五元组（A-B-C-D-E)对应的板卡xml是BA-DC
- 找出对应的事件监控对象：打开板卡的xml，在里面搜索步骤一找到属性名，就找到了对应的事件监控对象
- Reading属性对应的就是要找的的告警属性
### 告警属性配置
- 根据机型配置： UniAutos/Component/ServerField/AlarmEvent/Huawei/EventCollection/Mainboard/0x100000C1.json
- 根据板卡配置： UniAutos/Component/ServerField/AlarmEvent/Huawei/EventCollection/PCIeCard/0x08000061.json
- 五元组怎么获取
```
vid_info = self.alarmMgt.getVidSubvid(debug_object=obj)
boardId = self.alarmMgt.debugCommand(method="getprop", attribute_name="{}.BoardId".format(obj))
card_name = vid_info + "_" + CommonFunc.numToHex(boardId)
info = self.alarmMgt.getPcieCardObjectAlarmValue(event_id=event_id, debug_object=obj, card_nam=card_name)
```
### 告警事件失败原因分析
- 模拟告警失败原因
  - 机型未适配
    - json文件未适配 Alarm_mainboard_0073 适配2288H V6 http://taas.xfusion.com/heaven/#/log?log_id=9ae05e01c2824ffd6411a65261b43c4a 修改json文件
    - 告警命令未适配 FDM_Log_Transfer_146 适配FDM命令
    - 机型不支持 0x06000003 EVENT_REDFISH_EVENTTYPE_052 修改环境映射规则  要注意是不是测试主体
  - 缺少板卡
    - 修改映射规则 缺少Raid卡 TC_NandFlash_Fun_008 修改映射规则
    - 模拟加载板卡 Alarm_pciecard_Raid_0111
    - 映射规则有，但是环境变了 Alarm_pciecard_0090 http://taas.xfusion.com/heaven/#/log?log_id=0d493fa1ff0330073fcc8edc81a66634 还是要去确认一下卡在不在，可以去web上看下，也可以去一键收集日志里面看当时跑的时候这个卡到底在不在
  - 卡需要适配
    - Alarm_pciecard_0703 0x08000061 http://taas.xfusion.com/heaven/#/log?log_id=6fcebb67679808f21d0d1f6630537e02
    - http://taas.xfusion.com/heaven/#/log?log_id=9801a20b881e3f03975a9d251611f0ac
  - 模拟告警延时出现
      - 增加等待的时间 但是要确认下告警命令需要适配不能，是不是问题
  - 告警描述校验失败的 就修改json文件
    - Alarm_pciecard_0703 0x08000061 http://taas.xfusion.com/heaven/#/log?log_id=6fcebb67679808f21d0d1f6630537e02
- 如何确定告警被板卡支持
  - 获取告警对象 在platform_v5/v6.xml中搜索
  - 全局搜索该告警对象 有结果的就是支持告警的卡
- 如何确定卡被那些环境上支持
  - 单板支持的兼容性板卡都在board目录下的profile.txt application\src\resource\board\1288hv6_2288hv6_5288v6\2288hv6\profile.txt
  - 搜索三元组14140130_100000af_19e5d225 （五元组A-B-C-D-E 换成3元组的后面两元组 BA-DC） 如果在某个机型的profile里存在，就是支持
  - 14140129为Riser卡，1406G002为硬盘背板，14220246为网卡 14220292为Raid卡，14140130为PCIE卡，14140228为硬盘，14220376为MEZZ卡
- 模拟加载板卡
```
Alarm_pciecard_Raid_0111
card_xml = "14140130_100000af_19e5d225"
self.result = self.PCIeCardMgt.loadAnyCard(card_xml=card_xml)
```
- 告警上报常见失败原因
  - 邮件被覆盖 
    - http://taas.xfusion.com/heaven/#/log?log_id=7b50099eb2d9b67c9210840a418bdfcd
  - trap鉴权方式错误
    - 修改 Syslog_RFC3164_fun_CLI_003 
  - trap 信息不在最新一条
    - EVENT_TRAP_Config_010 http://taas.xfusion.com/heaven/#/log?log_id=7409d71b218ec28cb5a46c5bd0598f37 
    - 修改：Txoid_Trap_Function_0110
- trap特性
  - Sensor_Trap_CLI_013
```
# 获取trap服务器的配置
self.trapserver = self.bmcController.host.getService('snmptrap')
self.trapinfo = self.trapserver.getConfig(
    required_args=["server", "username", "password"])
# 使用snmp方式来设置trap信息
EngineID = self.SystemMgt.getEngineID(mode='redfish').get("SnmpV3EngineID")
# 设置trap服务器上的配置
self.trap_port = str(random.randint(1, 65535))
self.logger.info("随机端口为：", self.trap_port)
self.trapserver.setUpTrapService(
    egineid=EngineID, port=self.trap_port,
    community=community_test, privpwd=self.bmcuserpassword,
    username=self.bmcusername, athpwd=self.bmcuserpassword)
#设置环境上的trap配置
self.alarmMgt.setAlarmTrapReceive(
    trap_port=self.trap_port,
    TrapVersion='V1', AlarmSeverity='Minor',
    TrapServerAddress=self.trapinfo['server'])
# 获取trap服务器收到的上报信息
res = self.trapserver.getTrapReceive(port=self.trap_port)
# 对收到的信息进行检查
self.alarmMgt.trapOidReceiverChk(
    trap_msg=res,
    trap_event_code=event_id)
```
# 遗留
- 邮件并发 调度
- REDFISH_EventAlarm_049 有没有日志可以看发送操作成功了没 是不是负债太多了 可以用cte来验证一下

# syslog服务器排查
- 首先看进程起来了没有 
```
ps -ef|grep ng
install:~ # ps -ef|grep ng
root         39      2  0 Jan28 ?        00:00:00 [khungtaskd]
root       1680      1  0 Jan28 ?        00:00:00 /usr/sbin/syslog-ng -F
root       6552   6480  0 15:17 pts/0    00:00:00 grep --color=auto ng
如果没有就是进程没有起来，先手动试一下 /sbin/syslog-ng -f /etc/syslog-ng/syslog-ng.conf 看配置文件跑错不报，报错了就看报错的行，和正常的服务器中的配置对比修改一下
然后reboot服务器
```
# smtp服务器排查
### 登录宿主机
- 70.171.2.9 root Xfusion@123
- 90.90.203.19 root Xfusion12#$
- 点击更多虚拟机
![](../imgs/smtp_17.png)
![](../imgs/smtp_18.png)
![](../imgs/smtp_19.png)
![](../imgs/smtp_20.png)
- 然后输入密码，所有的密码都是Huawei12#$
- 打开后spec不用管，直接最小化就行



### 重启后的操作
- 打开 Exchange Mangement Console 确认协议里有这个smtp 
![](../imgs/smtp_1.png)
- 132要把这个表单服务给打开
![](../imgs/smtp_12.png)
- 如果证书不正确，就点右边的将服务分配给证书
- 如果启动报错，就控制台搜索 services.msc 然后点击 Micrsoft Exchange Service主机 这条服务，启动
![](../imgs/smtp_02.png)
- 不支持tls协议，要把这个重新分配下，然后在服务里重新启动下micrsoft ExchangeService 主机
![](../imgs/smtp_13.png)
- 点击全是
![](../imgs/smtp_16.png)
- 出现下面这两种错误，重启os
![](../imgs/smtp_14.png)
![](../imgs/smtp_15.png)
- 如果网络出错了，先看网络配置是否出错 点击本地连接>属性>TCP/IPV4>属性(下图是正常的)
![](../imgs/smtp_03.png)
![](../imgs/smtp_04.png)
- 如果配置正常，但还是ping不通 点击更改适配器设置>禁用本地连接>启动本地连接来重启网络
![](../imgs/smtp_05.png)
- 所有的服务
![](../imgs/smtp_06.png)
![](../imgs/smtp_07.png)
![](../imgs/smtp_08.png)
![](../imgs/smtp_09.png)
![](../imgs/smtp_10.png)
![](../imgs/smtp_11.png)

# learn_code
### 命名
- FusionUniautos/src/Framework/Dev/lib/UniAutos/Component/ServerField/AlarmEvent/Huawei/IntelligentCompute.py 的self.properties
- dispatch
- dispatch是怎么搞进去得
  - self.wrapper_list 是什么时候接收数据的？
  - 所有下发到设备的命令都会经由分发器，选择合适的Wrapper来执行，调的就是wrapper里的方法
- component 业务对象
- controller
- wrapper
- discover
  - discoverCommandInstance 生成Command对象 -> return CommandBase.discover(**temp)
- 了解下代码的继承结构
- 创个分支写注释
- 模块是怎么导入的
```
UniAutos/Wrapper/Tool/SnmpCli/SnmpCli.py
    modules = [
        'UniAutos.Wrapper.Tool.SnmpCli.NetSnmpTool',
        'UniAutos.Wrapper.Tool.SnmpCli.System',
        'UniAutos.Wrapper.Tool.SnmpCli.snmpUserMgt',
        'UniAutos.Wrapper.Tool.SnmpCli.snmpAlarmMgt',
        'UniAutos.Wrapper.Tool.SnmpCli.SnmpPoD',
        'UniAutos.Wrapper.Tool.SnmpCli.SnmpPower'
    ]

    def __init__(self, params=None):
        """wrapper的tool基类，封装Linux命令行下的业务命令解析
        Args:
            params (dict): 此处仅关注key: retry
            Attributes:
                "logger"                       (obj):  一个日志对象，用于记录日志
                "retry"                       (dict): 命令执行失败后是否重试的重试信息
                "method_release_requirement"  (list): 释放时需要执行的方法列表
                "user_retry_codes"            (list): 用户自定义的需要重试的字符串列表
        Returns:
            None
        Raises:
            None
        Examples:
            Nonew
        """
        super(SnmpCli, self).__init__(params)
        self._vendorSnmp = None
        for m in self.modules:
            __import__(m)
            for i in dir(sys.modules[m]):
                if i.find("__") < 0:
                    method = getattr(sys.modules[m], i)
                    setattr(self, i, method)
```
- self.wrapper_list 怎么改变的
- FusionUniautos/src/Framework/Dev/lib/UniAutos/Wrapper/Tool/BmcCli/BmcCli.py 里的module是干什么的
- 调试代码失去响应时可以把浏览器给关了
- 在FusionUniautos/src/Framework/Dev/lib/UniAutos/Dispatcher.py的activatecan中就跳到方法中去开始执行了，能调试到
- 看代码时一直想知道变量是啥时候被赋值的，所以很麻烦

- 初始化GUI执行机时杀死进程![](../imgs/kill_gui_process.PNG)
- 运行命令后输入y TC_NandFlash_Reliablity_024 ipmcset -d clearlog -v 0

- echo is not received 这个是因为抛出socket.timeout异常了，但是还没有超过传入的命令执行的等待事件
  - UniAutos/Command/Connection/ServerConnection.py def recv
- 从日志中看redfish的请求地址
```
是resource的data.id
```
- 这不是重复了吗？
```
        if params.get("action").split(".")[0] in dict_item.keys():
            if re.search(params.get("action").split(".")[0], params['action']):
```
- redfish 值
  - self.SystemMgt.vendorSnmp.SnmpNameOID: "2011"
  - mapping.redfish_mapper.map_members() "Members"
  - mapping.redfish_mapper.map_links_ref() '@odata.id'
  - self.redfish.vendorRedfish.OemName "Huawei"
  - self.bmcController.getHostObject().getBmcBranchVersion() "Version"
  - self.url 是已打印的这个url https://70.176.18.34/redfish/v1/Systems/1/Processors 然后再与odata.id拼接
  ```
  [2022-10-09 15:08:41,622][2680][DEBUG] > url: https://70.176.18.34/redfish/v1/Systems/1/Processors
  [2022-10-09 15:08:41,625][2680][DEBUG] > Starting new HTTPS connection (1): 70.176.18.34:443
  [2022-10-09 15:08:42,026][2680][DEBUG] > https://70.176.18.34:443 "GET /redfish/v1/Systems/1/Processors HTTP/1.1" 200 352
  [2022-10-09 15:08:42,033][2680][DEBUG] > 打印self._cache_data值：
  ```
- redfish的url是怎么获取的
```
  File "/mnt/uniautos/prj/framework/src/Framework/Dev/lib/UniAutos/Wrapper/Api/RedFish/Function/Managers.py", line 752, in modifySyslogInfoRedfish
    syslogInfo = dev.syslog_service.modify_syslog(modifyInfo)
  File "/mnt/uniautos/prj/framework/src/Framework/Dev/lib/UniAutos/Wrapper/Api/RedFish/Root/Managers.py", line 191, in syslog_service
    self._syslog_service = SyslogService(self.get_link_url('SyslogService', self.cache_data.Oem[self.vendorRedfish.OemName])
    # self.cache_date 上有各种url ，然后通过syslogService来取出来
```
- 看日志中的异常
```
# 异常信息
[2022-06-06 14:28:26,772][13840][DEBUG] > Running: UniAutos.Wrapper.Api.RedFish.BmcRedFish.BmcRedFish
Method: getAlarmEventProperty
With params: {}
[2022-06-06 14:28:26,775][13840][INFO] > Traceback (most recent call last):
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Dispatcher.py", line 459, in syncClassDispatch
    ret = self.__callWrapper(runWrapperParams, methodName, syncParamsDict, 1)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Dispatcher.py", line 893, in __callWrapper
    ret = self.activateCan(can, curWrapper, wrapperParamsDict)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Dispatcher.py", line 777, in activateCan
    ret = can()
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Wrapper\Api\RedFish\BmcRedFish.py", line 621, in getAlarmEventProperty
    public_info = self.getRedfishInfo()
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Wrapper\Api\RedFish\Function\Public.py", line 48, in getRedfishInfo
    info = self.Public.get_pub_info()
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Wrapper\Api\RedFish\BmcRedFish.py", line 94, in __getattribute__
    return super(BmcRedFish, self).__getattribute__(item)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Wrapper\Api\RedFish\BmcRedFish.py", line 162, in Public
    self._PublicResource = PublicResource(self.connection_parameters.rooturl,
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Wrapper\Api\RedFish\BmcRedFish.py", line 93, in __getattribute__
    setattr(cnn_param, 'vendorObj', getattr(dev_obj.vendorObj, "redfish"))
AttributeError: 'NoneType' object has no attribute 'redfish'

[2022-06-06 14:28:26,776][13840][DEBUG] > This thread [13840] is releaseing Class Lock for uniautos.component.serverfield.alarmevent.huawei.intelligentcompute.alarmevent
[2022-06-06 14:28:26,778][13840][ERROR] > SNMP_SELEVENT_RH8100_013 Failed, Because an issue occurred while trying to run the test case: 
Traceback (most recent call last):
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\TestEngine\Engine.py", line 285, in _runTest
    testCase.procedure()
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionServer_TcLib\iBMC\TaiShan\02_AlarmEventManagement\02_QueryingAlarmEvents\03_SNMP\SNMP_SELEVENT_RH8100_013.py", line 54, in procedure
    self.alarmMgt = self.bmcController.find("AlarmEvent")[0]
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Component\ServerField\Controller\Huawei\IntelligentCompute.py", line 279, in find
    compObj = self.owningDevice.find(alias=alias, criteria=criteria, forceSync=forceSync)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Device\DeviceBase.py", line 481, in find
    objs = self.classDict[fullName.lower()].sync(self, criteria, forceSync)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Component\ComponentBase.py", line 299, in sync
    twProps = device.syncClassDispatch(cls, criteria, synParams, device)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Device\Server\Huawei\Server.py", line 431, in syncClassDispatch
    syncClassDispatch(componentClass=cls, criteriaDict=criteria, syncParamsDict=synParams, device=self)
  File "C:\Users\jw0013109\Desktop\Uniautos\FusionUniautos\src\Framework\Dev\lib\UniAutos\Dispatcher.py", line 473, in syncClassDispatch
    raise e
AttributeError: 'NoneType' object has no attribute 'redfish'
# 代码
  def syncClassDispatch(self, componentClass, criteriaDict=None, syncParamsDict=None, device=None, ):
      """使用Tool Wrappers同步更新这个类别里面所有对象实例的properties

      Args:
          componentClass(String): Wrapper方法名称,可在相应的Wrapper类里面获取使用信息
          criteriaDict(Dict): 根据同步的对象属性Dict和过滤的Dict进行匹配
          syncParamsDict(Dict): 需要同步的参数属性Dict
          device(UniAUtos.Device): UniAutos Device 对象

      Returns:
          returnDict(Dict): 获得相应的Wrapper对象

      Raises:
          UniAutos.Exception.UniAutosException

      """
      pass
          for methodName in methodDict.values():
              runWrapperParams = {}
              if host is not None:
                  runWrapperParams['host'] = host
              runWrapperParams['wrapper'] = wrapper
              ret = self.__callWrapper(runWrapperParams, methodName, syncParamsDict, 1)

              for result in ret:
                  twProps.extend(result['parser'].values())
                  if result.get("partial", False) or partial:
                      fullFind = False
          return {'properties': twProps,
                  'classes': classes,
                  'full_find': fullFind,
                  'thread_locks': threadComponentClassLocks}
      except Exception as e:
          self.logger.info(traceback.format_exc()) # 如果出现异常，这里会打印异常信息（这里的上一行就是正常运行的输出，而不是failed提示），然后在运行一些代码来补救
          for name in threadComponentClassLocks:
              device.threadUnlock(name)
          raise e 这里会把异常再抛出来，使用例结束 这里就有： SNMP_SELEVENT_RH8100_013 Failed, Because an issue occurred while trying to run the test case:
```

- 看命令回显
```
# 日志打印
stdout为ipmitool raw 0x06 0x25
Could not open device at /dev/ipmi0 or /dev/ipmi/0 or /dev/ipmidev/0: No such file or directory
root@#>, stdlist为['ipmitool raw 0x06 0x25', 'Could not open device at /dev/ipmi0 or /dev/ipmi/0 or /dev/ipmidev/0: No such file or directory', 'root@#>']

# code
stdout = self.execCommands(cmdList, waitList, timeout=timeout)
stdlist = stdout.split('\r\n')
self.logger.debug("stdout为{}, stdlist为{}".format(stdout, stdlist))

# 解释
为什么命令也包含在回显内呢？因为命令你输入进去，他也会显示在屏幕上，所以会显示
那怎么区分命令和结果呢？看下面的stdlist 因为是经过分割的，所以可以看出来
```

- self.locateElementByName('login_buttonLocator') 
  - 文件 FusionUniautos/src/Framework/Dev/lib/UniAutos/Wrapper/Tool/BmcWeb/iBMCV2R2C90/Pages/LoginPage.py：87
  - 在获取属性时加了一个wrapper：decorator_find_element，由wrapper来完成高亮 点击操作
  - wrapper如果有异常，就截屏，等待，重试

- 使用这种模式来返回类的不同实例
  - 说是不同的实例，虽然命名不一样，但其实是一样的，就是入参不同
```
# FusionUniautos/src/Framework/Dev/lib/UniAutos/Command/ConnectionPool.py
class ConnectionPool(object):
    def __init__(self, **kwargs):
        self.loginTarget = None
        self.status = None
        self.version = None
        self.dirty = True
        self.maxSession = kwargs.pop('maxSession', 1)
        self.protocol = kwargs.pop('protocol', 'standSSH')
        self.mutex = threading.RLock()
        self.connectionPool = dict()
        self.rawConnectInfo = dict(kwargs)
        self.defaultConnectInfo = dict(kwargs) 
    pass
    @classmethod
    def createBmcSSHPool(cls, ip, username, password=None, key=None, port=22, maxSession=1):
        return cls(ip=ip, username=username, password=password,
                   key=key, port=port, maxSession=maxSession, protocol='bmcSSH')
    @classmethod
    def createServerSSHPool(cls, ip, username, password=None, key=None, port=22, maxSession=1):
        return cls(ip=ip, username=username, password=password, key=key, port=port, maxSession=maxSession,
                   protocol='serverSSH')
                   
# 使用
if protocol == 'bmcssh':
    return ConnectionPool.createBmcSSHPool(**kwargs)
if protocol == 'serverssh':
    return ConnectionPool.createServerSSHPool(**kwargs)
```