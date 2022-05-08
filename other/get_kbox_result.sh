
ssh huawei@90.90.0.111 ""
cd /home/huawei/Desktop/autotest/;find . -type d -name "*$(date +%Y%m%d)*" -o -name "*$(date +%Y%m%d)*.txt" |tar -zcvf 111back.tar.gz -T -&&scp 111back.tar.gz huawei@90.90.0.152:/home/huawei/Desktop/smoke/.