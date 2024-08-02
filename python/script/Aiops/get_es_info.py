
from log_util import init_logger
import requests
import os,json
logger = init_logger(os.path.basename(__file__).strip('.py'))

def get_es_index_info(cluster_name = "zj"):
    """
    获取es集群的overview信息
    """
    conf = {
        "zj": {
            "url": "http://10.251.52.102:18080/cerebro/overview",
            "host": "http://10.239.64.13:29202",
            "username": "elastic",
            "password": "Aiops_2022"
        },
        "sq": {
            "url": "http://10.251.52.102:18080/cerebro/overview",
            "host": "http://10.207.64.26:29202",
            "username": "elastic",
            "password": "Aiops_2022"
        },
        "dev":{ # 测试管理区，待修改
            "url": "http://10.251.52.102:18080/cerebro/overview",
            "host": "http://10.207.64.26:29202",
            "username": "elastic",
            "password": "Aiops_2022"
        }
    }
    if cluster_name == "dev":
        info = load_es_info(file_name="dev_es_info.json")
        if "dev" not in info.keys():
            dump_es_info(es_info={"dev":info}, file_name="dev_es_info.json")
        return
    payload = conf[cluster_name]
    url = payload.pop("url")
    header = {"content-type": "application/json"}
    res = requests.request("POST", url, headers=header, json=payload)
    if res.json().get("status") == 200:
        res = res.json()
        dump_es_info(es_info={cluster_name:res.get("body")})
        return res.get("body").get("indices")
    else:
        logger.error(f"获取{cluster_name}es信息失败")

def dump_es_info(file_name="prod_es_info.json", es_info=None):
    """
    es_info: dict => {"zj": es_info_dict}
    待修改
    """
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    if not os.path.isfile(file_path):
        with open(file_path, "w+") as f:
            f.write("{}")
    with open(file_path, "w+") as f:
        json.dump(es_info, f)
    # with open(file_path, "r+") as f:
    
        # all_es_info = json.load(f)
        # if es_info:
        #     f.seek(0)
        #     all_es_info.update(es_info)
        #     json.dump(all_es_info, f)
        # return all_es_info

def load_es_info(file_name="prod_es_info.json"):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    if not os.path.isfile(file_path):
        with open(file_path, "w+") as f:
            f.write("{}")
    with open(file_path, "r+") as f:
        all_es_info = json.load(f)
    return all_es_info

def calc_es_index_pro(all_index_info):
    """
    格式化es的数据
    """
    calc_res = {}
    for cluster_name,value in all_index_info.items():
        for index_info in value.get("indices"):
            index_name = index_info.get("name")
            name = index_name.split("_eoi")[0]
            if "eoi" in index_name:
                date = index_name.split("_eoi_")[-1]
            else:
                date = "total"
            size = round(index_info['size_in_bytes']/1024/1024/1024, 2)
            doc_count = index_info['doc_count']
            if doc_count:
                doc_size = round(index_info['size_in_bytes']/1024/doc_count,2)
            else:
                doc_size = 0
            index_info = {date: {"size": size, "doc_count":doc_count, "doc_size": doc_size}}
            
            if not calc_res.get(name,{}).get(cluster_name):
                # calc_res.update({name:{cluster_name:[index_info]}})
                calc_res.update({name:{cluster_name:index_info}})
            else:
                calc_res.get(name).get(cluster_name).update(index_info)
    # 排序
    for index_name,info_c in calc_res.items():
        for clu_name, info in info_c.items():
            calc_res[index_name][clu_name] = dict(sorted(info.items()))
            date_list = sorted(filter(lambda x:"_"in x, info.keys()))
            calc_res[index_name][clu_name].update({"date_list":date_list})

            # 计算额外数据
            if len(date_list):
                last_day = {"date": date_list[-1],
                            "doc_count": info[date_list[-1]].get("doc_count"),
                            "doc_size": info[date_list[-1]].get("doc_size"),
                            "doc_count_sec": round(info[date_list[-1]].get("doc_count")/86400,2)}
                calc_res[index_name][clu_name].update({"last_day": last_day})
                doc_count, doc_size = 0,0
                for date in date_list[-1:-8:-1]:
                    doc_size += info[date]["size"]
                    doc_count += info[date]["doc_count"]
                doc_count_sec = round(doc_count/7/86400,2)
                doc_size = doc_size/doc_count*1024*1024 if doc_count else 0
                calc_res[index_name][clu_name].update(
                    {"last_7_day": {"doc_count": doc_count/7,
                                    "doc_size": doc_size,"doc_count_sec":doc_count_sec,
                                    }})

    dump_es_info("calc_es_res.json", calc_res)

    return calc_res



if __name__ == "__main__":
    # get_es_index_info("sq")
    # get_es_index_info("zj")
    # get_es_index_info("dev")
    # 获取石泉和张江和测试管理区的es_info
    all_index_info = {}
    for file in ["prod_es_info.json", "dev_es_info.json"]:
        all_index_info.update(load_es_info(file))

    calc_es_index_pro(all_index_info)

    # with open(os.path.join(os.path.dirname(__file__), "es_index.json"), "r", encoding='utf-8') as f:
    #     all_data = json.load(f)
