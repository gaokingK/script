# To: 介绍supervisor的使用
## link:
- http://supervisord.org

## 常识
- systemctl status supervisord
- supervisor配置文件叫supervisord.conf，supervisord和supervisorctl共用一个配置文件
- 怎么知道改把某个程序的配置文件放在哪里呢？
    - supervisorctl status 查看所有的进程
    - find / -name "上面的某个进程名字" 2>/dev/null 这样就找到了
## 启动supervisor
    - supervisord 就只有这个命令
    - 或者systemctl restart supervisor or service supervisor restart
## 命令 命令使用supervisorctl 关键字
- supervisordctl status 查看所有进程运行状态 
- supervisorctl update 更新（supervisor的配置和程序的配置）
- supervisorctl start xxx 应用程序文件中的配置名不是配置文件的名字
- supervisorctl tail -f xxx 显示该应用的日志（是tail 该应用配置文件中stdout_logfile的值）
## 错误
- 错误分为supervisorctl的错误（比如配置文件错误等）和程序错误
- 配置文件错误可以通过supervisorctl status 查看 考虑日志权限错误，是不是配置文件中user指定的用户没有相关日志文件的权限呢

## 应用程序配置文件解析
```cs
[program:x]：配置文件必须包括至少一个program，x是program名称，必须写上，不能为空
command：包含一个命令，当这个program启动时执行
process_name：进程起一个名字，格式：%(program_name)s
numprocs：启动个数，默认1
directory：执行子进程时supervisord暂时切换到该目录
user：用哪个用户启动进程，默认是root
startsecs：进程从STARING状态转换到RUNNING状态program所需要保持运行的时间（单位：秒）；启动后没有异常退出，就表示启动成功了
autorestart：程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries：启动失败自动重试次数，默认是3
priority：进程启动优先级，默认999，值小的优先启动
redirect_stderr：如果是true，则进程的stderr输出被发送回其stdout文件描述符上的supervisord
stdout_logfile：将进程stdout输出到指定文件；stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile_maxbytes：stdout_logfile指定日志文件最大字节数，默认为50MB，可以加KB、MB或GB等单位
stdout_logfile_backups：要保存的stdout_logfile备份的数量
stopasgroup：默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup：默认为false，向进程组发送kill信号，包括子进程
```

## supervisor.conf配置文件解析
```cs
[include]
files = /path/to/file/*.ini /path/to/file/.conf  # 这样可以使用多个
```
2023/09/26 15:32:22 [Warning] [2325824360] app/proxyman/outbound: failed to process outbound traffic > proxy/trojan: failed to find an available destination > common/retry: [dial tcp 185.77.225.53:443: i/o timeout dial tcp 185.77.225.53:443: operation was canceled dial tcp: lookup www.gaoking.top: operation was canceled] > common/retry: all retry attempts failed

# 问题
- supervisor.sock file missing TO：重启`systemctl restart supervisor or service supervisor restart`
- supervisor.sock refused connection
    - 是因为supervisor没启动成功
    - supervisord -c /etc/supervisord.conf

- supervisor: couldn't setuid to 0: Can't drop privilege as nonroot user
  - 由于启动supervisor的用户和program配置的用户不是同一个用户导致，将两个用户配置成相同用户即可。

- supervisor项目配置文件中的错误日志中打印：
    supervisor: couldn't setuid to 0: Can't drop privilege as nonroot user
    supervisor: child process was not spawned
    - https://blog.csdn.net/qq_31493927/article/details/110231174
    - 由于启动supervisor的用户和program配置的用户不是同一个用户导致，将两个用户配置成相同用户即可

- 启动报错supervisord -c /etc/supervisord.conf     Error: Cannot open an HTTP server: socket.error reported errno.EACCES (13)
  - sock文件权限问题
