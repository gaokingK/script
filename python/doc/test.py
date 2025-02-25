import datetime
# from apscheduler.schedulers.background import BackgroundScheduler

def job_func(text2):
    print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, {text2}')

# scheduler = BackgroundScheduler()
# # 每隔两分钟执行一次 job_func 方法
# scheduler.add_job(job_func, args=('interval',), misfire_grace_time=10)
# # 在 2017-12-13 14:00:01 ~ 2017-12-13 14:00:10 之间, 每隔两分钟执行一次 job_func 方法
# # scheduler.add_job(job_func, 'interval', minutes=2, start_date='2017-12-13 14:00:01' , end_date='2017-12-13 14:00:10')

# scheduler.start()
# print("other task")

data = {"a": {"a":"1"}}


def updata_data(data):
    data["b"] = []
    # return data

# updata_data(data["a"])
# print(data)


def format_tags(tags_data, load=True):
    """处理tags;load=True 将数据转换为前端喜欢的"""
   
    if load:
        res = []
        for key, value in tags_data.items():
            res.extend([{"key": key, "value": v} for v in value])
        return res
    else:
        res={}
        for data in tags_data:
            if data["key"] not in res:
                res[data["key"]] = [data["value"]]
            else:
                res[data["key"]].append(data["value"])
        return res
    
if __name__ == "__main__":
    tags = [
					{
						"key": "Market",
						"value": "上海"
					},
					{
						"key": "Ownership",
						"value": "DL"
					},
					{
						"key": "Ownership",
						"value": "CL"
					}
				]
    print(format_tags(tags, False))
