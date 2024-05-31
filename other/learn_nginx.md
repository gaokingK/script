# other 杂
### 正向代理与反向代理
- link
    - https://www.cnblogs.com/ysocean/p/9392908.html#_label1
- 正向代理代理客户端，反向代理代理服务器。
### 一个端口反向代理多个端口
```cs
server {
    listen 80;
    server_name example.com; 代理对外暴漏的域名或者是ip

    location /app1/ {
        proxy_pass http://localhost:8081/; //代理的地址1
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /app2/ {
        proxy_pass http://localhost:8082/; 代理的地址2
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # 可以添加更多的 location 块，每个块对应一个不同的后端服务

    # 其他配置...
}
# 注意8081末尾的反斜杠/如果一对一代理，不写反斜杠可以代理成功，如果一对多代理，不屑反斜杠就代理不成功
访问example.com/app1 会访问到8081的端口的服务，访问example.com/app2 会访问到8082的端口的服务
```
### 命令
```
/path/to/nignx/sbin/nginx -s reload 重启
/path/to/nignx/sbin/nginx -V 查看详细版本信息 -v 简略版本信息
/path/to/nignx/sbin/nginx -t 检查配置
/path/to/nignx/sbin/nginx  启动
```
### 编译脚本
### sub_filter 模块
- 可以替换响应体中的字符串，无论是否在body体内，只要是被代理的url的响应体，都可以替换
- link:
    - https://blog.csdn.net/carefree2005/article/details/121373537
    - nginx使用sub_filter指令替换字符: https://dyrnq.com/nginx-sub_filter/
```py
# 注意结尾的分号
sub_filter 'foo.com'  'dyrnq.com';
sub_filter_types *; # 指定MIME类型的字符串替换，除了“ text/html” 之外，还可以在指定MIME类型的响应中启用字符串替换。特殊值“ *”匹配任何MIME类型。
sub_filter_once on; # 指示是否查找每个字符串以替换一次或重复替换。使用语法：sub_filter_once on | off，默认on
proxy_set_header Accept-Encoding ""; # sub_filter无效 配置文件的反代规则里增加，如果还不行检查backend应用是否强制开启了gzip压缩。
```
### /nginx/sbin/stop 时遇到Nginx: [Alert] Kill (2480) failed (3:no such process) solution
- 因为结束时会杀死nginx的进程，niginx的pid放在nginx.pid文件当中，这个文件可能在/nginx/log下，如果不在就查找下，由于这个文件是从另外一台文件复制过去的，所以这个杀死的时候就找不到这个进程
- 解决办法是手动杀死当前的nginx进程 pkill nginx
- 或者把nginx.pid文件中的pid换成当前主机上nginx的pid
