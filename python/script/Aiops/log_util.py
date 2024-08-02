import logging
import logging.handlers
import os, sys, time,functools
import requests


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
    time_handler = logging.handlers.TimedRotatingFileHandler(log_name, when="midnight",interval=1,encoding='utf-8', backupCount=count)
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

def get_cookies(url,user,passwd):
    try:
        data = {
            "enableLDAP": False,
            "password": passwd,
            "userName": user
        }
        headers = {"content-type": "application/json"}
        res = requests.post(url=url, json=data, headers=headers)
    except Exception as e:
        logger.error("登录sso失败，{}".format(e))
    else:
        return res.cookies
    

def do_request(method, url, headers, payload=None):
    try:
        headers.update({"Cookie":cookie})
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False
    
logger = init_logger(os.path.basename(__file__).strip('.py'))




