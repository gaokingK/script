
##### 为什么不加classmethod装饰器就访问不到cls.__name --------------no
##### pycharm 自动完成
[link](https://blog.csdn.net/migming/article/details/109978585)
##### print(1/0)会出错
##### 1. 字节字符串、Unicode字符串、打开的二进制文件对象或者打开的文本文件对象都是什么？、BOM（byte order mark)
##### 1. 为什么如下所示的yaml文件经过反序列化后再序列化得到的文件格式和原来的不一样？
[link](https://blog.csdn.net/swinfans/article/details/88770119)
```python
document = """
    a: 1
    b:
      c: 3
      d: 4
    """
print(yaml.dump(yaml.load(document)))
a: 1
b: {c: 3, d: 4}
```
因为PyYaml会根据一个集合内是否含有嵌套的集合来决定使用哪种格式来表示这个集合，如果一个集合中含有嵌套的集合
那么PyYaml会使用块样式来表示，否则就会使用流样式来表示（上面的就是流样式）可以通过`dump`的参数`default_flow_style=False`
来使用块样式


##### 1. format中的**位置参数**是一个元组，在前面引用的部分是元组的索引
```python
a = "{server}:{0}{1}".format("127.0.0.1", "8080", server="www.xxxx.cn")
```
[format 的填充对齐](https://www.cnblogs.com/lvcm/p/8859225.html)

##### 1. Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
[doc](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)
`html.parser` 是python内置的解析器

##### 1.协程看上去也是子程序，但执行过程中，在子程序内部可中断， ，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断