# To: 查看某个进程使用的各种资源

## 查看内存
- cat /proc/pid/status VmRSS对应的值就是物理内存占用
- top -p 2913 看cpu和内存占用百分比 

### ps
- jps 显示java进程的
- -p 
- ps -ef/ aux/ -aux的区别
   - link: 
      - https://www.cnblogs.com/sexybear/p/Linux_ps.html
      - 不同：https://blog.csdn.net/qq_36025814/article/details/122232571
   - 显示的风格不同;aux会截断命令,如果后面配合grep可能会影响效果;
   - 都显示全部的系统进程和用户进程，但是列不一样，-aux会显示cpu和mem占用信息
   - PID    进程ID（Process ID）
   - PPID    父进程的进程ID（Parent Process id）
   - RSS 进程使用的驻留集大小或者是实际内存的大小，Kbytes字节。
- -u user_name 显示user_name用户的进程
  - 不过没有ps -aux |grep user_name显示的信息多 
  - 不能使用 ps -u username -ax
- uf
    - u：用户格式，显示与用户（owner）相关的信息，例如进程的所有者（USER）、用户ID（UID）、进程使用的CPU百分比（%CPU）、内存使用百分比（%MEM）等。
    - f：full-format，提供更详细的进程信息，包括进程之间的父子关系（PPID）、进程的启动时间、进程状态等。
```cs
root:# ps aux
USER      PID       %CPU    %MEM    VSZ    RSS    TTY    STAT    START    TIME    COMMAND

```
