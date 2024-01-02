import requests
import json

# get_all_store_task_url = "http://10.251.52.102:18080/logAnalysis/api/itoa/dataset/storageOutPut"
# cookie = "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzAzMjI0MjY0NzQwLCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjUwNTI0MTQ4NDQ2MDEzNDQsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJKc3FpbkkxdjJwcFY4dXIxK0NTbUxITHQ1ano2WGlHVVRPWHNteTdhUkdFTWxQdG51S1Q0QlpUQ3VlMGw5SVdpVU1EMnd1dklVZmFnZ0JxRjFHaGVQTnRlNUVhbXRKa3pwNjcxTEMrVEZBYmEvUlUzcEhObllUeE5GaVBPMXFweStvQjU3UWcwU01Mb2hlM0s4Ulg3T1ZXakNVa3Rhb2FXcUM0b0R1d3podk09IiwicHJvZHVjdHMiOiJ7fSJ9.d2Luik1xJEtQDO6gR-ukMwGa1YJPWb2J-c5BNCCPXDZohDxmU__qu7_yQxbs6IboC0xGLtRCMf2nANv6BYDuKA"
# querystring = {"page":"0","from":"0","size":"200"}
# headers = {"Cookie": cookie}

# def get_other_info(data_set_id):
#     # 获取采集任务名和Topic
#     url = "http://10.251.52.102:18080/logAnalysis/api/itoa/dataset/topology"
#     querystring = {"datasetId":data_set_id,"type":"storing"}
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     res = json.loads(response.text)["entity"]["collectings"]
#     in_data_set_name = []
#     topic_name = []
#     for item in res:
#         in_data_set_name.append(item["dataSetName"])
#         topic_name.append(item["outTopicName"])
#     return "\n".join(in_data_set_name), "\n".join(topic_name)


# response = requests.request("GET", get_all_store_task_url, headers=headers, params=querystring)

# res_list = []
# all_store_list = json.loads(response.text)["entity"]
# for item in all_store_list:
#     data = {}
#     data["dataSetAlias"] = item["dataSetAlias"] # 存储任务名
#     info = get_other_info(item["dataSetId"])
#     data["in_data_name"] = info[0] # 采集任务名
#     data["topic_name"] = info[1] # topic名

#     data["center_num"] = str(len(item["centerList"])) # 中心数
#     data["dataSetName"] = item["dataSetName"] # 数据集名称/索引名
#     data["dataSetId"] = item["dataSetId"] # 存储任务id 用来查询采集任务名和Topic
#     res_list.append(data)
# with open("./res.json", "w+") as f: 
#     json.dump(res_list, f, )

with open("./python/script/RESTFull_Api/res.json", "r") as f:
    data = json.load(f)

with open("res2.json", "w+", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False)

with open("res2.json", "r", encoding="utf8") as f:
    data = json.load(f, )
    for item in data:
        item.pop("dataSetId")
        # print(item.values())
        print(":".join(item.values()))
# for item in res_list:
#     print(item)


