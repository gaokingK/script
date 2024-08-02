#encoding:utf-8
import math
import os, sys, time
import json
import requests
import re
import logging
import logging.handlers


def init_logger(name, count=10):
    logger = logging.getLogger(__name__)
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
    log_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + os.sep + 'logs' + os.sep + name + '.log'
    print("日志保存在%s" % log_name)
    ###
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight", interval=1,
                                                             encoding='utf-8', backupCount=count)
    time_handler.setLevel(log_level)
    time_handler.setFormatter(formatter)
    con_handler = logging.StreamHandler()
    con_handler.setLevel(log_level)
    con_handler.setFormatter(formatter)
    ###
    logger.setLevel(log_level)
    logger.addHandler(con_handler)
    logger.addHandler(time_handler)
    return logger
logger = init_logger(os.path.basename(__file__).strip('.py'))


def do_request(method, url, headers, payload=None):
    try:
        headers.update({"Cookie":cookie})
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False

def get_anlysis_task(size=500, name=None):
    headers = {
        "Content-Type": "application/json"
    }
    if name:
        url = f"{host}/logAnalysis/api/itoa/dataset/stream?dataSetName={name}&page=0&from=0&size={size}"
    else:
        url = f"{host}/logAnalysis/api/itoa/dataset/stream?page=0&from=0&size={size}"
    res = do_request("GET", url, headers)
    if res.get("retCode") == "0000":
        logger.info(f"获取所有解析任务成功：{res.get('retMsg')}")
        return res.get("entity")
    else:
        logger.error(f"获取所有解析任务失败：{res.get('retMsg')}")


def filter_anlysis():
    name_pattern = r""
    res = []
    for info in all_anlysis_list:
        if name_pattern:
            if not re.search(name_pattern, info["dataSetName"]):
                logger.info(f"{info['dataSetName']}不匹配，跳过")
                continue
        res.append(info["dataSetId"])
    return res

def get_anlysis_info(task_id, check=False):
    """
    check 如果为True，会输出该任务的一些信息
    """
    url = f"{host}/logAnalysis/api/itoa/dataset/stream/{task_id}"
    headers = {
        "Content-Type": "application/json"
    }
    res = do_request("GET", url, headers)
    if res.get("retCode") == "0000":
        res = res.get("entity")
        if check:
            logger.info(f"{res.get('dataSetName')}的"
                        f"内存为{res.get('advanceConfig')[0].get('taskManagerMemory')},"
                        f"并发数为{res.get('advanceConfig')[0].get('instanceNum')}")
        return res

    else:
        logger.error(f"获取解析任务{task_id}失败：{res.get('retMsg')}")

def update_anlysis(task_id):
    new_conf = gen_new_conf(task_id)
    url = f"{host}/logAnalysis/api/itoa/dataset/stream"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "entity": new_conf,
        "statusReq": {"discardSavepoint": True, "offset": "group"}
    }
    res = do_request("PUT", url, headers,payload)
    if res.get("retCode") == "0000":
        logger.info(f"更新解析任务{new_conf.get('dataSetName')}成功：{res.get('retMsg')}")
    else:
        logger.error(f"更新解析任务{task_id}失败：{res.get('retMsg')}")


def gen_new_conf(task_id):
    task_info = get_anlysis_info(task_id)
    task_info["filter"]["filterGroup"]["filtersJson"] = conf_templete["filtersJson"]
    return task_info


if __name__ == "__main__":
    host = "http://10.240.246.138:8080"

    cookie = "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzIxMjY2Mjg3MDc0LCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCIsXCJyZWZpbmVyXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjU2NDM2MTU4MzI0NDE4NTYsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJjWit4ekdpUVBSZWpISW1OZUlKK1FGV2t3Uk9PcTFEelVZZ0FuWmtycTN4dDhzZkMrOGgzK3hLbEpDMmdPb3VqYlZCdTNna29mVUFzYk1aZGpxdEFMNTRzaG5VdThMdkRGa2VSemhJb3VSZWowOGRvSTRsVE5Ud3FoQnF2c2dIeVFmNFY0VzM5UmMzMHkxeUxKVVVBNlRDbTNkN2JuMEw0MVpxQjhTWEJVNE09IiwicHJvZHVjdHMiOiJ7fSJ9.gipP-kkDRcgYPZpfP1r0ZPnhG22hDjTnJuq_DbLEe-RsQBPtTi7etrMp4l9iEnEyeJ20lbRGzIE8K-VR0Zxrfg"
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "anlysis_conf_templete.json")) as f:
        conf_templete = json.load(f)
    # ECMP_APPLOG
    all_anlysis_list = get_anlysis_task(name="ECMP")
    # all_anlysis_list = get_anlysis_task()
    all_anlysis_list = filter_anlysis()


    for task_id in all_anlysis_list:
        # 获取任务信息
        # get_anlysis_info(task_id, check=True)
        # continue
        # 修改任务
        update_anlysis(task_id)
        time.sleep(1)

