import sys
import os,re
import pandas as pd
from pyzabbix import ZabbixAPI


# 获取要读取的Excel文件名
if len(sys.argv) < 4:
    print("Usage: python script_name.py <excel_file|-I <ips>> -A <applications> -O <output_file.xlsx>")
    sys.exit(1)

def select_zabbix_server():
    zabbix_servers = {
        'zj': {
            'area': 'zj',
            'url': 'http://10.251.4.18:8082/zabbix/zj',
            #'user': 'user1',
            #'password': 'password1'
        },
        'sq': {
            'area': 'sq',
            'url': 'http://10.251.4.18:8082/zabbix/sq',
            #'user': 'user2',
            #'password': 'password2'
        },
        'cloud': {
            'area': 'cloud',
            'url': 'http://10.239.1.65:8080',
            #'user': 'user3',
            #'password': 'password3'
        },
        'zjhw': {
            'area': 'zjhw',
            'url': 'http://10.251.4.18:8082/zabbix/zjhw',
            #'user': 'user4',
            #'password': 'password4'
        }, 
        'sqhw': {
            'area': 'sqhw',
            'url': 'http://10.251.4.18:8082/zabbix/sqhw',
            #'user': 'user5',
            #'password': 'password5'
        }        
        # 根据实际情况添加更多的 Zabbix 环境
    }

    print("管理员，请选择你要使用的 Zabbix 环境：")
    for key in zabbix_servers:
        print(key)

    selected_server = input("请输入要执行的 Zabbix 环境名称：")
    if selected_server in zabbix_servers:
        return zabbix_servers[selected_server]
    else:
        print("Error: 选择的环境不存在!")
        sys.exit(1)
        
zabbix_info = select_zabbix_server()
zabbix_server = zabbix_info['url']
zabbix_area = zabbix_info['area']
#zabbix_user = zabbix_info['user']
#zabbix_password = zabbix_info['password']
zabbix_user = 'ywptzabbix'
zabbix_password = 'Ywpt!@34'
zapi = ZabbixAPI(url=zabbix_server, user=zabbix_user, password=zabbix_password)

def get_item_info(ip, applications=[]):
    item_info_list = []
    
    # 查询对应主机的触发器表达式
    host_info = zapi.hostinterface.get(filter={"ip": ip})
    
    if host_info:
        for host in host_info:
            host_id = host['hostid']
            host_name = zapi.host.get(hostids=host_id)[0]['host']

            if applications:
                # 获取主机相关的applicationid
                app_ids = [app['applicationid'] for app in zapi.application.get(hostids=host_id) if app['name'] in applications]
                items = zapi.item.get(hostids=host_id, applicationids=app_ids, output=['name','key_','status','lastvalue'])
            else:
                items = zapi.item.get(hostids=host_id, output=['name','key_','status','lastvalue'])

            for item in items:
                item_info_list.append({
                    'IP': ip,
                    'Host': host_name,
                    'Item Name': item['name'],
                    'Item Key': item['key_'],
                    'Item Status': item['status'],
                    'Lastvalue': item['lastvalue']
                })
    
    return item_info_list

# 获取指定的applications
applications = []
if "-A" in sys.argv:
    try:
        index = sys.argv.index("-A")
        applications = sys.argv[index + 1].split(',')
    except IndexError:
        pass
        
# 获取指定的output_file文件名
if "-O" in sys.argv:
    try:
        index = sys.argv.index("-O")
        output_file = sys.argv[index + 1]
    except IndexError:
        pass

# 从Excel中读取IP列表
output_data = []
if "-I" in sys.argv:
    ips = []
    try:
        index = sys.argv.index("-I")
        ips = sys.argv[index + 1].split(',')
        
        for ip in ips:
            item_info_list = get_item_info(ip, applications)
            output_data.extend(item_info_list)
    except IndexError:
        pass
else:
    excel_file = sys.argv[1]
    # 检查文件是否存在
    if not os.path.exists(excel_file):
        print("文件不存在，请检查路径和文件名!")
        sys.exit(1)
        
    df = pd.read_excel(excel_file, usecols=[0])

    b = [{'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_authentication.jar_znyw count', 'Item Key': 'proc.num[,znyw,,"authentication.jar"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_authentication.jar_znyw memory', 'Item Key': 'proc.mem[,znyw,,"authentication.jar",rss]', 'Item Status': '0', 'Lastvalue': '1435738112'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_authentication.jar_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"authentication.jar"]', 'Item Status': '0', 'Lastvalue': '0.7'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_gateway.jar_znyw count', 'Item Key': 'proc.num[,znyw,,"gateway.jar"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_gateway.jar_znyw memory', 'Item Key': 'proc.mem[,znyw,,"gateway.jar",rss]', 'Item Status': '0', 'Lastvalue': '1654284288'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_gateway.jar_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"gateway.jar"]', 'Item Status': '0', 'Lastvalue': '2.2'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_streaming-dataset_znyw count', 'Item Key': 'proc.num[,znyw,,"streaming-dataset"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_streaming-dataset_znyw memory', 'Item Key': 'proc.mem[,znyw,,"streaming-dataset",rss]', 'Item Status': '0', 'Lastvalue': '6141157376'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_streaming-dataset_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"streaming-dataset"]', 'Item Status': '0', 'Lastvalue': '1.1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_insper-server_znyw count', 'Item Key': 'proc.num[,znyw,,"insper-server"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_insper-server_znyw memory', 'Item Key': 'proc.mem[,znyw,,"insper-server",rss]', 'Item Status': '0', 'Lastvalue': '1744166912'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_insper-server_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"insper-server"]', 'Item Status': '0', 'Lastvalue': '9.3'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_planAlert_znyw count', 'Item Key': 'proc.num[,znyw,,"planAlert"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_planAlert_znyw memory', 'Item Key': 'proc.mem[,znyw,,"planAlert",rss]', 'Item Status': '0', 'Lastvalue': '769794048'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_planAlert_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"planAlert"]', 'Item Status': '0', 'Lastvalue': '0.1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_jax-web_znyw count', 'Item Key': 'proc.num[,znyw,,"jax-web"]', 'Item Status': '0', 'Lastvalue': '1'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_jax-web_znyw memory', 'Item Key': 'proc.mem[,znyw,,"jax-web",rss]', 'Item Status': '0', 'Lastvalue': '1698185216'}, {'IP': '10.239.84.74', 'Host': 'zjiopsappa01', 'Item Name': 'IOPS_PROC_jax-web_znyw cpuutil', 'Item Key': 'proc.cpu.util[,znyw,,"jax-web"]', 'Item Status': '0', 'Lastvalue': '8.6'}]

    for ip in df['IP']:
        item_info_list = get_item_info(ip, applications)
        description = ""
        alert_rule = ""
        for item in item_info_list:
            if item["Item Key"].startswith("proc.num"):
                keywords = re.findall(r"\[.*?([\w.]+).*?([\w.]+).*\]", item["Item Key"])
                if keywords:
                    keywords = keywords[0]
                if len(keywords) > 1:
                    description = f"用户{keywords[0]}下名为{keywords[1]}的进程数量"
                    alert_rule = "进程数小于1"
            elif item["Item Key"].startswith("proc.cpu"):
                keywords = re.findall(r"\[.*?([\w.]+).*?([\w.]+).*\]", item["Item Key"])
                if keywords:
                    keywords = keywords[0]
                if len(keywords) > 1:
                    description = f"用户{keywords[0]}下名为{keywords[1]}的进程cpu使用率"
                    alert_rule = "无告警"
            elif item["Item Key"].startswith("proc.mem"):
                keywords = re.findall(r"\[.*?([\w.]+).*?([\w.]+).*\]", item["Item Key"])
                if keywords:
                    keywords = keywords[0]
                if len(keywords) > 1:
                    description = f"用户{keywords[0]}下名为{keywords[1]}的进程内存使用率"
                    alert_rule = "无告警"
            
            item.update({"description": description, "alert_rule":alert_rule})

        output_data.extend(item_info_list)

# 将数据输出到Excel文件
output_df = pd.DataFrame(output_data)
output_df.to_excel(output_file, index=False)
bos="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⣠⡾⠿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠿⠿⠷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                   
   智慧金融·专业服务⠀⠀⠀⠀
"""
print(bos)
print(f"查询结果已保存到 {output_file}")

