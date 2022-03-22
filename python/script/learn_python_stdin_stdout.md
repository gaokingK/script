# 标准输入与标准输出
## link
- https://www.cnblogs.com/clover-toeic/p/5491073.html
## 重定向标准输出
```
import sys
savedStdout = sys.stdout  #保存标准输出流
with open('out.txt', 'w+') as file:
    sys.stdout = file  #标准输出重定向至文件
    print 'This message is for file!'

sys.stdout = savedStdout  #恢复标准输出流
print 'This message is for screen!'
```
