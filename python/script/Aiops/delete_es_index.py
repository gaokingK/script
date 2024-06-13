import requests
import os, json
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
    log_name = log_path + "/" + name + "_" + datetime.now().strftime("%Y%m%d") + '.log'
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
logger = init_logger(os.path.basename(__file__).strip('.py'))


def delete_es_index(index):
    url = "http://10.251.52.102:18080/cerebro/overview/delete_indices"

    payload = {
        "indices": "sys_oracle_alertunix_eoi_2024_04_25",
        "host": "http://10.207.64.26:29202",
        "username": "elastic",
        "password": "Aiops_2022"
    }
    headers = {
        "Cookie": "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzE3Mzk5MzI0ODIwLCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCIsXCJyZWZpbmVyXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjU1MTY5MDMyMTMzMDI3ODQsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJjWit4ekdpUVBSZWpISW1OZUlKK1FGV2t3Uk9PcTFEelVZZ0FuWmtycTN4dDhzZkMrOGgzK3hLbEpDMmdPb3VqYlZCdTNna29mVUFzYk1aZGpxdEFMNTRzaG5VdThMdkRGa2VSemhJb3VSZWowOGRvSTRsVE5Ud3FoQnF2c2dIeVFmNFY0VzM5UmMzMHkxeUxKVVVBNlRDbTNkN2JuMEw0MVpxQjhTWEJVNE09IiwicHJvZHVjdHMiOiJ7fSJ9.LsQ1M3z5Z73pOt75JO-65zhYPsYXhqTLKY5HeDKcWnuti73pm7iaqD_7xPqIXdxOYuyiMmfqCd-0Isu9b4xqSQ",
        "content-type": "application/json"
    }
    try:
        res = requests.request("POST", url, json=payload, headers=headers).json()
        if res.get("status") == 200:
            logger.error(f"删除索引{index}成功")
            return True
        logger.error(f"删除索引{index}失败")
        return False
    except Exception as e:
        logger.exception(e)
        logger.error(f"删除索引{index}失败")

def filter(index):
    if not index:
        return False
    
    if "_eoi_2023_" not in index:
        return False
    
    if "net_nmm_almlog_source" in index:
        return False
    
    if "itm_linux_securelog_source" in index:
        return False

    if "itm_linux_dmesglog_source" in index:
        return False

    if "itm_linux_messageslog_source" in index:
        return False

    if "itm_san_syslog_source" in index:
        return False

    if "itm_net_syslog" in index:
        return False

    return True

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "es_index.json"), "r", encoding='utf-8') as f:
        all_data = json.load(f)

    for item in all_data:
        name = item.get("name", "")
        if filter(name):
            delete_es_index(name)
