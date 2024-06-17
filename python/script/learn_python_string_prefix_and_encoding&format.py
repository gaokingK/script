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
# 前缀和编码
"""
# 字符串前缀 r"xxxx"、u"xxxx"、b"xxxx" 都是啥意思
# link: https://zhuanlan.zhihu.com/p/39602759

# r(raw) 原始字符串，不需要识别转义, 会按照原样进行输出
# 注意不能在原始字符串结尾输入反斜线，否则Python不知道这是一个字符还是换行符(字符串最后用\表示换行)，会报错：
print("learn_r_prefix")
print("a\ta")
print(r"a\ta")

# u 字符串前面加u是用来表明该字符串采用unicode编码
# python2 经常使用，因为python2 默认采用AsCii编码（因为python2诞生的时候们没有Unicode）
# 而python3默认采用UTF-8

# b 字符串的前面加b 用来表示该字符串是bytes类型
# python3 经常使用，因为python3 的str默认是unicode类， python2 的str本身就是bytes类，所以可不用
# 因为在物理存储，网络传输时，为了节省空间（包括物理空间和时间空间）需要将字符串转化为字序列对象bytearray, 按字节Bytes发送
print("learn_u_prefix")
a = b"hello"
print(a, end="\t")
print(type(a))
print(a.decode('utf-8'), end="\t")
print(type(a.decode('utf-8')))
# 这又是为什么呢？
a = b"hello你好"  # SyntaxError: bytes can only contain ASCII literal characters.
# 编码
# python编码
# 在文件开头添加 # coding:utf8
# Python在内存中处理的字符串一般都是经过unicode编码的了的字符串

# Python在物理存储、网络传输时，为节省空间（包括物理空间和时间空间），
# 需将字符串转换成字节序列对象bytearray，按字节Bytes发送。
# 0X是16进制前缀，代表后面跟的数字是16进制的
# 一些编码
#   - UTF-8 编码 直接控制台中print转换不出来
#       - &#x652F;&#x6301; &#x6C49;&#x5B57; &#x8F6C; UTF-8 &#xFF0C; &#x4E5F;&#x53EF;&#x4EE5; UTF-8&#x7F16;&#x7801; &#x8F6C; &#x6C49;&#x5B57; &#x3002; 
#       - UTF-8 转中文：https://www.sojson.com/utf8.html
#   - Unicode
#       - 十进制（print转换不出来）：&#25265;&#27465;&#65292;&#25105;&#21482;&#26159;&#19968;&#20010;&#20154;&#24037;&#26234;
#       - 16进制（转换的出来）：\u62b1\u6b49\uff0c\u6211\u53ea\u662f\u4e00\u4e2a\u4eba\u5de5\u667a
#   - 字节码 （三*8位二进制共24位）组成一个字
#       - 二进制：
#           - 1110011 01011001 010100001 没
#           - https://www.lddgo.net/convert/string-binary
#       - 16进制/HEX：
#           - e6b2a1 # 没 
#           - https://www.lddgo.net/string/hex
#           - 有时在控制台能输出、有时不能（amd64不能）print("\xe6\xb2\xa1")
"""
"""
To: 编码
"""
def byte2str():
    b = "\xe6\xb2\xa1\xe6\x9c\x89\xe9\x82\xa3\xe4\xb8\xaa\xe6\x96\x87\xe4\xbb\xb6\xe6\x88\x96\xe7\x9b\xae\xe5\xbd\x95" # 在arm上的
    print(b) # 直接就输出中文了"没有那个文件或目录"
    str = "没有那个文件或目录"
    str.encode("utf-8") # 报错UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)

"""
### f格式化字符串
    - f 格式化字符串中不能又反斜杠，只能用单引号
    - df[col].map(lambda x: f'{x:0>6}') 如果 x 少于 6 位，这意味着对于 x 的任何值右对齐前填充零:
    - f"{num:xxx}"
    其中xxx的格式如下
        格式	说明
        width	整数width指定宽度
        0width	整数width指定宽度，0表示最高位用0补足宽度
        width.precision	整数width指定宽度，整数precision表示精度（保留小数点后几位小数）
    - 使用<>^可以靠左， 靠右，居中显示，另外可以配合填充
    - f{a:.3f} 带f表示保留3位小数
### % 格式化
- link: https://www.cnblogs.com/nutix/p/4504899.html
- %d格式化符: 将任何Python对象转化为整数，如果转化失败，则报错。
    - %nd：决定对齐与填充。n为整数；当n>0时，左填充，当n<0时，右填充。
    - %0nd：以数字0而不是默认的空格来作填充。
- %s 格式化符：将要格式化的值表中对应位置的元素，格式化为字符串，如果值元素不是字符串，将自动调用该元素的__str__()，以得到其字符串表示。
    - %ns决定对齐与填充：n为整数；当n>0时，左填充，当n<0时，右填充。
    - %.ns决定对字符串的截取：n为正整数 (保留最左边的)
- 如何输出大括号呢
f-string大括号外如果需要显示大括号，则应输入连续两个大括号 {{ 和 }}：

"""
name = 'Tom'
print(f'my name is {{{name}}}') # my name is {Tom}

"""
# str.find() # find # index
- find和index的区别在于前者找不到返回-1，后者抛出异常

"""
"""
TO: 字符串占用空间
存储量取决于采用的编码格式，例如ASCII、UTF-8、UTF-16等。在计算机中，1KB等于1024字节（Bytes）。因此，0.5KB等于512字节。以下是基于不同类型的字符和一般编码格式的简单估计：
ASCII编码（英文字符和数字）
ASCII编码一个字符（包括英文字母和数字）通常占用1个字节（8位）。
因此，0.5KB（或512字节）大约可以存储512个ASCII字符。
UTF-8编码
对于UTF-8编码，英文字符和数字仍旧占用1个字节，但中文字符和某些特殊符号会占用更多字节。中文字符通常占用3字节。
因此，如果全是英文字符或数字，可以存储512个。
如果全是中文字符，则大约可以存储170个左右（512除以3）。
UTF-16编码
UTF-16编码中，许多常用字符（包括大多数英文字符和数字）占用2个字节。对于某些不常用的字符，UTF-16可能会使用更多字节，但大部分字符都是2个字节。
中文字符在UTF-16中也是占用2个字节。
因此，不论是英文字符、数字还是中文字符，0.5KB（或512字节）大约可以存储256个。
"""
