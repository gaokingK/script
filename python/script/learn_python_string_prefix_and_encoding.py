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
# Python在内存中处理的字符串一般都是经过unicode编码的了的字符串

# Python在物理存储、网络传输时，为节省空间（包括物理空间和时间空间），
# 需将字符串转换成字节序列对象bytearray，按字节Bytes发送。
