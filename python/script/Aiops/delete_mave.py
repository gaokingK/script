# /iops/python/python-3.8.13/bin/python3.8
#encoding:utf-8
import math
import os, sys,time
import requests
import logging
import logging.handlers
from datetime import datetime
#!/aiops/python/python-3.8.13/bin/python3.8

def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
    log_path = os.getcwd()
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + "\\" + name + "_" + datetime.now().strftime("%Y%m%d") + '.log'
    print("日志保存在%s" % log_name)
    ###
    ch_handler = logging.StreamHandler()
    ch_handler.setLevel(log_level)
    ch_handler.setFormatter(formatter)
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight", interval=1,
                                                             encoding='utf-8', backupCount=count)
    time_handler.setLevel(log_level)
    time_handler.setFormatter(formatter)
    ###
    logger.setLevel(log_level)
    logger.addHandler(time_handler)
    logger.addHandler(ch_handler)
    return logger

def do_request(method, url, headers, payload):
    try:
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False

def get_cookie():
    payload = {"userName":"admin","password":"SH4uRFfyjLdxppCzZNr3sNrovpckhG4Srb/5WHCzJ5FpMkFyEhT0b82FIngIdQKhKa/emAVWiSY7crkXBZTuRbCVfunPqY61IyjLH3LyMuZVgTrEOprhT17B/EjDnwU53oe201w2/pcussNKTx5iVJNPr9Cmexrb4vfN5NRVRn0=","verificationCode":"","verificationCodeId":0,"enableLDAP":False,"flag":False}
    url = "%s/authentication/api/login"%host
    header = {"Content-Type": "application/json"}
    res = requests.request("POST", url=url, headers=header, json=payload)
    return res.cookies

def get_offline(ip_list,page=0, start=0, size=10):
    headers = {
        "Content-Type": "application/json",
        "Cookie":cookie
    }
    # url = "%s/api/cell/agents" % host
    url = "%s/logAnalysis/api/cell/agents" % host
    offline_mave_list, no_offline_list = [], []
    for ip in ip_list:
        payload = {
            "filter":{"hostnameOrIp": ip,"connection": 2},
            "sort":{"field":"update_time","order":"desc"},
            "page":page,"from":start ,"size":size
        }
        res = do_request("POST", url,headers, payload).get("entity", {}).get("list", [])
        if res:
            for item in res:
                data = {}
                data["agentId"] = item["agentId"]
                data["ip"] = item["ip"]
                data["lastHbTime"] = item["lastHbTime"]
                offline_mave_list.append(data)
        else:
            no_offline_list.append(ip)
    return offline_mave_list, no_offline_list


def del_mave(offline_list):
    try:
        url = "%s/api/cell/agent"%host
        url = "%s/logAnalysis/api/cell/agent"%host
        header = {"Content-Type": "application/json", "Cookie":cookie}
        delete_list = [item["agentId"] for item in offline_list]
        # delete_list = [2577946515139233]
        payload = {
            "ids": delete_list,
            "op": "delete"
        }
        res = do_request("POST", url, header, payload)
        if res:
            logger.info("删除成功")
        else:
            logger.error("删除失败")
    except Exception as e:
        logger.error("删除失败")
        logger.exception(e)

def parse_ip(all_ip):
    try:
        ip_list = [x.strip() for x in all_ip.split(",") if x.strip()]
        ip_list = list(set(ip_list))
        return ip_list
    except Exception as e:
        logger.error(f"解析参数失败:\n{all_ip}")
        logger.exception(e)

def parse_ip_from_file(file_path):
    try:
        with open(file_path, "r+") as f:
            all_ip = f.readlines()
        print(f"删除{len(all_ip)}台")
        ip_list = [x.strip() for x in all_ip if x.strip()]
        ip_list = list(set(ip_list))
        print(f"去重后的IP个数为{len(all_ip)}")
        return ip_list
    except Exception as e:
        logger.error(f"解析参数失败:\n{all_ip}")
        logger.exception(e)


if __name__ == '__main__':
    print(__file__)
    print(os.getcwd())
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(__file__))
    logger = init_logger(os.path.basename(__file__).strip('.py'))
    paso = ["CB","CBC", "PDMP.ECMP", "CMO.POF", "IST"]
    env1 = ["PI1", "PI2", "UAT1", "UAT2", "UAT3", "UAT4", "PL1", "PL2", "SIT1", "SIT2", "SIT3", "KFLT1", "KFLT2"]
    env2 = ["PI1", "PI2", "SFYL1", "UAT1", "UAT2", "UAT3", "UAT4", "SIT1", "SIT2"]
    topic_d = {
    "CB": env1,
    "ECMP": env1,
    "CMO.POF": env1,
    "IST": env1,
    "CBC": env2
    }
    # 测试
    # conf=gen_conf("APP_test_TRACELOG_SOURCE_test")
    # create_jax(conf)
    # create_analysis(conf)
    # create_storage(conf)
    # exit()
    for paso in topic_d:
        logging.info(f"创建{paso}的")
        for env in topic_d[paso]:
            topic = f"APP_{paso}_TRACELOG_SOURCE_{env}"
            logging.info(topic)
    exit()
    # host = "http://10.251.52.102:7680"
    host = "http://10.251.52.102:18080"
    # host = "http://10.251.52.102:7680"
    # host = "http://10.240.99.200:7680"
    cookie="UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzE1Mzg5NzA3Mzk4LCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCIsXCJyZWZpbmVyXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjU0NTEwNTIwNjk2MTg2ODgsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJjWit4ekdpUVBSZWpISW1OZUlKK1FGV2t3Uk9PcTFEelVZZ0FuWmtycTN4dDhzZkMrOGgzK3hLbEpDMmdPb3VqYlZCdTNna29mVUFzYk1aZGpxdEFMNTRzaG5VdThMdkRGa2VSemhJb3VSZWowOGRvSTRsVE5Ud3FoQnF2c2dIeVFmNFY0VzM5UmMzMHkxeUxKVVVBNlRDbTNkN2JuMEw0MVpxQjhTWEJVNE09IiwicHJvZHVjdHMiOiJ7fSJ9.2kjby48DtbcAuEayUkUSq4veVcEz-4fzpuA2piAlUP4eq-__UBPcgwj656q4cr7kT2LE3eyJhNBVEZE3MasRxw"

    # if len(sys.argv) > 1:
        # all_ip = sys.argv[1]
        # all_ip = parse_ip(all_ip)
    # 10.232.49.85
    if True:
        all_ip = parse_ip_from_file("./下线ip_0511.txt")
        batch_count=50
        for i in range(math.ceil(len(all_ip)/batch_count)):
            current_ip_list = all_ip[i*batch_count: (i+1)*batch_count]
            logger.info(f"第{i+1}/{math.ceil(len(all_ip)/batch_count)}轮")
            offline_mave_list, no_offline_list = get_offline(current_ip_list)
            logger.info(f"以下ip无离线状态的采集器:\n{no_offline_list}")
            if offline_mave_list:
                logger.info(f"删除以下ip上的采集器:\n{offline_mave_list}")
                del_mave(offline_mave_list)
            time.sleep(0.1)
        # print(sys.argv[1])
    else:
        logger.error("请传入参数如：\"10.240.97.39, 10.208.5.35, .... \"")
        print(sys.argv[1])
