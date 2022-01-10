1. ### shell 中小命令
   - id -u 判断当前用户是不是root 是root返回0 `if $(id -u) !=0`
1. #### expr 
    ```
    huawei ~/Desktop/smoke% expr 2 + 1
    3
    huawei ~/Desktop/smoke% 2 + 1     
    cd:cd:2: too many arguments
    ```
2. #### shell 数组 列表
   - [link](https://www.runoob.com/linux/linux-shell-array.html)
   ```shell 
   a = (ele1, ele2.....)
   a[index]
   a[@]/a[*] 获取所有元素
   ```
   - (shell for循环和数组应用)[https://blog.csdn.net/jk110333/article/details/7748645?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.no_search_link]
   - 数组遍历
2. #### seq 生产序列
   用法：seq [选项]... 尾数
　      或：seq [选项]... 首数 尾数
　      或：seq [选项]... 首数 增量 尾数
    ```
    for dir in 11{1..4}; do echo $dir; done
    for dir in `seq 32`; do echo $dir; done
    for dir in $array_name[@]; do echo $dir; done
    ```
3. #### 字符串
   - 获取字符串的长度
     - link: https://www.jb51.net/article/121290.htm
     - ${#str}
   - 