# 放到定时任务中删除autotest_dir中的文件
# * 11 * * * sh /home/huawei/autotest_dir/delete_file_regular.sh
delete_path=/home/huawei/autotest_dir/
log_file_name=${delete_path}delete_file.log

echo "$(date) delete dirs:\n" >>${log_file_name}
find /home/huawei/autotest_dir/ -type d -ctime +7 >>${log_file_name}
find /home/huawei/autotest_dir/ -type d -ctime +7 | xargs -i rm -rf {}

if [ $? -ne 0 ]
then    
        echo "删除命令出现错误"
        exit 1
fi
        


