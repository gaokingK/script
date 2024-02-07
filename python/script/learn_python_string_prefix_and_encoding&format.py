"""
前缀和编码
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
To: 编码
"""
def byte2str():
    b = "\xe6\xb2\xa1\xe6\x9c\x89\xe9\x82\xa3\xe4\xb8\xaa\xe6\x96\x87\xe4\xbb\xb6\xe6\x88\x96\xe7\x9b\xae\xe5\xbd\x95" # 在arm上的
    print(b) # 直接就输出中文了"没有那个文件或目录"
    str = "没有那个文件或目录"
    str.encode("utf-8") # 报错UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)

"""
### 格式化字符串
    - f 格式化字符串中不能又反斜杠，只能用单引号
    - df[col].map(lambda x: f'{x:0>6}') 如果 x 少于 6 位，这意味着对于 x 的任何值右对齐前填充零:
### % 格式化
- link: https://www.cnblogs.com/nutix/p/4504899.html
- %d格式化符: 将任何Python对象转化为整数，如果转化失败，则报错。
    - %nd：决定对齐与填充。n为整数；当n>0时，左填充，当n<0时，右填充。
    - %0nd：以数字0而不是默认的空格来作填充。
- %s 格式化符：将要格式化的值表中对应位置的元素，格式化为字符串，如果值元素不是字符串，将自动调用该元素的__str__()，以得到其字符串表示。
    - %ns决定对齐与填充：n为整数；当n>0时，左填充，当n<0时，右填充。
    - %.ns决定对字符串的截取：n为正整数 (保留最左边的)
"""
