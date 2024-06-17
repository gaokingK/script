import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent import futures
import socket
from urllib.parse import urlparse
import urllib3
import schedule
import logging
import os
import logging
import logging.handlers
import time
import queue
import threading
import json
from inspect import isclass

#!/aiops/python/python-3.8.13/bin/python3.8
from peewee import Model, DatabaseProxy, SQL,  chunked, \
    AutoField, CharField, IntegerField, DoubleField, DateTimeField

proxy_db = DatabaseProxy()

import logging
from playhouse.shortcuts import model_to_dict
# from models.cbs import SparseForecastRecord, SparseAlarmConf, \
#     CbsBaseBand, CbsForecastResult, chunked, MySQLDatabase, proxy_db

auto_create = SQL("DEFAULT CURRENT_TIMESTAMP")
auto_update = SQL("ON UPDATE CURRENT_TIMESTAMP")
# 总表
# id 主键
# base_url # 该条url是在哪个主页爬取到的 
# domain_count 有多少个域名
# ipv6_count # ipv6域名
# ipv4_count
# ipv6_precent 该主页的ipv6浓度
# create_time 该行插入时间
class UrlDnsRes(Model):
    class Meta:
        database = proxy_db
        table_name = 't_url_dns_res'

    id = AutoField(help_text='自增ID')
    base_url = CharField(max_length=256, help_text='该条url是在哪个主页爬取到的')
    domain_count = IntegerField(help_text="门户页下的域名数量")
    ipv6_count = IntegerField(help_text="门户页下的ipv6域名数量")
    ipv4_count = IntegerField(help_text="门户页下的ipv4域名数量")
    ipv6_precent = DoubleField(help_text="该主页的ipv6浓度")
    create_time = DateTimeField(index=True, constraints=[auto_create], help_text='创建时间')



# 明细表
# id 主键
# base_url # 该条url是在哪个主页爬取到的 
# url 爬取到的url
# domain 爬取到的url的域名
# is_ipv6 是否支持ipv6 是的话就是1
# ipv6 域名的ipv6地址，如果没有则为空
# ipv6_precent 该主页的ipv6浓度
# create_time 该行插入时间
class UrlDnsResDetail(Model):
    class Meta:
        database = proxy_db
        table_name = 't_url_dns_res_detail'

    id = AutoField(help_text='自增ID')
    base_url = CharField(max_length=256, help_text='该条url是在哪个主页爬取到的')
    url = CharField(max_length=256, help_text='爬取到的url')
    domain = CharField(max_length=256, help_text='爬取到的url')
    is_ipv6 = IntegerField(help_text="是否支持ipv6 是的话就是1")
    ipv6 = CharField(max_length=256, help_text='域名的ipv6地址，如果没有则为空')
    ipv6_precent = DoubleField(help_text="该主页的ipv6浓度")
    create_time = DateTimeField(index=True, constraints=[auto_create], help_text='创建时间')



class MysqlHandler:
    def __init__(self, conf):
        # db = MySQLDatabase(**conf)
        # self.proxy_db = DatabaseProxy()
        # proxy_db.initialize(db)
        # self.db = db
        self.create_all_tables(UrlDnsRes)
        self.create_all_tables(UrlDnsResDetail)

    def close(self):
        self.db.close()

    def is_model(self, model):
        return isclass(model) and issubclass(model, Model)


    def create_all_tables(self, model):
        if model.table_exists():
            return
        ###
        try:
            model.create_table(safe=True)
        except Exception as ex:
            logging.error(f"create table failed on {model}")
            logging.exception(ex)


    @staticmethod
    def __record_data(model, rows):
        try:
            for chunk in chunked(rows, 1000):
                model.insert_many(chunk).on_conflict_ignore().execute()
        except Exception as e:
            logging.exception(e)
            logging.error(f'表记录插入异常, model_name: {model.__name__}, rows: {rows}')

    def record_url_dns_res(self, rows):
        model = UrlDnsRes
        self.__record_data(model, rows)
    
    def record_url_dns_res_detail(self, rows):
        model = UrlDnsResDetail
        self.__record_data(model, rows)




def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(thread)d) (%(filename)s:%(funcName)s:%(lineno)d) %(message)s")
    log_path = os.path.dirname(__file__)

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + "\\" + name + '.log'
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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""
输入：base_urls，下钻层级n
输出：支持ipv6的url列表，支持ipv4的url列表，ipv6浓度
1、提取base_urls下的url列表，如果提取多层，再对url进行下钻，得到urls
2、检测urls是否支持ipv6协议-> ipv4=[], ipv6=[]
3、计算ipv6浓度：ipv6_count/all_count
检测范围：上海银行官网，个人网银，企业网银
"""

class SpeedSpider:
    def __init__(self):
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                          'Chrome/80.0.3987.149 Safari/537.36',
            "Content-Type": "application/json",
            }
        self.encoding = 'utf-8'
        self.end_event=threading.Event()
        self.need_dns_url = queue.Queue() # 待检测的ipv4v6的域名
        self.all_domain=set()
        self.dnsed_domain=set()
        self.dnsed_url=set()
        self.spidered_url = set() 
        self.need_spider_url=set()  # 待爬取url的网址
        self.ipv4_domain = set()
        self.ipv6_domain = set()

    def thread_pool(self, function, urls):
        """线程池加速爬虫"""
        # max_workers: 设置线程池中最多能同时运行的线程数目
        executor = futures.ThreadPoolExecutor(max_workers=20)
        all_task = [executor.submit(function, url) for url in urls]
        # as_completed方法是阻塞的，会等行程池中的所有任务执行完毕，用result方法获取结果
        return [future.result() for future in futures.as_completed(all_task)]

    def ipv6_access_check(self):
        while not self.end_event.is_set() or not self.need_dns_url.empty():
            try:
                url = self.need_dns_url.get(timeout=5)

                # 首先获取域名AAAA解析地址，也就是ipv6地址
                aaaa = ""
                logger.info(f"解析{url}")
                # 解析出url的域名
                domain = urlparse(url).hostname
                if domain in self.dnsed_domain:
                    logger.info(f"{url}的域名为{domain}已解析过")
                    return None
                self.dnsed_domain.add(domain)

                print(f"{url}解析出来的domain是{domain}")
                # socket.getaddrinfo返回结果示例：
                # [(<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:c1:6800::19', 0, 0, 0)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:780:4000:1::7', 0, 0, 0))]
                aaaa = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
                if aaaa == "":
                    logger.info(f"{url}不支持ipv6访问，不支持解析AAAA地址。")
                    self.ipv4_domain.add(domain)
                else:
                    logger.info(f"{url}的ipv6为{aaaa}")
                    self.ipv6_domain.add(domain)
            except queue.Empty:
                logger.info("待dns的url为空")
                continue
        # 如果出现异常，说明不支持ipv6访问
            except Exception as e:
                logger.error(f"dns出错:{url}")
                logger.exception(e)
                return self.ipv4_domain.add(domain)


    def should_spider(self,url):
        blocked_extensions = ['.jpg', '.jpeg', '.zip', '.gif', '.pdf', ".msi" ".tar", ".gz", ".xls", ".exe", ".apk"]
        return not any(url.lower().endswith(ext) for ext in blocked_extensions)

    def extract_urls_from_page(self, url):
        """提取所请求url下的所有url列表"""
        href_all = []
        # 发送HTTP请求
        try:
            if not self.should_spider(url):
                logger.warning(f"url为资源链接，跳过：{url}")
                return href_all

            response = requests.get(url, headers=self.headers, timeout=10, verify=False,allow_redirects=True)
            # 检查请求是否成功
            if response.status_code == 200:
                # 解析HTML内容
                soup = BeautifulSoup(response.text, 'html.parser')
                # 找到所有的<a>标签，里面会包含链接
                all_link = soup.find_all("a")
                for link in all_link:
                    href = link.get('href')
                    # 确保链接是有效的，并且以http开头（或者相对链接）
                    if href and (href.startswith('http') or href.startswith('/')):
                        # 如果是相对链接，则转换为绝对链接
                        if not href.startswith('http'):
                            href = urljoin(url, href)
                        href_all.append(href)
                logger.info(f"爬取成功:{url}")
            else:
                logger.error(f"请求出错: {response.status_code}，url:{url}")
        except Exception as e:
            logger.error(f"爬取出错{url}")
            logger.exception(e)
        
        return href_all

    def multi_depth_extract_urls(self, urls, depth=1):
        """下钻多层url"""
        self.need_spider_url.update(urls)

        for i in range(depth):
            logger.info(f"开始提取第{i+1}层")

            ex_urls = self.thread_pool(self.extract_urls_from_page, self.need_spider_url)[0]
            # #保留包含bosc或bankofshanghai的地址
            bosc_urls = [item for item in ex_urls if 'bosc' in item or 'bankofshanghai' in item]

            self.spidered_url.update(self.need_spider_url)
            self.need_spider_url = set(bosc_urls)  - self.spidered_url 
            logger.info(f"提取出的bosc_urls共{len(set(bosc_urls))}个, 准备爬取{self.need_spider_url}")
            
            for url in bosc_urls:
                self.need_dns_url.put({index_url: url})
                self.dnsed_url.add(url)
            
            if not self.need_spider_url:
                logger.warning("待爬取的url为空")
                break
        else:
            logger.info(f"剩余未爬取的url:{self.need_spider_url}")

    def calculate_ipv4v6(self):
        logger.info(f"ipv4的地址列表: {self.ipv4_domain}")
        logger.info(f"ipv6的地址列表: {self.ipv6_domain}")
        logger.info(f"探测到的域名为{self.dnsed_domain}")
        logger.info(f"共探测到{len(self.dnsed_url)}个地址, 共{len(self.dnsed_domain)}个域名， 其中ipv6有{len(self.ipv6_domain)}个, ipv6的浓度为: {len(self.ipv6_domain) / len(self.dnsed_domain) * 100:.2f}%")

# 张天天

if __name__ == '__main__':
    # all_urls = [['https://www.bosc-hk.com/'], ['http://www.boscinternational.com/', 'http://www.bosc.cn/'],
    # ["https://www.bosc.cn/zh/"]
    conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ipv4v6.json")
    with open(conf_path) as f:
        conf = json.load(f)
    l_t = time.time()
    urls = conf["urls"]
    depth = conf["depth"]
    mysql_conf = conf["PARAM_FOR_MYSQL"]
    ss = SpeedSpider()
    SS = MysqlHandler(mysql_conf)
    producer_thread = threading.Thread(target=ss.multi_depth_extract_urls, args=(urls, depth))
    producer_thread.start()

    con_threads = []
    for i in range(1):
        consumer_thread = threading.Thread(target=ss.ipv6_access_check)
        consumer_thread.start()
        con_threads.append(consumer_thread)

    
    producer_thread.join()
    ss.end_event.set()
    for t in con_threads:
        t.join()
    ss.calculate_ipv4v6()
    print(f"span time{time.time()-l_t}")

