#!/bin/bash

# 当前主机IP
IP=10.239.84.105
# mave安装目录
MAVE_HOME=/boslog/mave

# 采集任务信息
taskinfo="
10.239.84.105:itoa-flow-156648405020672:514\n
10.239.84.105:itoa-flow-288289579163648:1515\n
10.239.84.105:itoa-flow-288309089239040:1514\n
10.207.84.105:itoa-flow-156648405020672:514\n
10.207.84.105:itoa-flow-288289579163648:1515\n
10.207.84.105:itoa-flow-288309089239040:1514\n
10.239.84.104:itoa-flow-156648998649856:1514\n
10.207.84.104:itoa-flow-156648998649856:1514\n
10.239.84.104:itoa-flow-156649210540032:514\n
10.207.84.104:itoa-flow-156649210540032:514\n
"

task=$(echo -e $taskinfo|grep $IP)
isok=0
for t in $task;do
    echo "[$(date "+%F %T")] checking $t"
    taskport=$(echo $t|cut -d":" -f3)
    taskname=$(echo $t|cut -d":" -f2)
    # 检查是否需要修改
    old_host=$(sed -n '/Input/,/\/Input/p' $MAVE_HOME/probes/$taskname/conf/flow.conf|grep "Host" |awk '{print $NF}')
    new_host="0.0.0.0"
    if [[ $old_host != "0.0.0.0" ]];then
        sed -i '/Input/,/\/Input/s/Host.*$/Host 0.0.0.0/' $MAVE_HOME/probes/$taskname/conf/flow.conf
    fi
    
    echo $(netstat -nap|grep "$new_host:$taskport")
    iswork=$(netstat -nap|grep "$new_host:$taskport"|wc -l)
    if [ $iswork -eq 1 ];then
        echo "$taskport is working"
    else
        isok=1
    fi
    if [ $isok -eq 0 ];then
        exit 0
    else
        echo "restart mave"
        $MAVE_HOME/bin/stop 
        sleep 10
        $MAVE_HOME/bin/start
    fi
done

