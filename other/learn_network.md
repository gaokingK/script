# 协议
- httpdoc: https://developer.mozilla.org/zh-CN/docs/web/http/overview 
# http 状态码
## link
- https://www.runoob.com/http/http-status-codes.html
## 总分类
1**	信息，服务器收到请求，需要请求者继续执行操作
2**	成功，操作被成功接收并处理
3**	重定向，需要进一步的操作以完成请求
4**	客户端错误，请求包含语法错误或无法完成请求
5**	服务器错误，服务器在处理请求的过程中发生了错误
## 常见状态码
200 - 请求成功
301 - 资源（网页等）被永久转移到其它URL
304 - 
401 - 用户需要登录
404 - 请求的资源（网页等）不存在
405 
500 - 内部服务器错误

# 网络安全
注意没有100%的安全，就像你的密码被人盗了，他能100%伪装成你一样。
## 跨站请求伪造（ CSRF ）
- 使用cookie会造成CSRF, 本质原因是他伪造的请求中有cookie，而这个cookie是浏览器层面的原因。所以采用类似session的一次性令牌可以解决，但是如果他把你session拿走了，就像把你的密码拿走了
# 网络问题
- 内网穿透：https://blog.csdn.net/qq_45878803/article/details/121651477
- ngrok
- 不是从局域网访问，而是可以从公网访问 ngrok需要一直运行
- 启动命令 ngrok http 8000

### 开启端口允许外部访问 
link:
	- windows https://blog.csdn.net/lm_is_dc/article/details/118335869
- 控制的维度不仅有端口、还有该端口使用的协议、该端口是入站还是出站、来源主机的ip、来源主机的用户、都可以设置
### 网络访问不了 https://www.maketecheasier.com/fix-no-route-to-host-error-linux/
- 先看dns有没有 /etc/resolv.conf

# 常识
- http 基于tcp协议
# 套接字
在网络通信中，"监听"和"非监听"套接字表示套接字（socket）的两种状态。

## 监听套接字（Listening Socket）：

当一个程序（通常是服务器程序）在某个特定的端口上等待来自其他程序的连接请求时，它会创建一个监听套接字。
这个套接字处于"监听状态"，等待来自客户端的连接请求。
服务器程序通过监听套接字接受客户端的连接，并创建一个新的套接字来处理该连接。这个新的套接字用于与客户端进行实际的数据通信。
## 非监听套接字（Non-Listening Socket）：

一旦连接建立，套接字进入"非监听状态"，也称为"已建立状态"。
在已建立状态下，数据可以在客户端和服务器之间进行双向通信。
对于客户端和服务器之间的每个连接，都会有一个对应的非监听套接字。
示例：

服务器端：服务器创建一个监听套接字用于接受连接请求。
客户端：客户端连接到服务器的监听套接字，建立一个非监听套接字用于实际的数据传输。
在 netstat -an 的输出中，你会看到一些套接字的状态。"LISTEN" 表示该套接字是一个监听套接字，而其他状态（例如 "ESTABLISHED"）表示已建立的非监听套接字，正在进行数据传输。


# netstat 查看端口 # 端口管理 打开端口 # port
   - 端口是否被占用`lsof -i 8080`
     - link: https://www.runoob.com/w3cnote/linux-check-port-usage.html
     - 应该用root来执行，否之看不到
   - netstat -tunlp 用于显示 tcp，udp 的端口和进程等相关情况。`netstat -tunlp | grep 8000`
     - link:https://zhuanlan.zhihu.com/p/367635200 
     - -t (tcp) 仅显示tcp相关选项Administrator  
     - -u (udp)仅显示udp相关选项
     - -l 仅列出在Listen(监听)的服务状态
     - -anp：显示系统端口使用情况
     - -n（--numeric）: 显示网络地址和端口号为数字形式，而不是尝试将它们解析为主机名、服务名称等。这可以提高显示速度，避免查询 DNS 服务器。
     - -a（--all）: 显示所有选项，默认情况下，netstat 命令不显示监听（LISTEN）状态的套接字信息。使用 -a 选项，可以显示所有活动的和非活动（监听状态）的连接和监听端口。netstat -an |grep 7788 显示有多少个连接在7788上
     - -p（--program）: 显示每个套接字关联的进程标识号 (PID) 和程序名称。这对于确定哪个程序建立了哪个连接或监听了哪个端口非常有用。 因为 -p 参数需要访问进程信息，因此在大多数系统上，你需要以 root 用户执行 netstat -nap 命令来查看所有进程的相关信息。
   - 获取正在使用的端口 netstat -ntl |grep -v Active| grep -v Proto|awk '{print $4}'|awk -F: '{print $NF}' 
   - 打开端口
      - link：https://www.cnblogs.com/sxmny/p/11224842.html
      - systemctl start firewalld 开启防火墙 
      - firewall-cmd --zone=public --add-port=1935/tcp --permanent # 开放指定端口
         - --zone #作用域
         - --add-port=1935/tcp  #添加端口，格式为：端口/通讯协议
         - --permanent  #永久生效，没有此参数重启后失效
      - systemctl restart firewalld.service
      -  firewall-cmd --reload 重启防火墙
   - 测试端口连通性 https://www.cnblogs.com/lijinshan950823/p/9376085.html
      - curl ip:port 如果远程主机开通了相应的端口，都会输出信息，如果没有开通相应的端口，则没有任何提示，需要CTRL+C断开。。
      - wget ip:port
      - telnet ip port 
      - ip 也可以是域名 curl  https://cee6-140-206-192-11.ngrok-free.app 不用加端口
   - firewall-cmd --zone=public --list-ports 查看开放的端口
      - https://blog.csdn.net/s_frozen/article/details/120636667
   - 查询指定端口是否已开启 firewall-cmd --query-port=3306/tcp 提示 yes，表示开启；no表示未开启。
   - 端口不仅受防火墙控制，还受iptable规则控制
# iptables
- link: 
   - 使用：https://www.cnblogs.com/wanstack/p/8351718.html
   - 查看已有的规则：https://www.cnblogs.com/wanstack/p/8351209.html
- iptables -L -n 查看规则
- -L <链名> 查看链得规则，如果省略就看所有链得
- -t 指定表名
- -v选项，查看出更多的、更详细的信息
   - pkts:对应规则匹配到的报文的个数。
   - bytes:对应匹配到的报文包的大小总和。
   - target:规则对应的target，往往表示规则对应的"动作"，即规则匹配成功后需要采取的措施。
   - prot:表示规则对应的协议，是否只针对某些协议应用此规则。
   - opt:表示规则对应的选项。
   - in:表示数据包由哪个接口(网卡)流入，我们可以设置通过哪块网卡流入的报文需要匹配当前规则。
   - out:表示数据包由哪个接口(网卡)流出，我们可以设置通过哪块网卡流出的报文需要匹配当前规则。
   - source:表示规则对应的源头地址，可以是一个IP，也可以是一个网段。
   - destination:表示规则对应的目标地址。可以是一个IP，也可以是一个网段。
- 保存规则：
   - centos6中，使用"service iptables save"
   - centos7: iptables-save > /etc/sysconfig/iptables

# 网段、子网掩码计算方法
- https://blog.csdn.net/yzpbright/article/details/81384559
