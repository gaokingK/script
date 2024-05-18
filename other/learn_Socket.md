# socket
- socket是应用层和传输层中间抽像出来的一个层，他把TCP/IP层复杂的操作抽象为几个简单的接口供应用调用来实现进程在网络中间通信。
- ![](https://images0.cnblogs.com/blog/349217/201312/05225723-2ffa89aad91f46099afa530ef8660b20.jpg)
- 进程要想在网络中通信时采用的标识时ip+端口号+协议
# python 实现socket通信
### 通信过程
- link：https://www.cnblogs.com/dolphinx/p/3460545.html
- 服务端初始化socket： 根据socket类型、协议类型创建socket，然后为socket绑定ip和端口
- 服务端开始监听端口号，等待和客户端连接，这是socket还没有打开
- 客户端： 初始化socket
- 客户端： 根据ip+端口像服务端发起请求
- 服务端： 发现接收到客户端的socket请求，被动打开socket，等待客户端返回连接信息。这时候会进入连接阻塞状态（会阻塞在accept函数，知道接受到客户端的连接请求后该函数才会返回，客户端才能接受下一个连接请求）
- 客户端： 发送连接信息
- 服务端： 接受到连接信息，accept函数返回，连接成功
- 客户端： 发送信息
- 服务端： 接受信息
- 客户端： 关闭连接
- 服务端： 关闭连接
### 服务端
- 
### 连接阻塞状态？
启动后重新启动
查看证书 smtp有就行了
网络不通，看ipv4的配置，然后看网关、dns能不能ping通 
services.msc
### 实践
```
# 客户端
import socket
import sys


s = socket.socket()
s.connect(("127.0.0.1", 8888))
while True:
    msg = input("发送")
    if msg == "exit":
        s.close()
        sys.exit(0)
    else:
        s.send(msg.encode("utf-8"))
        msg = s.recv(1024)
        print("服务器发送了：%s" % msg)
# 服务端
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8888))

s.listen(5)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        dt = data.decode("utf-8")
        print("收到%s" % dt)
        a = input("向对方发送")
        if a == "exit":
            conn.close()
            s.close()
        else:
            conn.send(a.encode("utf-8"))
```
