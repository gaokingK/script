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
#!/aiops/python/python-3.8.13/bin/python3.8

def init_logger(name, count=10):
    logger = logging.getLogger()
    log_level = logging.DEBUG
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s (%(filename)s:%(lineno)d) %(message)s")
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

    # def general(self, url):
    #     """普通请求"""
    #     response = requests.get(url, headers=self.headers)
    #     response.encoding = self.encoding
    #     if response.status_code == 200:
    #         return response.text
    def thread_pool(self, function, urls):
        """线程池加速爬虫"""
        # max_workers: 设置线程池中最多能同时运行的线程数目
        executor = futures.ThreadPoolExecutor(max_workers=6)
        all_task = [executor.submit(function, url) for url in urls]
        # as_completed方法是阻塞的，会等行程池中的所有任务执行完毕，用result方法获取结果
        return [future.result() for future in futures.as_completed(all_task)]

    def ipv6_access_check(self,url):
        # 首先获取域名AAAA解析地址，也就是ipv6地址
        aaaa = ""
        try:
            # 解析出url的域名
            domain = urlparse(url).hostname
            print(f"{url}解析出来的domain是{domain}")
            # socket.getaddrinfo返回结果示例：
            # [(<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:c1:6800::19', 0, 0, 0)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('240e:780:4000:1::7', 0, 0, 0))]
            aaaa = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
            print(aaaa)
            if aaaa == "":
                logging.info(f"{url}不支持ipv6访问，不支持解析AAAA地址。")
                return {url: False}
            else:
                logging.info(f"{url}支持ipv6访问，支持解析AAAA地址。")
                return {url: True}
        # 如果出现异常，说明不支持ipv6访问
        except Exception as e:
            logging.exception(e)
            return {url: False}
        
    def multi_thread_ipv6_access_check(self, urls):
        """多线程ipv6地址识别"""
        result = self.thread_pool(self.ipv6_access_check, urls)
        print(result)
        ipv4 = []
        ipv6 = []
        for res in result:
            for key, value in res.items():
                if value is True:
                    ipv6.append(key)
                else:
                    ipv4.append(key)
        return ipv4, ipv6
    

    def extract_urls_from_page(self, url):
        """提取所请求url下的所有url列表"""
        href_all = []
        # 发送HTTP请求
        try:
            response = requests.get(url, headers=self.headers, timeout=10, verify=False,allow_redirects=True)
            logging.info(f"请求返回码: {response.status_code}")
            # 检查请求是否成功
            if response.status_code == 200:
                # 解析HTML内容
                soup = BeautifulSoup(response.content, 'html.parser')
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
            else:
                logging.error(f"Failed to retrieve the page. Status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Error occurred: {e}")
        return href_all



    def multi_depth_extract_urls(self, urls, depth=1):
        """下钻多层url"""
        # 创建空列表用于存放提取到的url
        all_urls = [[]] * (depth+1)
        all_urls[0]= urls
        visited_urls = set()
        for i in range(depth):
            logging.info(f"开始提取第{i+1}层")
            ex_urls = self.thread_pool(self.extract_urls_from_page, all_urls[i])[0]
            #保留包含bosc或bankofshanghai的地址
            bosc_urls = [item for item in ex_urls if 'bosc' in item or 'bankofshanghai' in item]
            logging.info(f"提取出的bosc_urls共{len(bosc_urls)}个, {bosc_urls}")
            visited_urls.update(all_urls[i])
            validurls = list(set(bosc_urls) -visited_urls)
            if validurls == []:
                break
            all_urls[i+1] = validurls
            logging.info(f"validurls: {len(validurls), validurls}")
            logging.info(f"all_urls: {all_urls}")
        return all_urls




    def calculate_ipv4v6(self, urls, depth):
        all_urls=self.multi_depth_extract_urls(urls, depth)
        # all_urls = [['https://www.bosc-hk.com/'], ['http://www.boscinternational.com/', 'http://www.bosc.cn/'], ["https://www.bosc.cn/zh/sy/khfw/lxwm/"]]
        check_urls = []
        for i in range(depth+1):
             if all_urls[i] != []:
                check_urls.extend(all_urls[i])
                logging.info(f"所有待检测的urls: {check_urls}")
        ipv4, ipv6 = self.multi_thread_ipv6_access_check(check_urls)
        logging.info(f"ipv4的地址列表: {ipv4}")
        logging.info(f"ipv6的地址列表: {ipv6}")
        logging.info(f"共探测到{len(check_urls)}个地址, 其中ipv6有{len(ipv6)}个, ipv6的浓度为: {len(ipv6) / len(check_urls)}")



if __name__ == '__main__':
    # soup = BeautifulSoup(a, "html.parser")
    # logging.info(f'current environment: {env}')
    # all_urls = [['https://www.bosc-hk.com/'], ['http://www.boscinternational.com/', 'http://www.bosc.cn/'],
# ["https://www.bosc.cn/zh/sy/khfw/lxwm/"]]
    l_t = time.time()
    conf = {"urls": ["http://www.bosc.cn/zh/"],
            "depth": 4
            }
    urls = conf["urls"]
    depth = conf["depth"]
    ss = SpeedSpider()
    ss.ipv6_access_check("http://www.bosc.cn/cn")
    

    # ss.calculate_ipv4v6(urls, depth)
    print(f"span time{time.time()-l_t}")
    # timeStart = time.time()
    # schedule.every().sunday.at("16:15").do(
    #     ss.calculate_ipv4v6, urls=urls, depth=depth
    # )
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    # all_urls=ss.multi_depth(urls, depth)
    # all_urls = [['https://www.bosc-hk.com/'], ['http://www.boscinternational.com/', 'http://www.bosc.cn/'],
    # ["https://www.bosc.cn/zh/sy/khfw/lxwm/"]]
    # check_urls = []
    # for i in range(depth+1):
    #     # print(all_urls[i])
    #     if all_urls[i] != []:
    #          check_urls.extend(all_urls[i])
    # print(check_urls)
    # ipv4,ipv6 = ss.multi_thread_ipv6_access_check(check_urls)
    # print(f"ipv4的地址: {ipv4}")
    # print(f"ipv6的地址: {ipv6}")
    # print(f"共探测到{len(check_urls)}个地址, 其中ipv6有{len(ipv6)}个, ipv6的浓度为: {len(ipv6) / len(check_urls)}")
    # # timeStart1 = time.time()
    # # print(time.time() - timeStart1)

