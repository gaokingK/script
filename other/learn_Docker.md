### 简单命令
- 有的image用`docker run -d image_name /bin/sh` 会立马Existed，而使用`docker run -it image_name [/bin/sh]` 能进入docker，但是推出后容器也会跟着推出，这时可以使用`docker run -itd image_nume [/bin/sh] `选项
- 查看本机所有容器的Docker的服务 `docker ps -a # 可以看到我们刚刚起来的hello-world`
- 拉取指定版本的镜像`docker pull ubuntu:17.10 # 不指定版本就拉取最新的`
- 查看本地的所有镜像`docker images`
- 以指定版本的镜像启动一个容器`docker run image[:version] # 如果目标镜像没有，就会去dockerhub拉取，就像最初运行hello-world一样`
- 下午搬服务器，后续更新
#### [docker19.03限制容器使用的内存资源](https://www.cnblogs.com/architectforest/p/12586336.html)
### 镜像
- Simple Tags and Shared Tags [link](https://github.com/docker-library/faq#whats-the-difference-between-shared-and-simple-tags)
- #### 镜像管理
    - 删除镜像 `docker rmi hello-world`
    - 搜索镜像 `docker search httpd`
### 脚本
- 批量删除命令 `docker ps -a|tail -n +2|head -n 1|awk '{print $1}'|xargs -i docker rm {}`
- 删除所有的exited的container `docker ps -a|grep -w Exited|awk '{print $1}'|xargs -i docker rm {}`

### 问题
- docker也可虚拟化？
- 这里的 交付
    > Docker 是一个用于开发，交付和运行应用程序的开放平台
- 使用alpine 基础镜像build新镜像的时候出错
    ```bash
    # Dockerfile
    FROM python:3.7-alpine
    ...
    RUN pip install --no-cache-dir -r requirements.txt

    # requirements.txt
    django==2.2.13
    beautifulsoup4==4.8.2
    lxml
    pillow==6.2.2
    pyppeteer==0.0.25
    loguru==0.4.1
    djangorestframework==3.9.1

    # 错误日志
    [root@localhost MrDoc]# docker build -t mrdoc-python-3.7-alpine:test .
    Sending build context to Docker daemon  49.43MB
    Step 1/6 : FROM python:3.7-alpine
    ---> e449f233097e
    Step 2/6 : WORKDIR /usr/src/app
    ---> Running in 0f5653a61c4b
    Removing intermediate container 0f5653a61c4b
    ---> c4a37bec703b
    Step 3/6 : RUN mkdir -p ~/.pip
    ---> Running in cfa91edb7415
    Removing intermediate container cfa91edb7415
    ---> c404b5f81e44
    Step 4/6 : RUN echo -e '[global]\nindex-url = https://repo.huaweicloud.com/repository/pypi/simple\ntrusted-host = repo.huaweicloud.com\nproxy = http://ptaishanpublic2:Huawei123@90.90.64.10:8080\ntimeout = 120' > ~/.pip/pip.conf
    ---> Running in 169d4a621d62
    Removing intermediate container 169d4a621d62
    ---> 8a4fbb86c6d6
    Step 5/6 : COPY requirements.txt ./
    ---> 6cb507d584cf
    Step 6/6 : RUN pip install --no-cache-dir -r requirements.txt
    ---> Running in 6241095809e0
    Looking in indexes: https://repo.huaweicloud.com/repository/pypi/simple
    Collecting django==2.2.13
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/fb/e1/c5520a00ae75060b0c03eea0115b272d6dc5dbd2fd3b75d0c0fbc9d262bc/Django-2.2.13-py3-none-any.whl (7.5 MB)
    Collecting beautifulsoup4==4.8.2
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/cb/a1/c698cf319e9cfed6b17376281bd0efc6bfc8465698f54170ef60a485ab5d/beautifulsoup4-4.8.2-py3-none-any.whl (106 kB)
    Collecting lxml
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/c5/2f/a0d8aa3eee6d53d5723d89e1fc32eee11e76801b424e30b55c7aa6302b01/lxml-4.6.1.tar.gz (3.2 MB)
        ERROR: Command errored out with exit status 1:
        command: /usr/local/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-0qbseg16/lxml/setup.py'"'"'; __file__='"'"'/tmp/pip-install-0qbseg16/lxml/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-pvlkcnot
            cwd: /tmp/pip-install-0qbseg16/lxml/
        Complete output (3 lines):
        Building lxml version 4.6.1.
        Building without Cython.
        Error: Please make sure the libxml2 and libxslt development packages are installed.
        ----------------------------------------
    ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
    WARNING: You are using pip version 20.2.3; however, version 20.2.4 is available.
    You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
    The command '/bin/sh -c pip install --no-cache-dir -r requirements.txt' returned a non-zero code: 1

    ```
    而如果使用python:3.7 作为基础镜像就可以build 成功
    ```bash
    # 日志的关键区别
    Step 6/6 : RUN pip install --no-cache-dir -r requirements.txt
    ---> Running in 6fed28fe1833
    Looking in indexes: https://repo.huaweicloud.com/repository/pypi/simple
    Collecting django==2.2.13
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/fb/e1/c5520a00ae75060b0c03eea0115b272d6dc5dbd2fd3b75d0c0fbc9d262bc/Django-2.2.13-py3-none-any.whl (7.5 MB)
    Collecting beautifulsoup4==4.8.2
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/cb/a1/c698cf319e9cfed6b17376281bd0efc6bfc8465698f54170ef60a485ab5d/beautifulsoup4-4.8.2-py3-none-any.whl (106 kB)
    Collecting lxml
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/9f/b1/b42206e8ad5e2180988fa97691f4d0db761775c5ce89e48d7b70e6f90c3a/lxml-4.6.1-cp37-cp37m-manylinux2014_aarch64.whl (6.7 MB)
    Collecting pillow==6.2.2
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/b3/d0/a20d8440b71adfbf133452d4f6e0fe80de2df7c2578c9b498fb812083383/Pillow-6.2.2.tar.gz (37.8 MB)
    Collecting pyppeteer==0.0.25
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/b0/16/a5e8d617994cac605f972523bb25f12e3ff9c30baee29b4a9c50467229d9/pyppeteer-0.0.25.tar.gz (1.2 MB)
    Collecting loguru==0.4.1
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/b2/f4/2c8b94025c6e30bdb331c7ee628dc152771845aedff35f0365c2a4dacd42/loguru-0.4.1-py3-none-any.whl (54 kB)
    Collecting djangorestframework==3.9.1
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/ef/13/0f394111124e0242bf3052c5578974e88e62e3715f0daf76b7c987fc6705/djangorestframework-3.9.1-py2.py3-none-any.whl (950 kB)
    Collecting pytz
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl (510 kB)
    Collecting sqlparse
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/14/05/6e8eb62ca685b10e34051a80d7ea94b7137369d8c0be5c3b9d9b6e3f5dae/sqlparse-0.4.1-py3-none-any.whl (42 kB)
    Collecting soupsieve>=1.2
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/6f/8f/457f4a5390eeae1cc3aeab89deb7724c965be841ffca6cfca9197482e470/soupsieve-2.0.1-py3-none-any.whl (32 kB)
    Collecting pyee
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/0d/0a/933b3931107e1da186963fd9bb9bceb9a613cff034cb0fb3b0c61003f357/pyee-8.1.0-py2.py3-none-any.whl (12 kB)
    Collecting websockets
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/e9/2b/cf738670bb96eb25cb2caf5294e38a9dc3891a6bcd8e3a51770dbc517c65/websockets-8.1.tar.gz (58 kB)
    Collecting appdirs
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/3b/00/2344469e2084fb287c2e0b57b72910309874c3245463acd6cf5e3db69324/appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
    Collecting urllib3
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/56/aa/4ef5aa67a9a62505db124a5cb5262332d1d4153462eb8fd89c9fa41e5d92/urllib3-1.25.11-py2.py3-none-any.whl (127 kB)
    Collecting tqdm
    Downloading https://repo.huaweicloud.com/repository/pypi/packages/bd/cf/f91813073e4135c1183cadf968256764a6fe4e35c351d596d527c0540461/tqdm-4.50.2-py2.py3-none-any.whl (70 kB)
    Building wheels for collected packages: pillow, pyppeteer, websockets
    Building wheel for pillow (setup.py): started
    Building wheel for pillow (setup.py): finished with status 'done'
    Created wheel for pillow: filename=Pillow-6.2.2-cp37-cp37m-linux_aarch64.whl size=1355447 sha256=44a63449355c4506dcdd75190a25f80a055448d654fe901f07aa8390659947ce
    Stored in directory: /tmp/pip-ephem-wheel-cache-lkjnksvr/wheels/01/aa/41/7147d3a49f839eb42d1eb303b3166ff03d003878bd09eec850
    Building wheel for pyppeteer (setup.py): started
    Building wheel for pyppeteer (setup.py): finished with status 'done'
    Created wheel for pyppeteer: filename=pyppeteer-0.0.25-py3-none-any.whl size=78362 sha256=cbf0c8ec2bbc0319f5d4611b953da182e0810e88bc6c613a4a987f99e6d50dd3
    Stored in directory: /tmp/pip-ephem-wheel-cache-lkjnksvr/wheels/49/22/73/2a03f5494665ad60988869b13538bf438c715f126b96e2ff9d
    Building wheel for websockets (setup.py): started
    Building wheel for websockets (setup.py): finished with status 'done'
    Created wheel for websockets: filename=websockets-8.1-cp37-cp37m-linux_aarch64.whl size=78914 sha256=60af95dca10ca9810c085c526f8011cdb9885c2f9430fd2f68cbe794693e6558
    Stored in directory: /tmp/pip-ephem-wheel-cache-lkjnksvr/wheels/d6/82/11/da033e89cc4669750b0ca4f6817724439b80193a8b76d68e01
    Successfully built pillow pyppeteer websockets
    Installing collected packages: pytz, sqlparse, django, soupsieve, beautifulsoup4, lxml, pillow, pyee, websockets, appdirs, urllib3, tqdm, pyppeteer, loguru, djangorestframework
    ```
    关键的原因是alpine在安装某些三方包的时候下载的是源码的压缩包(.tar.gz)，而编译这些包需要实现编译好他们的依赖
    详细信息[link](https://www.jianshu.com/p/ec789a088f1e)
### 错误
1.
    ```shell
    ➜  MrDoc-master  docker run -d --name mrdoc -p 10086:10086 jonnyan404/mrdoc-alpine
    7b09ea58fbffd0e3e8964fd7571c9d5dc1fcf9b349d2018be85050e37dc2bfed
    docker: Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "process_linux.go:430: container init caused \"write /proc/self/attr/keycreate: permission denied\"": unknown.
    # 解决办法
    # 关闭 SELinux 及防火墙
    setenforce 0
    systemctl stop firewalld
    systemctl disable firewalld
    ```
2. [resolve](https://blog.csdn.net/sin_geek/article/details/86736417)
    ```shell
    [root@localhost ~]# docker rmi f19b575
    Error response from daemon: conflict: unable to delete f19b575222f7 (cannot be forced) - image has dependent child images
    # resolve
    ```
### 简单上手
- 参照 [link](https://support.huaweicloud.com/instg-kunpengcpfs/kunpengcpfs_03_0001.html)来安装docker
- 需要配置代理
    ```shell
    export http_proxy='http://ptaishanpublic2:Huawei123@90.90.64.10:8080'
    export https_proxy='http://ptaishanpublic2:Huawei123@90.90.64.10:8080'
    wget https://download.docker.com/linux/static/stable/aarch64/docker-18.09.8.tgz --no-check-certificate
    ```
- 一直都很顺利，直到<code>docker run hello-world </code> 会提示错误<code>connection refused</code>
- 因为环境的差异性，需要额外配置一些东西去设置docker代理
    ```shell
    mkdir –p /etc/systemd/system/docker.service.d
    touch /etc/systemd/system/docker.service.d/https-proxy.conf
    # 文件内容如下 （分行）
    [Service]
    Environment="HTTP_PROXY=http://ptaishanpublic2:Huawei123@90.90.64.10:8080"
    "HTTPS_PROXY=http://ptaishanpublic2:Huawei123@90.90.64.10:8080"
    "NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,"
    # 重启docker服务
    systemctl daemon-reload
    systemctl restart docker
    ```


### 90.90.67.14已运行的容器
```
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                                                              NAMES
00df1c32014d        vmware/nginx-photon:1.11.13        "nginx -g 'daemon of…"   2 weeks ago         Up 2 weeks          0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:4443->4443/tcp   nginx
4d1c5817bc4e        vmware/harbor-jobservice:v1.2.2    "/harbor/harbor_jobs…"   2 weeks ago         Up 2 weeks                                                                             harbor-jobservice
1964fd917292        vmware/harbor-ui:v1.2.2            "/harbor/harbor_ui"      2 weeks ago         Up 2 weeks                                                                             harbor-ui
e30fe12489ce        vmware/registry:2.6.2-photon       "/entrypoint.sh serv…"   2 weeks ago         Up 2 weeks          5000/tcp                                                           registry
c507f4dd0bfb        vmware/harbor-db:v1.2.2            "docker-entrypoint.s…"   2 weeks ago         Up 2 weeks          3306/tcp                                                           harbor-db
c5d3e428e0e6        vmware/harbor-adminserver:v1.2.2   "/harbor/harbor_admi…"   2 weeks ago         Up 2 weeks                                                                             harbor-adminserver
101cbd32c45b        vmware/harbor-log:v1.2.2           "/bin/sh -c 'crond &…"   2 weeks ago         Up 2 weeks          127.0.0.1:1514->514/tcp                                            harbor-log
[root@localhost ~]#
```