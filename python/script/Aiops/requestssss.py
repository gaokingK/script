from log_util import init_logger
import requests
import os,json
logger = init_logger(os.path.basename(__file__).strip('.py'))


def do_request(method, url, headers, payload=None):
    try:
        headers.update({"Cookie":"JSESSIONID=36DAD01D416BD2B1D7F22C8B2F594BBF"})
        res = requests.request(method, url=url, headers=headers, json=payload)
        res = res.json()
        return res
    except Exception as e:
        logger.exception(e)
        return False
    
def get_attm():
    url = "http://10.232.97.191:8888/api/v1/base-oss/attachments"
    payload = {
        "vuId": "437d68e2b84547bea893bd129f9e1515",
        "fieldIds": [
            "0b063873016b4482a530296ee5ad35eb-fieldAttachment"
        ]
    }
    header = {"content-type": "application/json"}
    res = do_request("POST", url, header, payload)
    return res

def d_file(info):
    req = requests.get(f"http://10.232.97.191:8888/oss{info['key']}")
    file_name = ".".join(info['name'].split('.')[:2])
    with open(info['name'], "wb") as f:
        f.write(req.content)

if __name__ == "__main__":
    attms = get_attm()
    for attms_info in attms.get("resultValue").get("0b063873016b4482a530296ee5ad35eb-fieldAttachment"):
        d_file(attms_info)
