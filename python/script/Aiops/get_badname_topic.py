import os,json
import logging
import logging.handlers     
from openpyxl import Workbook
def init_logger(name, count=10):
    logger = logging.getLogger(__file__)
    log_level = logging.DEBUG
    formatter = logging.Formatter("%(message)s")
    log_path = os.path.dirname(__file__)

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + os.sep + 'logs' + os.sep + name + '.log'
    print("日志保存在%s" % log_name)
    ###
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight", interval=1, encoding='utf-8', backupCount=count)
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

filename = f"{os.path.basename(__file__).strip('.py')}"
logger = init_logger(name=filename)

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "get_badname1.json"),encoding='utf-8') as f:
        all_conf = json.load(f)
    res_file = os.path.join(os.path.dirname(__file__), "get_badname.xlsx")
    
    res = []
    wb = Workbook()
    ws = wb.active
    ws.append(["任务名称", "输出topic", "数据中心"])
    for conf in all_conf:
        res.append({"dataSetName": conf.get("dataSetName"),
                    "outTopicName":conf.get("outTopicName"),
                    "centerName":conf.get("centerName")})
        # if conf.get("outTopicName").upper() != conf.get("outTopicName"):
        if conf.get("outTopicName").startswith("fc") or conf.get("outTopicName").startswith("an"):
            ws.append([conf.get("dataSetName"),conf.get("outTopicName"),conf.get("centerName")])
        else:
            logger.info(f"{conf.get('dataSetName')}    {conf.get('outTopicName')}    {conf.get('centerName')}")
    wb.save(res_file)

