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
```cs
root:# ps aux
USER      PID       %CPU    %MEM    VSZ    RSS    TTY    STAT    START    TIME    COMMAND

```