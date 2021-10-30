# scp xml
# 检查参数 --------------no
# echo $0 $1 $2 $3
# $3 是目的路径 怎样使用${var:?=''} 来
# echo "scp huawei@90.90.0.$1:$2 /home/huawei/Desktop/a.$(echo $2|awk -F . '{print $NF}')"
scp huawei@90.90.0.$1:$2 /home/huawei/Desktop/a.$(echo $2|awk -F . '{print $NF}')