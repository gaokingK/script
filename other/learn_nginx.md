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