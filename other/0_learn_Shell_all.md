### 规范
- 缩进统一4个空格，不要tab，其实有些地方不缩进也可以（for、if）
- 赋值时等号左右不能有空格
### shell 多行注释
   ```shell
   # 方法1 block自定义的单词（可以是字符） 推荐
   :<<！
   被注释的内容
   block
   ！
   # or
   :'
   被注释的内容
   '
   ```
### 查看swp等.开头的文件时`ls .*.swp`
### 数组
- link：
  - https://zhuanlan.zhihu.com/p/483399604
  - https://www.cnblogs.com/cheer-lingmu/p/16467290.html
- 生成序列
  - seq `seq 5 //起始默认是1，间隔默认也是1`
  - `{begin..end}` # 性能比seq快
- 生成列表
  - `alist=$(seq 5)` //alist得到的是字符串，不同之处是以空格隔开，但echo ${alist[0]} 就把全部的都数出来了，而用for是一个个输出的
  - arry=($alist) //如果需要生成array,只需要将$(seq 5)再加个“()”即可
- 列表方法
  - ${arry[@]} 列表所有元素
  - ${#arry[@]} 长度
  - ${alist[0]} 第一个元素，不能-1， 假如超过索引输出null但不报错
### 整数运算
- link:
  - https://cloud.tencent.com/developer/article/1770000
- echo ${test_a[$((5%3))]}
### set
- link:
  - https://blog.csdn.net/fw63602/article/details/52799073?utm_source=copy
- set – "$X"就是把X的值返回给$1, set – $X就是把X作为一个表达式的值一一返回
- IFS=oIFS 这样会导致’o’,‘I’,‘F’,'S’都是分隔符，应该IFS=$oFIS 
- set -- $(ls /opt)
### 各种括号
- link：https://blog.csdn.net/weixin_44794688/article/details/123138257
- 变量范围限定${}
```
# 如果变量 a 没有用{} 括起来的话，shell 就会将abc 识别为变量名
 $ a=123456
 $ echo $abc

 $ echo ${a}bc
123456bc
```
### 标准输出
```
ls > /tmp/log # > 重定位运算符 ">" 的默认参数为标准输出 stdout ，即 1 ; 所以 ">" 等价于 "1>";
# ls liqiu > /tmp/error 2>&1 #使用 " 2>&1" 把标准错误 stderr 重定向到标准输出 stdout ；
```
### 抛出异常
```
exit 1
```
### 注释
   - link：https://www.cnblogs.com/Braveliu/p/10855771.html
```
行注释使用 # 或者//
# 方式一
:<<!
!
# 方式二
if false; then
fi
```
### shell 中小命令
   - id -u 判断当前用户是不是root 是root返回0 `if $(id -u) !=0`
### expr 计算
    ```
    huawei ~/Desktop/smoke% expr 2 + 1
    3
    huawei ~/Desktop/smoke% 2 + 1     
    cd:cd:2: too many arguments
    ```
### shell 数组 列表
   - [link](https://www.runoob.com/linux/linux-shell-array.html)
   ```shell 
   a = (ele1, ele2.....)
   a[index]
   a[@]/a[*] 获取所有元素
   ```
   - (shell for循环和数组应用)[https://blog.csdn.net/jk110333/article/details/7748645?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-6.no_search_link]
   - 数组遍历
### seq 生产序列
   用法：seq [选项]... 尾数
　      或：seq [选项]... 首数 尾数
　      或：seq [选项]... 首数 增量 尾数
    ```
    for dir in 11{1..4}; do echo $dir; done
    for dir in `seq 32`; do echo $dir; done
    for dir in $array_name[@]; do echo $dir; done
    ```
### 字符串
   - 获取字符串的长度
     - link: https://www.jb51.net/article/121290.htm
     - ${#str}
   - 