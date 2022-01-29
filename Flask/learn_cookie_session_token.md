# link
- [Flask学习笔记: cookie](https://blog.csdn.net/feit2417/article/details/80735527)
- [session](https://blog.51cto.com/douya/2151255)
- [jwt简单介绍](https://blog.csdn.net/weixin_45439324/article/details/103371604)

# cookie
## flask 中使用cookie
```
# 设置cookie,默认有效期是临时cookie,浏览器关闭就失效, 可以通过 max_age 设置有效期， 单位是秒
from flask import make_response, request
resp = make_response("success")  # 设置响应体
resp.set_cookie("Itcast_1", "python_1", max_age=3600) # 设置cooke
reps.delete_cookie("username") # 删除cookie
return resp
cookie = request.get_cookies # 获取所有cookie
key = cookie.get("key", "")
request.cookies.get("key", "")
```

# session
## flask 中使用session
- 操作session就如同操作字典！
```
# 设置session相关配置
app.config['SECRET_KEY'] = os.urandom(24)                       #使用一组随机数对session进行加密
session.permanent = True # 可以通过给app.config设置PERMANENT_SESSION_LIFETIME来更改过期时间，这个值的数据类型是datetime.timedelay类型。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)   #修改session 过期时间 

# 设置session
session['username'] = 'hinzer'
print(type(session)) # <class 'werkzeug.local.LocalProxy'>
 
# 删除session
session.clear()  # 清楚所有
session.pop() 

# 获取session
username = session.get('username', "")
```

# JWT(Json Web Token)
使用Flask-jwt或 PyJWT 
## 为什么用JWT
## JWT的组成
- ![](https://img-blog.csdnimg.cn/20191203165305270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQzOTMyNA==,size_16,color_FFFFFF,t_70)
- JWT由三部分组成"header.PayLoad.signature" # xxxxx.yyyy.zzzz
- Header： 头部用于描述关于该JWT的最基本的信息，例如其类型以及签名所用的算法等。 JSON内容要经Base64 编码生成字符串成为Header。
- 载荷（PayLoad）
    - payload的五个字段都是由JWT的标准所定义的。
    - iss: 该JWT的签发者
    - sub: 该JWT所面向的用户
    - aud: 接收该JWT的一方
    - exp(expires): 什么时候过期，这里是一个Unix时间戳
    - iat(issued at): （开始生效的时间）
    - 自己定义的字段
- 签名（signature）
    - 这部分则是对第二部分完成后拼接成功的值，进行加密加盐，接着进行base64编码，以此来防止恶意用户构造token来进行身份伪造 JWS的主要目的是保证了数据在传输过程中不被修改，验证数据的完整性。但由于仅采用Base64对消息内容编码，因此不保证数据的不可泄露性。所以不适合用于传输敏感数据。
## 使用PyJWT
- link： https://www.cnblogs.com/chnmig/p/10143324.htm
```
import jwt
import datetime

dic = {
    'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间 会被编码为时间戳
    'iat': datetime.datetime.now(),  #  开始时间
    'iss': 'lianzong',  # 签名
    'xxx': {  # 内容，一般存放该用户id和开始时间
        'a': 1,
    },
    "xxx": "xxx"
}
s = jwt.encode(dic, 'secret', algorithm='HS256')  # 加密生成字符串
print(s) # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDUzMDI5OTIsImlhdCI6MTU0NTIxNjU5MiwiaXNzIjoibGlhbnpvbmciLCJkYXRhIjp7ImEiOjEsImIiOjJ9fQ.pSq-XRcC-E7zeg3u0X6TsKdhhsCPh3tB40_YJNho8CY
s = jwt.decode(s, 'secret', issuer='lianzong', algorithms=['HS256'])  # 解密，校验签名
print(s) # 源数据dic
print(type(s)) # <class 'dict'>
```
## 问题
- jwt.exceptions.DecodeError: Not enough segments
  - 因为JWT由三部分组成"header.PayLoad.signature"如果jwt.decode(token)中的token没有点分割，就会报错