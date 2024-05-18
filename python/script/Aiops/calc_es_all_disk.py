# 计算es集群的磁盘资源
import json

def main(json_path):
    total=float()
    avaliable = float()
    with open(json_path, "r+", encoding='utf-8') as f:
        data = json.load(f).get("body")
    for item in data:
        total += item.get("disk", {}).get("total")
        avaliable += item.get("disk", {}).get("available")
    return total, avaliable


if __name__ == "__main__":
    path = "res2.json"
    total, avaliable = main(path)
    total = total/1024/1024/1024/1024
    avaliable = avaliable/1024/1024/1024/1024
    print(f"磁盘总空间:{total}T, 可用空间:{avaliable}T, 占用率为{(1-avaliable/total)*100}%")



