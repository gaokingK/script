### 字典的value方法不能直接取值
```py
payload.get("region_id", params["region_id"].values())
# 必须要这样
payload.get("region_id", list(params["region_id"].values())[0])
```
