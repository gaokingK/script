from log_util import init_logger
import requests
import os,json
import re

logger = init_logger(os.path.basename(__file__).strip('.py'))


def do_request(method, url, headers, payload=None):
    try:
        headers.update({"Cookie":"JSESSIONID=BE1C215E9AD2ABD606B1A2FE83A1BF67"})
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False
    
def get_attm():
    url = "http://10.232.97.191:8888/api/v1/base-oss/attachments"
    payload = {
        "vuId": "ecd3f0aa79514e60b0e7d70e2fe1c4b7",
        "fieldIds": [
            "0b063873016b4482a530296ee5ad35eb-fieldAttachment"
        ]
        }
        
#         # "vuId": "985bdf284e784c58af9160196d1b4299",
#         # "fieldIds": [
#         #     "0b063873016b4482a530296ee5ad35eb-fieldAttachment"
#         # ]
#     }
    header = {"content-type": "application/json"}
    res = do_request("POST", url, header, payload)
    return res

def d_file(info):
    file_name = os.path.join("E:\\Deskop\\tmp4", info['name'])
    if os.path.exists(file_name):
        logger.info(f"{file_name} is exist,break")
        return
    req = requests.get(f"http://10.232.97.191:8888/oss{info['key']}")
    # file_name = os.path.join("E:\\Deskop\\tmp2", ".".join(info['name'].split('.')[:2]))

    with open(file_name, "wb") as f:
        f.write(req.content)




if __name__ == "__main__":

    attms = get_attm()
    # 0b063873016b4482a530296ee5ad35eb
    for attms_info in attms.get("resultValue").get("0b063873016b4482a530296ee5ad35eb-fieldAttachment"):
        d_file(attms_info)
