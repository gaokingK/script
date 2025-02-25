# flask其他组件问题
- app.register_blueprint(assign_task, url_perfix="/assign_task") 能接受关键字参数，所以参数名写错也不会报错，这里url_perfix写错了就导致路由未注册成功。
- return get_response(xxx) 如果service 中raise BadRequest会报错 说接受2个参数却给了三个
```
# 是因为werkzeug版本不一样，换成同样的版本就好了
      Successfully uninstalled Werkzeug-2.0.3
ller.py][line 26] - {'username': 'adm2in', 'password': '111111'}                                       │Successfully installed Werkzeug-1.0.1

```
### 查看动态地获取某个 URL 对应的处理函数
```py
# 获取 URL 规则和 endpoint 名称
url_rule, endpoint = app.url_map.bind('/').match(return_rule=True)

# 获取 endpoint 对应的处理函数
view_func = app.view_functions[endpoint]
```
### 解决循环导入的问题
```py
with app.app_context():
    # 注册蓝图

    from .store.views import store_bp
    api_bp.register_blueprint(store_bp, url_prefix='/stores')
```
# flask 路由模糊匹配
- [Python Flask详解正则匹配路由](https://blog.csdn.net/weixin_42008209/article/details/80368492)


# falsk 自带服务器启动
- 所有都能访问 `app.run(host="0.0.0.0", port=5010, debug=True)`
  - `2022-02-19 16:53:27,103 - INFO -  * Running on http://7.249.232.144:5010/ (Press CTRL+C to quit)`
  - localhost:5010 
  - 上面的日志的地址也能访问(但不是在百度中查到的本机地址)
  - 局域网内的地址也可访问 90.90.0.224:5010
- conf 文件改动并不会时debug中的服务自动重启
# response
- link:
  - https://www.cnblogs.com/lyg-blog/p/9332609.html
```
# 方法一
response = Response(json.dumps({"a": "b"}), content_type="applications/json", status=404)
# 方法二
response = make_response(json.dumps({"a": "b"}), 405)
response.headers["Content-Type"] = "applications/json"
return response
```
# python requests
## link
  - [python接口自动化20-requests获取响应时间(elapsed)与超时（timeout）](https://www.cnblogs.com/yoyoketang/p/8035428.html)
```
with requests.post(url=url, cookies=cookie, verify=False) as result:
    account = result.json().get("userId")
    if account:
        return account
    logger.info("The cookie is expired")
    return False
方式二
try:
    req = requests.patch(req_url,
                          body_json,
                          auth=(bmc_user, bmc_password),
                          headers=headers,
                          verify=False)

    result = {
        "status": req.status_code,
        "headers": req.headers,
        "rt": req
    }
    break
except requests.HTTPError:
    time.sleep(3)
```
## requests 超时时间
- link：https://www.cnblogs.com/yoyoketang/p/8035428.html
```
res = requests.get(url=f"{record_server}/record", data=json.dumps({"duration_time": duration_time}), timeout=5
必须在5s内收到相应报文
```

## [requests获取结果](https://www.cnblogs.com/lanyinhao/p/9634742.html)
```
r.encoding                       #获取当前的编码
r.encoding = 'utf-8'             #设置编码
r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
r.status_code                     #响应状态码
r.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
r.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功
 #*特殊方法*#
r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
r.raise_for_status()             #失败请求(非200响应)抛出异常
```

### Flask如何保证线程安全
[关于flask线程安全的简单研究](https://www.cnblogs.com/fengff/p/9087660.html)
简单结论：处理应用的server并非只有一种类型，如果在实例化server的时候如果指定threaded参数就会启动一个ThreadedWSGIServer，而ThreadedWSGIServer是ThreadingMixIn和BaseWSGIServer的子类，ThreadingMixIn的实例以多线程的方式去处理每一个请求
只有在启动app的时候将threded参数设置为True，flask才会真正以多线程的方式去处理每一个请求。


### 项目结构
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── auth.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── templates/
│   │   ├── layout.html
│   │   └── home.html
│   └── static/
│       ├── css/
│       └── js/
│
├── config.py
├── requirements.txt
├── migrations/
└── run.py
### 自定义异常
- https://www.cnblogs.com/se7enjean/p/12955417.html
