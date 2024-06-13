# docker 的命令行参数

# run run 命令的参数
- --privileged 
大约在0.6版，privileged被引入docker。
使用该参数，container内的root拥有真正的root权限。
否则，container内的root只是外部的一个普通用户权限。
privileged启动的容器，可以看到很多host上的设备，并且可以执行mount。
甚至允许你在docker容器中启动docker容器。
- -detach Runs the current container in the background, known as "detached" mode, and outputs the container ID. If you do not specify this option, then the running Docker log for this container is displayed in the terminal window.
- docker run <image> <command> 
  - docker run ubuntu echo "Hello, Docker!" 这将在容器中执行该命令，并随后容器会结束运行，因为 Docker 容器在指定命令执行完毕后便会自动退出。

# exec
docker exec -it name_or_id sh # 使用的容器的的sh 也支持使用路径指定shell的位置，但在git bash下可能会出现问题