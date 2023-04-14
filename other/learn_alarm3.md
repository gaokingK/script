### 一些自己的改动
- 过滤Hdd硬盘 REDFISH_EventAlarm_001
- 根据机型对1288H V6 使用connector模拟告警 EVENT_AlARM_FUNC_044 有的是SlotNumber相同，有的是Id相同
### other
- #### smtp
```
from UniAutos.Service.SmtpServer import ClassSmtpServer
smtp = ClassSmtpServer(server="70.176.2.133", password="Huawei12#$", username="smtptest")
smtp.getNewerMail(del_option=False)
smtp = ClassSmtpServer(server="70.176.2.132", password="Xfusion", username="smtp1user")
smtp.getNewerMail(del_option=False)
```
- #### syslog
```
Syslog_RFC3164_fun_CLI_008
# 发送测试请求
self.snmpMgt = self.bmcController.find('SnmpMgt')[0]
self.snmpMgt.setSyslogInfoDescriptionEntry(node_name="syslogReceiverTest", value=1, gindex=1)

self.bmcWeb.setSyslogServer(sequence=1, is_test=1)
# 获取日志
cmd = 'cat /var/log/RemoteSyslog/syslog.log'
self.conn = SSHConnection(self.sysloginfo['server'], username=self.sysloginfo['username'], password=self.sysloginfo['password'])
result, isMatch, matchStr = conn.execCommand(cmd, waitstr, timeout, nbytes) # result就是日志内容
conn.reconnect()

Syslog_cli_019
self.syslogserver = self.host.getService('Syslogserver')
self.syslogserver.getSyslogFile("1", checkinfo='Normal,0x2C000001') # id 是bed里的id
```
- 获取产品名
```
self.alarm_mgt = self.bmcController.find("AlarmEvent")[0]
self.alarm_mgt.properties.get("ProductName")
```
- 使用ssh连接执行命令
```
from UniAutos.Command.Connection.SSHConnection import SSHConnection
self.conn = SSHConnection(hostname=nfs_info["server"],
                          username=nfs_info["username"],
                          password=nfs_info["password"])
conn.downloadFile(remote=remote, local=local)
ssh.close()
result, isMatch, matchStr = conn.execCommand(cmd, waitstr, timeout, nbytes)
conn.reconnect()
conn.send(cmd, timeout)              
```
- 获取操作日志
```
self.logMgt = self.bmc.find("LogMgt")[0]
operate_log = self.logMgt.getSystemOperateLog(page=3) # 结果是字符串

if "Clear Security Log successfully" not in operate_log:
            raise UniAutosException("日志校验失败")
# 方法二
from iBMC.ConfigData.BmcOpLogConfig_3 import getOpLogData

        self.bmc = self.bmcController.getHostObject()
        tmss_id = self.getTmssId()
        self.bmc_version = self.bmc.getBmcBranchVersion()
        operate_logs = self.logMgt.getSystemOperateLog()
        self.logInfo("operate_logs:%s" % operate_logs)
        op_logs = getOpLogData(tmss_id, self.bmc_version)
        self.logInfo("op_logs:%s" % op_logs)
        real_log = op_logs[0].replace("xxxx1", username)
        if not re.findall(real_log, str(operate_logs)):
            raise UniAutosException("操作日志校验不符合预期:%s" % real_log)
```
- 获取五元组
```
vid_info = self.alarmMgt.getVidSubvid(debug_object=obj)
boardId = self.alarmMgt.debugCommand(method="getprop", attribute_name="{}.BoardId".format(obj))
card_name = vid_info + "_" + CommonFunc.numToHex(boardId)
self.logger.info("card_name:%s" % card_name)
info = self.alarmMgt.getPcieCardObjectAlarmValue(event_id=event_id, debug_object=obj, card_nam=card_name)
# 方法二
五元组A-B-C-D-E 换成3元组的后面两元组 BA-DC
card_name = self.getSecondFeature()
    def getSecondFeature(self):
        pcieinfo = self.alarmMgt.debugCommand(method="lsprop",
                                              attribute_name=self.obj_info)
        pcie_str = "{0}_{1}_{2}_{3}_{4}".format(
            numToHex(pcieinfo['DeviceId']),
            numToHex(pcieinfo['VenderId']),
            numToHex(pcieinfo['SubDeviceId']),
            numToHex(pcieinfo['SubVenderId']),
            numToHex(pcieinfo['BoardId']))
        return pcie_str
```
- 获取hostname
```
self.nameinfo = self.sysMgt.getiBMCHostName(mode='snmp', snmpversion="1",
                                                    snmpcommunity="roAdministrator@9000")
```
- 获取机型
```
        self.systemgt = self.bmcController.find('SystemMgt')[0]
        self.system_version = self.systemgt.getBmcSystemsVersion(mode="cli")
        self.product_type = self.system_version["Product"]["Product_Name"].split(' ')[-1]
```
- web页面
```
self.bmc_web.setWebTimeout(time="480")
```
- 获取特定卡nic_obj = self.alarm_mgt.getRequirementObj("NetCard", "LomCard", attribute_filter={"ProductName": card})
- 分支判断用 getFeatureVersion 这个函数
```
from UniAutos.Util.CommonFunc import getFeatureVersion
self.version = self.bmcController.getHostObject().getBmcBranchVersion()
if getFeatureVersion(self.version, feature="file_system_reliability") is not True:
```
- snmp 
- 获取默认算法 
```
self.bmc = self.bmcController.getHostObject()
self.default_auth = self.bmc.getDefaultSnmpAlgorithm()

self.snmpMgt = self.bmcController.find('SnmpMgt')[0]
self.snmpMgt.restoreSnmpAlgorithm()

```
- 设置AC掉电
```
def set_ac_cycle(self):
    # 开始AC掉电
    self.powerControl.setACCycle(mode='hostos')
    for i in range(60):
        sleep(3)
        self.logger.info("第 %s 次等待3s检测bmc是否重启" % (i + 1))
        if not pingIpOperate(self.bmc.localIP, 400):
            break
    else:
        raise UniAutosException("未检测到bmc重启，校验失败")
    self.serverDevice.waitRecoverBmcService()
    self.serverDevice.reconnectOS()
```
- 检查日志 
```
checkSelLogCommon
# 方法一
Sensor_Trap_Web_011
self.logMgt = self.bmcController.find('LogMgt')[0]
def check_sel_info(self, level, event_code, status="Asserted", description=""):
    Asserted Deasserted 
    for i in range(20):
        try:
            self.logMgt.checkSelLogInfo(status=status,
                                        level=level,
                                        description=description,
                                        protime=None,
                                        eventcode=event_code,
                                        count=10)
            self.logger.info("[%s, %s, %s, %s]sel日志检查成功" % (status, level, description, event_code))
            break
        except Exception as e:
            self.logger.info("sel日志检查失败，继续查询")
            sleep(5)
    else:
        raise UniAutosException("20次后sel日志检查失败")
# 方法二 
self.log_mgt = self.bmcController.find('LogMgt')[0]
self.info = self.log_mgt.getSelLogInfo(status='Asserted', level=['Normal'],
                description="iBMC operation log has reached 90% space capacity.")
# 方法三
Alarm_mainboard_0724
# 方法三
Sensor_Alarm_True_Test_058
# 方法四
Cli_Discrete_Sensor_002
# 检查维护日志
AlarmBMC_pciecard_1822chip_0703
self.log_mgt = self.bmcController.find('LogMgt')[0]
    def check_maintance_info(self, level, description=""):
        for i in range(20):
            try:
                self.logMgt.checkMaintanceLogCycle(description, level=level, line=20, begin=None, end=None, timeout=1)
                self.logger.info("[%s, %s]维护日志检查成功" % (level, description))
                break
            except Exception as e:
                self.logger.info("维护日志检查失败，继续查询")
                sleep(5)
        else:
            raise UniAutosException("20次后维护日志检查失败")
```
- 校验告警
```
Event_Test_3_Func_060
```
- 设置超时时间
```
        self.logStep("步骤1：设置web超时时间为10分钟，防止内存数量多WEB会话超时的情况")
        params = {"Oem": {"Huawei": {"WebSessionTimeoutMinutes": 10}}}
        self.RedfishTeam.compareBodyValue(statuscode=200, params=params,
                                          function="modifySessionServiceRedfish", expectedInfo=params)
```
- 过滤对象
```
getRequirementObj
```
- 获取ip 
  - bmc: self.bmc_controller.getDispatcher().localIP 
  - bmc: self.bmc_controller.host.localIP
- 模拟加载网卡 
```
Alarm_Others_0696  
self.PCIeCardMgt = self.bmcController.find("PCIeCardMgt")[0]
self.PCIeCardMgt.loadAnyCard(card_xml=card_xml)

# 这两个卡为啥加载不了
# BC11PERV
# V2R2_trunk/application/src/resource/profile/rack_server_01/14140129_9e.xml
# 2288H V6|5288 V6|2288H V5|2288 V5|
# BC11PERT
# V2R2_trunk/application/src/resource/profile/rack_server_01/14140129_94.xml
# 1288H V5|2288H V5|2288 V5|2298 V5
```
- 自己检查告警 SEL_Language_New_010
- self.snmpMgt = self.bmcController.find('SnmpMgt')[0] 在日志中的回显
  - Add component, alias: SnmpMgt, id: 140203325357968
- 调速 Fan_IOTemp2_Target_001_658
- 等待trap iBMC/TaiShan/03_ReporteAlarm/01_Trap/09_Set_Trap_OID/01_Function/Txoid_Trap_Function_0050.py
- 获取默认SNMP鉴权算法 getDefaultSnmpAlgorithm snmp相关 EVENT_TRAP_Config_007 
- 连接telnet为什么要退出
  - 连接数、连接池
  - 一个测试套的连接是通用的，这次连上telnet不退出下个脚本就还用这个连接、不区分连接类型（首先用户的密码不一样、其次命令的回显字符（Administrator /path/这种回显）不一样source /etc/）
- 数字转换字符 format_list.append(chr(int(item, 16)))
- 图像识别： wait_untill_element
- 环境检查 FusionServer_TcLib/server/901_AutomatedFactory/TC_ENVIRONMENT_PRE_CHECK.py
- 下电前后对比告警 Cli_Sensor_002
- 快速增加日志
```
Log_AlmostFull_008
self.SystemMgt = self.bmcController.find("SystemMgt")[0]
self.SystemMgt.setRecordLogDiag(logtype="2", lognum="1000")
maint_debug_cli
attach bmc
record_log 2 100

```
- 恢复环境
```
        self.powerControl.setPowerStateCom(state=2, mode='cli')
        self.powerControl.setPowerStateCom(state=1, mode='cli')
        self.serverDevice.reconnectBMC()
        self.serverDevice.reconnectOS()
        self.serverDevice.waitRecoverBmcService()
        self.repairOs()
        self.powerControl.checkOsStatus(status='up')

# 删除会话
self.redfish = self.bmcController.find("Redfish")[0]
self.redfish.getResponse("delAllSessionRedfish")
```
- 获取host
```
self.testHost = self.resource.getDevice(deviceType='host', deviceId='1')
resReboot = self.testHost.reboot(timeout = "50S")
if resReboot:
    self.logger.info("测试机OS重启成功")
else:
    raise UniAutosException("测试机OS重启失败")
```
- 执行命令  
```
self.init_speed = self.host.run({"command": cmd.split()})['stdout']
FusionUniautos/src/Framework/Dev/lib/UniAutos/Device/Host/HostBase.py run
  - 1
  - self.bmc = self.bmcController.getHostObject()
  - res = self.bmc.runCmd('lsobj Hdd', waitstr='%')
  - self.bmc.run({"command": ['top -bn 1']})
self.bmcHost.command.delConnection({"username": self.bmcHost.username})
b = self.bmcHost.run({'command': [self.conn.linesep], 'timeout': 20, 'waitstr': "login", "input": ["root", "Password:", "Admin@9000"]})
{'stdout': "[Connect SOL successfully! Use 'Esc(' to exit.]\r\nWarning! The SOL session is in shared mode, the operation can be viewed on another terminal.\r\nroot\r\n-bash: root: command not found\r\n[root@localhost ~]# Admin@9000\r\n-bash: Admin@9000: command not found\r\n[root@localhost ~]# ", 'stderr': None, 'rc': 0}
```
- 验证回显信息
```
rspstr_0 = self.bmcController.getBMCCLIBasicCommandsInfo(
    cmd="!@#$%^&*()_=+< >?/ \|ugoirdegh:;'[]{}0123456789",
    waitstr='bash')
 if regExp(''.join(rspstr_0), '!@#$%'):
                self.logger.info("SOL回显信息验证通过")
```
- 延时读取回显
```
self.conn.execCommand("ls") 是send和recv结合到一块的
self.conn = SSHConnection(hostname=self.bmcHost.localIP,
                          username=self.bmcHost.username,
                          password=self.bmcHost.password)
self.conn.send("ls", 10)
self.conn.send("ls", 10)
self.conn.recv() # 两条命令的回显
('ls\r\nprocess.tmp\r\nAdministrator@#>ls\r\nprocess.tmp\r\nAdministrator@#>ls\r\nprocess.tmp\r\nAdministrator@#>', True, '#')        
```

- 获取bmc侧root权限
```
self.firmwareMgt = self.bmcController.find('FirmwareMgt')[0]
self.firmwareMgt.get_root_privilege()
```
- 重启BMC
```
self.bmcController.reboot(wait=True)
self.serverDevice.waitRecoverBmcService(service='Https')
# 方法二
self.bmcController.reboot(wait=True)
self.serverDevice.waitRecoverBmcService(service='RedFish', timeout='600S')
```
- OS上线电重启操作
```
Video_Local_Live_Func_008
self.redfish = self.bmcController.find("Redfish")[0]
response = self.redfish.getResponse(function='setSystemsResetRedfish',
                                    params={"ResetType": "ForceOff"})[0]
if response["status_code"] != 200:
    raise UniAutosException("Redfish执行OS下电失败")
```
- 运行命令 self.serial = self.serverDevice.getController("S1") self.serial.runCmd("ls")
- 删除文件  
```
self.bmc.deleteDirectory('/tmp/dump_info')
self.bmc.deleteFile("/data/share/img/" + 'img*.jpeg')
self.cifs.createDirectory(self.file_path) self.cifs = bmcController.getHostObject().getService('cifs')
```
- 查看文件是否存在 
```
FusionUniautos/src/Framework/Dev/lib/UniAutos/Device/Host/Unix.py doesPathExist
vidoefile = self.fileTransfer.getFileInfo(FilePath=self.filepath) 
   -> FusionUniautos/src/Framework/Dev/lib/UniAutos/Component/ServerField/FileTransfer/Huawei/IntelligentCompute.py getFileInfo
   -> FusionUniautos/src/Framework/Dev/lib/UniAutos/Device/Host/Unix.py listFile
```
- 获取win路径中文件
  - file_list = self.bmcController.iBmcWeb.getFilePathWin(r'C:\download', "record", 1)
  - self.bmcController.iBmcWeb.delFileWin(remoteFileName=r"C:\download\record*")
  - self.firmwareMgt.get_root_privilege()
  - self.filepath = "/data/share/img/manualscreen.jpeg"
  - self.fileTransfer.deleteFile(file_path=self.filepath)
- 传输文件  
  - self.nfs.transportFile(method="download", source_path=self.path0, target_path=self.local_path, target_host="local")
  - self.bmc.scpSftpFile(src="/mnt/dev_sdb/share/ibmc/ssl/server-nopassword.pfx", target="/tmp", method="download")
  - self.bmc.scpLocalFile(src="C:\Users\jw0013109\Desktop\code.PNG", target="/tmp/", method='download') # 本地上传到bmc
- 从nfs中下载文件
  - video_path = self.bmcController.iBmcWeb.downloadFromNFS(True, "ibmc/video", "video.mp4", False)
- 设置trap
```
        self.bmcWeb.setTrapServer(sequence=1, content=['sensor_name', 'level', 'event_code', 'event_description'])
# 通过redfish
        payload = {"TrapVersion": "V3", "TrapMode": "EventCode",
                   "TrapServer": [{"MemberId": 0, "Enabled": True, "TrapServerAddress": "70.176.2.204", "TrapServerPort": 38482,
                                   "BobEnabled": True, "MessageDelimiter": ";",
                                   "MessageContent": {"TimeSelected": True, "SensorNameSelected": True, "SeveritySelected": True, "EventCodeSelected": True, "EventDescriptionSelected": True},
                                   "MessageDisplayKeywordEnabled": True}]}
        body = {"SnmpTrapNotification": payload}
        self.redfish_team.getResponse(function='modifySnmpInfoRedfish', params=body)
```
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
#### redfish
  - AnonymousLoginEnabled smtp匿名登录
### 模拟告警
- 4种告警级别的ipmcset 模拟 Syslog_RFC3164_fun_CLI_005
- redfish模拟
```
REDFISH_Log_002
payLoad = {"EventCode": self.event_code, "Type": "Assert"}
res = self.redfish.getResponse(function='mockPreciseAlarmRedfish', params=payLoad)[0]
```
- 模拟使用动态值 
```
FusionUniautos/src/Framework/Dev/lib/UniAutos/Component/ServerField/AlarmEvent/Huawei/EventCollection/Mainboard/0x1000000B.json
```