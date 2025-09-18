import random
import string

import pandas as pd
import numpy as np
import csv
import json
import time

import logging
import logging.handlers
import os
import pickle


def init_logger(name, count=10):
    logger = logging.getLogger(__file__)
    log_level = logging.DEBUG
    formatter = logging.Formatter("%(message)s")
    log_path = os.path.dirname(__file__)

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + os.sep + name + '.log'
    logger.info("日志保存在%s" % log_name)
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


class Store:
    # 保证一定程度的分散
    # 集群增加多少个变成参数
    # 不是看的集群的平均度
    def __init__(self, id, market, do, ownership, bu=None):
        self.id = id          # 门店ID
        self.market = market  # 省份 获取该市场在每个集群的数量，计算出平均指标，计算出放进去后会最平均的一个集群
        self.do = do
        self.bu = bu          # 业务单位 不考虑这个分
        self.cluster = ""
        self.ownership = ownership  # 所有权类型（直营/DL/CL） 获取该类型在每个集群的数量，计算出平均指标，计算出放进去后会最平均的一个集群
        # 负责人 do 把机器分散到已有的集群里 获取该负责人在每个集群的数量，计算出平均指标，计算出放进去后会最平均的一个集群
        # 分别计算出省份、所有权类型、负责人这三个指标的平均指标、决定按哪一个去分配（是选择平均度最小的一个去分配，还是先按三个指标都分配一次，选择分配后最平均的一个结果呢）
        # 如何计算每个指标的平均指标 计算方差 平均值是指标的门店数量/集群数量 实际值是每个集群的数据
        # TODO 分配结果在该属性上是平均的，但是其他属性的平均指标会不会增高呢


class Cluster:
    def __init__(self, id):
        self.id = id
        self.stores = []  # 门店列表
        self.markets = set()  # 市场集合
        self.dos = set()  # DO
        self.ownerships = set()  # 所有权集合

    @property
    def store_count(self):
        return len(self.stores)

    @property
    def cluster_name(self):
        return f"Cluster{self.id}"

    def market_count(self, market):
        return len([s for s in self.stores if s.market == market])

    def do_count(self, do):
        return len([s for s in self.stores if s.do == do])

    def ownership_count(self, ownership):
        return len([s for s in self.stores if s.ownership == ownership])

    def add_store(self, store):
        self.stores.append(store)
        store.cluster = self.cluster_name
        self.markets.add(store.market)
        self.dos.add(store.do)
        self.ownerships.add(store.ownership)

    def __str__(self):
        return f"Cluster {self.id}: {self.store_count} stores, Markets: {self.markets}, Ownership: {self.ownerships}, Do: {self.dos}"

# TODO 分配直营门店的逻辑时 因为会判断集群里要有cl和dl的，会新建门店，如果都是直营，那就会创建n个集群
# TODO 如果最初就分配的是直营门店，那么前三个集群里即使没有内容，也还是会创建一个新的集群
# TODO 后面新增门店do/ownership/market会在前面的门店出现过吗？如果没有出现，那这些数据就会不均匀


def check_cluster_capacity(standard_cap=512, add_count=None):
    all_store_count = 0
    for c in clusters:
        all_store_count += c.store_count
    
    if add_count:
        if all_store_count/(len(clusters) * standard_cap) > 0.8:
            logger.info(f"在门店总数{all_store_count}时新建了{add_count}个集群")
            get_distribute_res()
            for _ in range(add_count):
                clusters.append(Cluster(len(clusters)+1))
            record_current_dis()
    

    if not add_count and add_chance:
        chance = add_chance[0]
        if chance.get("store_count", float("inf")) < all_store_count:
            add_count = chance.get("add_count", 0)
            logger.info(f"在门店总数{all_store_count}时新建了{add_count}个集群")
            for _ in range(add_count):
                clusters.append(Cluster(len(clusters)+1))
            add_chance.remove(chance)
            get_distribute_res()
            record_current_dis()
            

def check_cluster(cluster_index):
    # TODO 是否可以这里不做校验，而是检查所有集群都大于一个值时去创建集群呢
    cluster = clusters[cluster_index]
    if cluster.store_count < 512:
        return True


def choice_good_cluster(distribution, cluster_c):
    """
    :param distribution: 某个门店的三个维度的平均指标
    :return:
    """
    for item in distribution:
        dis = item.get("data")  # 该维度在每个集群的数量
        com_data = {i: dis[i] * cluster_c[i] for i in range(len(dis))}
        com_data = sorted(com_data, key=lambda x:com_data.get(x))
        for i in com_data:
            if check_cluster(i):
                return i
        else:
            return com_data[0]

def cluster_index_generator():
    i = 0
    while i > -1:
        res = i % len(clusters)
        yield res
        i += 1

def get_distribution(store: Store):
    """获取当前门店各维度的分布"""
    market_dis, do_dis, ownership_dis, ever_clu_count = [], [], [], []
    for c in clusters:
        market_dis.append(c.market_count(store.market))
        do_dis.append(c.do_count(store.do))
        ownership_dis.append(c.ownership_count(store.ownership))
        ever_clu_count.append(c.store_count)
    return market_dis, do_dis, ownership_dis, ever_clu_count


def calc_std(data):
    # 计算指标值
    avg = np.mean(data)
    std = np.std(data)
    # cv = std/avg
    return std

def serialize_cluster(dump=True):
    return 
    global clusters
    if dump:
        with open("clusters.pkl", "wb") as f:
            pickle.dump(clusters, f)
    else:
        with open("clusters.pkl", "rb") as f:
            clusters = pickle.load(f)

def record_current_dis():
    all_ownership, all_do, all_market = get_all_index_value()
    market_dis, _ = get_market_dis(all_market)
    ownership_dis, _ = get_owership_dis(all_ownership)
    do_dis, _ = get_do_dis(all_do)

def allocate_stores(stores, add_count=1, record_interval=100, dis_key="do"):
    """
    add_count: 是否按照总集群大于80%时添加集群，添加的数量，如果为0就是由add_chance决定什么时候添加
    record_interval: 在分配过程中记录数据，数值代表分配几次记录一次，如果为0代表分配的时候不记录
    dis_key: 决定根据什么方法分配门店 do：do维度；market:market维度；loop:循环往各个集群添加
    """
    for i, store in enumerate(stores):
        # serialize_cluster(dump=False)
        if add_count or add_chance:
            check_cluster_capacity(add_count=add_count)
        
        if dis_key == "loop":
            cluster_index = next(c_idx_gen)
        else:
            distribution = []
            # 挑选分布最不均匀的维度
            market_dis, do_dis, ownership_dis, ever_clu_count = get_distribution(store)
            if dis_key == "do":
                distribution.append({"data": do_dis, "var": calc_std(do_dis)})
            elif dis_key == "market":
                distribution.append({"data": market_dis, "var": calc_std(market_dis)})
            # distribution.append({"data": ownership_dis, "var": calc_std(ownership_dis)})
            # for data in get_distribution(store):
            #     distribution.append({"data": data, "var": calc_std(data)})
            # distribution = sorted(distribution, key=lambda x: x.get("var"), reverse=True)

            cluster_index = choice_good_cluster(distribution, ever_clu_count)
        clusters[cluster_index].add_store(store)
        # serialize_cluster(dump=True)
        
        # 记录数据
        if record_interval:
            if i % record_interval == 0:
                record_current_dis()
    record_current_dis()
            

def check_rule():
    # 一个do不能在一个集群
    pass


def get_all_index_value():
    all_ownership, all_do, all_market = set(), set(), set()
    for cluster in clusters:
        all_ownership = all_ownership.union(cluster.ownerships)
        all_do = all_do.union(cluster.dos)
        all_market = all_market.union(cluster.markets)
    return all_ownership, all_do, all_market


def get_market_dis(all_market, log=False):
    global all_market_dis_data
    market_var = []
    market_dis = []
    for v in all_market:
        data = []
        for c in clusters:
            count = c.market_count(v)
            market_dis.append({"cluster": c.cluster_name, "market": v, "dis": count})
            data.append(c.market_count(v))
        var = np.std(data)
        market_var.append(var)
        if log:
            logger.info(f"market维度: {v}的平均指标为: {var:.2f}, 每个集群中的分布数据: {data}")
    all_market_dis_data.append(market_dis)
    return market_dis, market_var


def get_owership_dis(all_owership, log=False):
    global all_owership_dis_data
    owership_var = []
    owership_dis = []
    for v in all_owership:
        data = []
        for c in clusters:
            count = c.ownership_count(v)
            owership_dis.append({"cluster": c.cluster_name, "owership": v, "dis": count})
            data.append(count)
        var = np.std(data)
        owership_var.append(var)
        if log:
            logger.info(f"ownership维度: {v}的平均指标为: {var:.2f}, 每个集群中的分布数据: {data}")
    all_owership_dis_data.append(owership_dis)
    return owership_dis, owership_var

def get_do_dis(all_do, log=False):
    global all_do_dis_data
    do_var = []
    do_dis = []
    for v in all_do:
        data = []
        for c in clusters:
            count = c.do_count(v)
            do_dis.append({"cluster": c.cluster_name, "do": v, "dis": count})
            data.append(count)
        var = np.std(data)
        do_var.append(var)
        if log:
            logger.info(f"do维度: {v}的平均指标为: {var:.2f}, 每个集群中的分布数据: {data}")
    all_do_dis_data.append(do_dis)
    return do_dis, do_var

def get_distribute_res(log=True):
    all_ownership, all_do, all_market = get_all_index_value()

    _, ownership_var = get_owership_dis(all_ownership, log=log)
    _, do_var = get_do_dis(all_do, log=log)
    _, market_var = get_market_dis(all_market, log=log)

    if log:
        logger.info(f"market维度平均指标为: {np.std(market_var):.2f} do维度平均指标为: {np.std(do_var):.2f} "
                    f"owner维度平均指标为: {np.std(ownership_var):.2f}")

    # 输出集群信息
    for cluster in clusters:
        logger.info(cluster)


def get_all_store(file_name, stores_count=1000):
    stores = []
    with open(file_name, "r", encoding="utf-8") as file:
        data2 = csv.DictReader(file)
        for d in data2:
            if not d.get("owner_type"):
                continue
            else:
                d["owner_type"] = {"M": "直营", "L": "CL", "J": "DL"}.get(d.get("owner_type"))
            if not d.get("market"):
                continue
            # if d.get("do_id") == "UNK":
            #     continue
            if not d.get("do_id"):
                d["do_id"] = "UNK"
            
            stores.append(Store(d.get("store_id"), d.get("market"), d.get("do_id"), d.get("owner_type")))
    return stores


if __name__ == '__main__':
    time_l = time.time()
    clusters = [Cluster(i) for i in range(1, 4)]  # 初始化3个集群
    c_idx_gen = cluster_index_generator()
    add_chance = [{"store_count": 1300, "add_count": 3}, {"store_count": 2500, "add_count": 2}, {"store_count": 3000, "add_count": 2}, {"store_count": 4000, "add_count": 4}]

    # serialize_cluster(dump=True)
    all_store = get_all_store("prod_store_info_with_do.csv")
    all_market_dis_data = []
    all_owership_dis_data = []
    all_do_dis_data = []

    allocate_stores(all_store, record_interval=600, add_count=0, dis_key="loop")
    with open("dis_data17.json", "w+") as f:
        res = {"market":all_market_dis_data, "owership": all_owership_dis_data, "do": all_do_dis_data}
        json.dump(res, f)
    get_distribute_res()
    print(f"span time: {time.time()-time_l}")

    # draw(res)

