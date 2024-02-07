#### curl
- [curl的用法指南](https://www.ruanyifeng.com/blog/2019/09/curl-reference.html)
- 不带有任何参数时，curl 就是发出 GET 请求。
- -s 参数将不输出错误和进度信息。
- -S 参数指定只输出错误信息，通常与-s一起使用。
- -k 数指定跳过 SSL 检测。不会检查服务器的 SSL 证书是否正确。
- -x 参数指定 HTTP 请求的代理。
- -X参数指定 HTTP 请求的方法。
- -F 上传文件：
    - curl  -F "file=@/apt/new_worker_alert_conf.json" https://a938-140-206-192-11.ngrok-free.app/alerts/update_conf
    - https://blog.csdn.net/zhu19950215/article/details/88387426
- -g/--global 禁用网址序列和范围的使用`{}和[]`

#### wget
- link: https://linuxtools-rst.readthedocs.io/zh-cn/latest/tool/wget.html
- -O,  --output-document=文件      将文档写入 FILE 用来重命名
- -c,  --continue                  断点续传下载文件
- -q 安静模式
- 如果在浏览器中点击下载需要同意某些协议才能下载的资源，直接使用wget下载的就是不同意协议下载的资源
- 从sftp文件服务器下载文件`wget -q --http-user=root --http-password=Backdoor123! http://10.240.99.204/boslog/test.sh -O /boslog/aac`
- 下载 FTP 指定文件 /aaDir/aa.txt, 以 bb.txt 命名保存 不能下载sftp，可能是需要指定端口
```cs
wget ftp://192.168.0.100/aaDir/aa.txt \
     --ftp-user "user" \
     --ftp-password "passwd" \
     -O "bb.txt"

### sftp
- link:https://www.cnblogs.com/linn/p/4171208.html
- sftp root@10.48.30.192:/root/test.sh（直接将192上的文件复制到本地）
- sftp user@ip:/path 会打开会话，然后使用get put来上传下载文件
```
