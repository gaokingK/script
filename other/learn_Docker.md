# 准备和使用
### 产品和版本、存储引擎
- docker版本、docker-ce/docker-ee和docker-io的区别
    - link：https://blog.csdn.net/zsy_1991/article/details/90261419
    - docker-io/docker-engine是docker的早期版本、默认centos7 安装的是docker-io、版本号是1.x，docker-io的最新版本是1.13; docker-ce是新的版本分为社区版docker-ce(Docker Community Edition)和企业版docker-ee(Docker Enterprise Edition)，版本号是17.x，最新的版本是17.12
    - docker-ce 和docker-ee 的可用版本是根据year-month 来的
    - 检查是哪个版本？
        - [docker 版本号说明](https://www.cnblogs.com/lcword/p/14478791.html)
        - `docker -v` 看版本号，Docker-ce 在 17.03 版本之前叫 Docker-engine/docker-io
### 安装docker-ce
    - 参考https://mirrors.huaweicloud.com/home
    - 安装完记得启动 `service docker start `

### 简单上手
- 参照 [link](https://support.huaweicloud.com/instg-kunpengcpfs/kunpengcpfs_03_0001.html)来安装docker
- 某些环境需要配置代理
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

# 命令 https://www.runoob.com/docker/docker-command-manual.html
- 有的image用`docker run -d image_name /bin/sh` 会立马Existed，而使用`docker run -it image_name [/bin/sh]` 能进入docker，但是推出后容器也会跟着推出，这时可以使用`docker run -itd image_nume [/bin/sh] `选项
- 查看本机所有容器的Docker的服务 `docker ps -a # 可以看到我们刚刚起来的hello-world`
- 拉取指定版本的镜像`docker pull ubuntu:17.10 # 不指定版本就拉取最新的`
- 查看本地的所有镜像`docker images`
- 以指定版本的镜像启动一个容器`docker run image[:version] # 如果目标镜像没有，就会去dockerhub拉取，就像最初运行hello-world一样`

## 单行命令
- 批量删除命令 `docker ps -a|tail -n +2|head -n 1|awk '{print $1}'|xargs -i docker rm {}`
- 删除所有的exited的container `docker ps -a|grep -w Exited|awk '{print $1}'|xargs -i docker rm {}`
- `docker top android_1 | grep com.hexin | awk '{print $2;exit}`
- `docker exec -it android_1 sh -c "ps -a|grep com.hexin" | awk '{print $2;exit}'`

## 容器生命周期管理
- docker create 创建一个新的容器但不启动它；
```cs
runoob@runoob:~$ docker create  --name myrunoob  nginx:latest      
09b93464c2f75b7b69f83d56a9cfc23ceb50a48a9db7652ee4c27e3e2cb1961f 
# 创建完成后可以通过docker ps -a 查看，状态为created
```
## 容器操作
- docker start 和docker container start 没有任何区别，前者是早期的命令，后者是后来引入的命令，旨在让docker的命令的结构更加清晰易懂，docker container 包含了所有和docker 容器相关的操作命令如start、stop、run、ps等，现在二者都能一直使用
- docker ps -a 查看所有状态的容器
- docker start/stop/restart [OPTIONS] CONTAINER [CONTAINER...] 启动/停止/重启容器
- run和start的区别
    - docker run 只在第一次运行时使用 ，将镜像放到容器中，以后再次启动这个容器时，只需要使用命令docker start 展开
- docker ps -a 查看某个容器的port列的内容是8080/tcp, 0.0.0.0:2376->2376/tcp, 50000/tcp 请问这代表什么意思呢
  - 8080/tcp 这意味着容器内的 8080 端口已经开放，允许通过 TCP 协议进行访问。但是，这个端口没有映射到 Docker 主机上的任何端口，所以不能从 Docker 主机外部直接访问这个端口。
  - 0.0.0.0:2376->2376/tcp 这代表容器内的 2376 端口被映射到了 Docker 主机的 2376 端口。0.0.0.0:2376 表明 Docker 主机上的 2376 端口将绑定到所有的网络接口，这样容器的 2376 端口就可以从任何远程地址访问。
  - ->2376/tcp 指的是所有发送到 Docker 主机的 2376 端口的 TCP 流量都会被转发到容器的 2376 端口。
  - 50000/tcp 表示容器打开了 50000 端口，使用的是 TCP 协议，但同样没有进行端口映射，所以它只能在 Docker 主机或者 Docker 网络内部其他容器访问，不能从外部访问。
## 镜像
- Simple Tags and Shared Tags [link](https://github.com/docker-library/faq#whats-the-difference-between-shared-and-simple-tags)
- 删除镜像 `docker rmi hello-world`
- 搜索镜像 `docker search httpd`
- export、import、save、load
    - [link](https://www.hangge.com/blog/cache/detail_2411.html)
    - docker export  命令根据容器 ID 将镜像导出成一个文件。
        - 可以从远程导出docker export $(docker create python:3-alpine) | tar -C django -xf
## other
- ### [docker19.03限制容器使用的内存资源](https://www.cnblogs.com/architectforest/p/12586336.html)

