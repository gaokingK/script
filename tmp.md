1. string.contains(${systemCode},'01') || string.contains(${systemCode},'05') 删除数据
2. ${eventInfo}==nil 删除
3. ${systemCode}=='09' 将  eventGroup 替换为 应用支持部2组
4. ${systemCode}=='11' 将  eventGroup 替换为 北京分行
5. ${systemCode}=='12' 将  eventGroup 替换为 南京分行
6. ${systemCode}=='13' 将  eventGroup 替换为 天津分行
7. ${systemCode}=='14' 将  eventGroup 替换为 宁波分行
8. ${systemCode}=='15' 苏州分行
9. ${systemCode}=='16' 成都分行
10. ${systemCode}=='17' 深圳分行
11. ${systemCode}=='18' 杭州分行
12. ${systemCode}=='02' 将 alarmValue 替换为 ${eventName}
13. firstTime . -
14. eventGroup MG-NET 网络通讯部
15. eventGroup null 
16. eventStatus PROBLEM 1 
17. eventStatus RESOLVED 2
18. eventLevel CRITICAL P1 MAJOR P2 Average P3 Information P5 Warning   P4
19. eventGroup MG-SYS 系统设备部
20. lastTime . - 
21. systemName 02  系管平台
22. ${systemCode}=='04' ipAddress  全部替换为空 alarmValue 全部替换为 ${eventName}
23. indexKey 保留99个 indexValue 保留49个 alarmValue  保留49个 
24. ${systemCode}=='04' 新增pasoCode ${objectName}
25. eventName 保留254个



{
	"alarmValue": "",
	"configItem": "Used memory (percentage)",
	"eventCount": "",
	"eventGroup": "",
	"eventInfo": "Windows memory used on zjfacpapp07 > 95%",
	"eventLevel": "CRITICAL",
	"eventName": "High memory utilization (over 95%)",
	"eventSerialno": "95150894",
	"eventStatus": "PROBLEM",
	"eventUrlInfo": "",
	"firstTime": "2022.11.23 23:38:00",
	"hostName": "zjfacpapp07",
	"indexKey": "MEMUsage",
	"indexType": "MEM",
	"indexValue": "96.41%",
	"insName": "",
	"ipAddress": "10.251.50.11",
	"lastTime": "2022.11.23 23:38:02",
	"objectCate": "OS",
	"objectID": "",
	"objectName": "10.251.50.11",
	"searchId": "OS.NODENEW",
	"systemCode": "01", 
	"systemName": "ZABBIX"
}
