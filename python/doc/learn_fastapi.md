### 路由匹配
```py
# {{cmdb_host}}{{cmdb_port}}/access_log/73/ 也会访问到get_access_log
@router.get("/73/")
def get_access_log2(record_id: int, db: Session = Depends(get_db)):
    """获取某个历史访问详情"""
    res = {"data": "123"}
    return create_response(200, "success", res)

@router.get("/{record_id}")
def get_access_log(record_id: int, db: Session = Depends(get_db)):
    """获取某个历史访问详情"""
    res = AccessRecord.get_access_log(record_id, db)
    return create_response(200, "success", res)
```
### 请求参数
```py
# get 请求
# {{fin_host}}{{fin_port}}/cost/cloud_server_image?a=a&c=c&b=b
@router.get("/cloud_server_image")
async def get_cloud_server_image(a, b="", db: Session = Depends(get_db)):
    pass
# a b 是查询参数的参数名 a是必填，不填会报错，b不是必填

@router.post("/estimation") # cost是整个post请求的请求体
def cost_estimation(cost: CostQuery, db: Session = Depends(get_db)):
    host_type = cost.host_type

```
### get请求把查询参数写成schema必须使用depend
```py

class QueryParams(BaseModel):
    page: int = Field(default=1, description="页码")
    page_size: int = Field(default=10, description="每页数量")
    keyword: Optional[str] = Field(default=None, description="搜索关键词")

@app.get("/items")
def list_items(params: QueryParams = Depends()):
    return {
        "page": params.page,
        "page_size": params.page_size,
        "keyword": params.keyword
    }
```
### get也能传递请求体 但是如果传了请求体就不会接受请求参数了？
### 
```py
# D:\Desktop\work\dccloud-finopsserv\app\cost\cloud_service.py
async def get_server_type(self):
    t_ins_types = asyncio.run(TencentClient.gen_type_data(self.get_region_id(region_id, False),have_types))
# 访问url报错：RuntimeError: asyncio.run() cannot be called from a running event loop
asyncio.run() 只能在主线程、无事件循环的环境中用。
在已有事件循环中（比如 Jupyter Notebook、某些 Web 框架）中调用 asyncio.run() 会报错。
应该使用
    t_ins_types = asyncio.get_event_loop().run_until_complete(TencentClient.gen_type_data(self.get_region_id(region_id, False),have_types))

  File "C:\Users\d1806\AppData\Local\Programs\Python\Python39\lib\asyncio\base_events.py", line 583, in _check_running
    raise RuntimeError('This event loop is already running')
RuntimeError: This event loop is already running
c:\Users\d1806\envs\finops\lib\site-packages\uvicorn\protocols\http\h11_impl.py:412: RuntimeWarning: coroutine 'TencentClient.gen_type_data' was never awaited      
  self.transport.close()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

```
### BackGroundTasks
```py
BackgroundTasks 是 FastAPI 提供的一个用于在响应返回后执行后台任务的功能。
主要特点
执行时机：在 HTTP 响应发送给客户端之后才执行任务
用途：
清理临时文件、发送邮件通知、记录日志、更新缓存、其他不影响响应的操作

执行顺序
路由函数执行、HTTP 响应发送给客户端、然后执行后台任务

优势
不阻塞响应：用户立即收到响应
自动管理：FastAPI 自动处理任务执行
异常安全：后台任务异常不影响已发送的响应
```
