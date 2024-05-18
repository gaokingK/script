"""
# 字符串前缀 与 字符编码

## link
- https://zhuanlan.zhihu.com/p/39602759
- https://www.cnblogs.com/zhangqigao/p/6496172.html

## 字符编码
- Python3在内存中处理的字符串一般都是经过unicode编码的了的字符串
- Python2的 默认编码 是ASCII，不能识别中文字符，需要显式指定字符编码；Python3的 默认编码 为Unicode，可以识别中文字符。

## 一些问题
### 字符串前缀 r"xxxx"、u"xxxx"、b"xxxx" 都是啥意思
- r(Raw) 原始字符串，不需要识别转义, 会按照原样进行输出
    - 注意不能在原始字符串结尾输入反斜线，否则Python不知道这是一个字符还是换行符(字符串最后用\表示换行)，会报错：
- u(Unicode) 字符串前面加u是用来表明该字符串采用unicode编码
    - python2 经常使用，因为python2 默认采用AsCii编码（因为python2诞生的时候们没有Unicode）
    - 而python3默认采用UTF-8
- b(Bytes) 字符串的前面加b 用来表示该字符串是bytes类型
    - python3 经常使用，因为python3 的str默认是unicode类， python2 的str本身就是bytes类，所以可不用
    - 因为在物理存储，网络传输时，为了节省空间（包括物理空间和时间空间）需要将字符串转化为字序列对象bytearray, 按字节Bytes发送

"""

"""
To: 不同的前缀
- 使用b前缀时str中只能包含ASCII字符外的
a = b"hello你好"  # SyntaxError: bytes can only contain ASCII literal characters.
"""
def learn_str_prefix():
    print("learn_r_prefix")
    print("a\ta")
    print(r"a\ta")

    print("learn_u_prefix")
    a = b"hello"
    print(a, end="\t")
    print(type(a))
    print(a.decode('utf-8'), end="\t")
    print(type(a.decode('utf-8')))


"""

"""
