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
- -O,  --output-document=文件      将文档写入 FILE
- -c,  --continue                  断点续传下载文件