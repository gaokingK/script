import json
import os
import logging
import logging.handlers

def init_logger(name, count=10):
    logger = logging.getLogger()
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

def filter(one_conf):
    if one_conf.get('advanceConfig'):
        task_conf = json.loads(one_conf.get('advanceConfig'))
        for conf in task_conf.get("store", []):
            if conf.get('taskManagerMemory') > 512:
                return True
    elif one_conf.get("centerList"):
        for conf in one_conf.get("centerList"):
            if conf.get("config").get("taskManagerMemory") > 512:
                return True
    return False

def parse_json():
    with open(os.path.join(os.path.dirname(__file__), "storage_task.json"), "r", encoding="utf-8")  as f:
        all_conf = json.load(f)
    return all_conf

def formate_print(one_conf):
    if one_conf.get('advanceConfig'):
        task_conf = json.loads(one_conf.get('advanceConfig'))
        task_name = task_conf.get("dataSetAlias")
        msg = f"{task_name}"
        for conf in task_conf.get("store", []):
            msg += f"   分片数{conf.get('numPartitions')}内存：{conf.get('taskManagerMemory')}M"
    else:
        task_name = one_conf.get("dataSetName")
        msg = f"{task_name}"
        for conf in one_conf.get("centerList"):
            msg += f"   分片数{conf.get('numPartitions')}内存：{conf.get('config').get('taskManagerMemory')}M"
    logger.info(msg)
    

if __name__ == "__main__":
    logger = init_logger(os.path.basename(__file__).strip('.py'))
    all_conf = parse_json()
    for conf_obj in all_conf.get("entity"):
        if filter(conf_obj):
            formate_print(conf_obj)
