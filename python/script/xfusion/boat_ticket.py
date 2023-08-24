# coding=utf-8
import os
import json
import math
from time import sleep
import logging
import requests
import datetime
from requests.packages import urllib3

LOG_FORMAT = "%(asctime)s - %(filename)s - %(funcName)s(%(lineno)d) - %(levelname)s: %(message)s"
fh_debug = logging.FileHandler("book_car_debug.log", encoding='utf-8')
fh_debug.setLevel(logging.DEBUG)
fh_info = logging.FileHandler("book_car_info.log", encoding='utf-8')
fh_info.setLevel(logging.INFO)
logging.basicConfig(handlers=[fh_debug, fh_info], level=logging.DEBUG, format=LOG_FORMAT)  # 如果有不一样的，比如format不一样，会用fh的


class AutoBook:
    def __init__(self):
        self.book_date = ""  # 预约的时间
        self.launch_date = ""  # 开始发送的时间 比如预约24号的，就要在23号开始预约
        self.get_date()
        urllib3.disable_warnings()
        self.item_index = 0
        self.url_dict = {"showGroupInfo": "https://api.ccore.cc/group/showGroupInfo",  # GET
                         "saveOrUpdate": "https://api.ccore.cc/record/v2/saveOrUpdate",
                         "cancel": "https://api.ccore.cc/record/delete"
                         }

        self.data_info = {"access_token": "1570937481111212034",
                          "appointId": "1501824148991008769",  # 驾校id
                          "carManagerId": "1501834378151878658"  # 陈教练 卢教练：id1503315595447656449
                          }
        self.first_book_id = ""
        # os.environ['NO_PROXY'] = 'api.ccore.cc'
        # os.environ['http_proxy'] = 'http://127.0.0.1:8080'
        # os.environ['https_proxy'] = 'http://172.16.67.168:8080'
        os.environ['https_proxy'] = "http://proxy.xfusion.com:8080"  # 写对应的ip地址的话会需要验证
        # self.proxy = {"http": "http://proxy.xfusion.com:8080", "https": "http://proxy.xfusion.com:8080"}
        # curl --location --request GET "https://www.baidu.com" -x "http://172.16.67.168:8080" -k
        self.check_data()
        logging.debug("init over")

    def add_book(self):
        headers = {"access_token": self.data_info["access_token"]}
        # form_data数据
        payload = {
                    # "itemId": "1502555129412091906",
                    "itemId": self.first_book_id,
                    "itemDate": self.book_date,
                    "appointId": "1501824148991008769",
                    "carManagerId": "1501834378151878658"
        }
        while True:
            try:
                res = requests.post(url=self.url_dict["saveOrUpdate"], data=payload,headers=headers, verify=False, timeout=10)
                content_json = res.json()
                if content_json.get("success") != True:
                    logging.info("request faild: \n %s" % content_json)
                    continue
                logging.info("request success: \n %s" % content_json)
                break
            except Exception as e:
                logging.exception("request faild")

    def get_group_info(self):
        """
        显示某天的预约列表
        :return:
        """
        headers = {"access_token": self.data_info["access_token"]}
        params = {"appointId": self.data_info["appointId"],
                  "activeDate": self.book_date,
                  "carManagerId": self.data_info["carManagerId"]}
        # url = "https://api.ccore.cc/group/showGroupInfo?appointId=1501824148991008769&activeDate=2023-02-20&carManagerId=1503315595447656449"
        # res = requests.request("GET", url, headers=headers, data=payload, verify=False)
        while True:
            try:
                res = requests.get(url=self.url_dict["showGroupInfo"], params=params, headers=headers, verify=False, timeout=10)
                content_json = res.json()
                if content_json.get("success") != True:
                    logging.info("request faild: \n %s" % content_json)
                    continue
                logging.info("request success: \n %s" % content_json)
            except Exception as e:
                logging.exception("request faild")

            try:
                config_items = content_json.get("content").get("configItems")
                self.first_book_id = config_items[self.item_index].get("id")
                logging.info("%s %dth book_id: %s" % (self.book_date, self.item_index, self.first_book_id))
                break
            except Exception as e:
                logging.exception(e)

    def scheduler(self):

        while True:
            end_time = datetime.datetime.strptime("%s 08:10:00" % self.launch_date, "%Y-%m-%d %H:%M:%S")
            start_time = datetime.datetime.strptime("%s 07:59:00" % self.launch_date, "%Y-%m-%d %H:%M:%S")
            # end_time = datetime.datetime.strptime("%s 20:48:00" % self.launch_date, "%Y-%m-%d %H:%M:%S")
            # start_time = datetime.datetime.strptime("%s 19:53:10" % self.launch_date, "%Y-%m-%d %H:%M:%S")
            current_date = datetime.datetime.now()
            self.get_group_info()
            if current_date > end_time:
                break
            if current_date > start_time:
                self.add_book()
                sleep(3)  # 59秒的时候就能预约好
                logging.info("要预约date：%s已经成功, 计算下次预约时间" % self.book_date)
                self.get_date()
                logging.info("计算结束要预约的date是：%s, 准备开始运行的日期是%s" % (self.book_date, self.launch_date))
            else:
                self.ice(current_date, start_time)

    def ice(self, current_t:datetime.datetime, melt_time:datetime.datetime):
        span = melt_time - current_t
        logging.debug("现在(%s)距离开始(%s)还有:%s,开始sleep" % (current_t, melt_time, span))
        if span.seconds < 60:
            print("sleep %s-%s" % (span.seconds, int(span.seconds)+1))
            sleep(int(span.seconds)+1)
        for i in range(math.floor(span.seconds/60)):
            logging.debug("共需沉睡%s次,开始第%s次sleep(60)" % (math.floor(span.seconds/60), i+1))
            sleep(60)

    def check_data(self):
        if self.item_index != 0:
            print("没有预约8点的")
            logging.warning("没有预约8点的")
            # raise Exception("没有预约8点的")

    def get_date(self):
        d = datetime.datetime.now()
        logging.info("d.hour:%s点" % d.hour)
        if d.hour >= 8:
            # self.book_date = (d+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            # self.launch_date = d.strftime("%Y-%m-%d")
            self.book_date = (d+datetime.timedelta(days=2)).strftime("%Y-%m-%d")
            self.launch_date = (d+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            self.book_date = (d+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        logging.info("要预约的date是：%s, 准备开始运行的日期是%s" % (self.book_date, self.launch_date))

def get_all_ticket():
    url = "https://pc.ssky123.com/api/v2/line/ship/enq"

    payload = json.dumps({
        "startPortNo": 1028,
        "endPortNo": 1010,
        "startDate": "2023-08-19",
        "accountTypeId": "0"
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'pc.ssky123.com',
        'Connection': 'keep-alive'
    }

    res = requests.request("POST", url, headers=headers, data=payload)
    content = res.json()
    pass


if __name__ == '__main__':
    # logging.info("#"*50)
    # A = AutoBook()
    # A.scheduler()
    os.environ['https_proxy'] = "127.0.0.1:10809"
    get_all_ticket()



