import requests
from multiprocessing import Process



def do_request(url, i):
    payload = ""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
        "Connection": "keep-alive"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    print(f"{url}: {response.status_code}  -{i}")

def vm_request(i):
    url = ["http://127.0.0.1:9000/overview/vm_count",
           "http://127.0.0.1:9000/overview/vm_count"]
    
    for _ in range(1):
        do_request(url[i], i)
    


if __name__ == "__main__":
    pl = []
    for i in range(2):
        p = Process(target=vm_request, args=(i,))
        pl.append(p)
        p.start()
    
    for p in pl:
        p.join()


