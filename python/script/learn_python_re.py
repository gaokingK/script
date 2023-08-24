#!/usr/bin/python3
"""
# 写正则表达式困难的不是匹配到想要的内容，而是尽可能的不匹配到不想要的内容
# 书籍：正则表达式必知必会
- [挺好的](https://deerchao.cn/tutorials/regex/regex.htm)
- [在线正则表达式，以及有一些正则表达式语法的介绍](https://c.runoob.com/front-end/854/)

# 概述
- re.sub() 可以接受一个函数，此函数可以把匹配到的内容作为参数

# 问题
    - 如何用re完成if "_get" or "_add" or "_update" in "xxxxx":

    - string = "113/kbox_result_202110180959.txt" 命令是：ls 113/*.txt|sed "s/*kbox_r.*t_//g" 为什么kbox前的那个星号没有用，
        - 因为sed也能用正则，但是*号代表前个模式匹配0次或者多次。
        - 但为什没有用呢？难道前面不是null吗

    - [a-z0-9]([-a-z0-9]*[a-z0-9])? == [a-z0-9][-a-z0-9]*

    - nothing to repeat 贪婪匹配的问题

    - 正则表达式如何传入参数
        - 不可以使用f
        - re.findall(r"(^# \b%sth\b.*$)(.*)"%(2), a, re.M)
        - re.findall(r"(^# \b{}th\b.*$)(.*)".format(2), a, re.M)
    - 如何匹配数字范围
        - https://geek-docs.com/regexp/regexp-tutorials/regular-expressions-match-numeric-ranges.html
        - 表达式[0-255]并不能匹配0至255之间的数字。表达式[0-255]是一个字符集，它的含义是匹配 0，1，2，5中任意一个字符，这个表达式等同于[0125]
    - 如何使用|
        - 使得"m|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m|f)ood"。
        - 但这样会有一个问题：re.findall(r"(18:([0-2][0-9]|30))", "18:30:55") 会有两个分组
    - 你能看出来这里有什么问题吗？
        - re.match(r"[0-1][0-9]|2[0-3].*", "23:52:16").group()
        - re.match(r"[0-1][0-9]|2[0-3].*", "18:52:16").group()
"""
import re


def choice_num(num="[40,256][88,888]"):
    # 把数字挑出来并放到列表中
    pattern1 = re.compile(r'(\d+)\D*')
    res = pattern1.findall(num)
    print(res)
    res = re.findall(r'(\d+)\D*', num)
    print(res)
    res = re.finditer(r'(\d+)', num)
    print([x.group() for x in res])

"""
re.match() 从字符串起始位置开始匹配
re.search() 返回第一个匹配的对象
re.findall() 返回一个列表, 里面是匹配到的内容, 如果里面有分组的话,只显示分组的
    - ((patternA)(patternB))(patternC) 在结果中是('patternApatternB', patternA, patterB, patternC)
re.finditer() 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
    for item in re.finditer():
        item.group()# 当前patter_str匹配到的子串, 不按分组分开
        item.groups() # 结果是里面分组匹配到的
        item.start() # 匹配结果的起始位置索引


re.S 使 . 匹配包括换行在内的所有字符, 但这样会引起问题可能.*就一直匹配到文件尾了
    可以在.*后面加?使匹配模式由贪婪变成不贪婪
    re.findall(r"patternA.*?(\d+)", content, re.S) 中的.*如果不加?会让后面的\d+匹配到文件的最后一个字符
匹配.字符 时使用 \.
是\d 不是%d
"""

"""
To: 贪婪非贪婪
link: https://blog.csdn.net/real_ray/article/details/17502587
Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪）在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
"""
"""
To: nothing to repeat 贪婪匹配的问题
$ 默认也是贪婪匹配的，加了？就会报错
"""
def test_greedy():
    test_str = """
    # 1th batch case 26
    Component_DISK_Model_0010
    Component_FAN_092


    # 2th batch case 26
    """
    # re.findall(r"(^# \b1th\b.*$?)(.*)", a, re.MULTILINE) # 会提示nothing to repeat
    # re.findall(r"(^# \b1th\b.*$)(.*)", a, re.MULTILINE) # [('# 1th batch case 26\nComponent_DISK_Model_0010\nComponent_FAN_092\n\n\n# 2th batch case 26', '')]
    re.findall(r"(# \b{}th\b.*?\n)(.*)".format(1), a, re.S) # 这样就好了 [('# 1th batch case 26\n', 'Component_DISK_Model_0010\nComponent_FAN_092\n\n\n# 2th batch case 26')]
    
"""
To: 回溯引用、向前向后查找
link：https://www.cnblogs.com/chuxiuhong/p/5907484.html

回溯引用（看下向后引用吧）
比如你要匹配h1-h6每个标题的内容， 你可能会这么写`p = r"<h[1-6]>.*?</h[1-6]>"`, 但是你也会匹配<h1>xxx<\h6>这种非预期的。
回溯引用的写法：p1 = r"<h([1-6])>.*?</h\1>" 
使用转义字符把1转成第一个子表达式， 前面匹配到1, 后面也匹配到1；（不一定，看向后引用）\2,\3,....就代表第二个第三个子表达式 \0代表整个表达式。

向前向后查找
简单来说，就是你要匹配的字符是XX，但必须满足形式是AXXB这样的字符串，那么你就可以这样写正则表达式
p = r"(?<=A)XX(?=B)"
匹配到的字符串就是XX。并且，向前查找向后查找不需要必须同时出现。如果你愿意，可以只写满足一个条件。
感觉和 p=r"() "
"""
"""
To: 向后引用以及零宽断言、小括号的用法
link: https://www.cnblogs.com/linux-wangkun/p/5978462.html
向后引用 

### 负向预查模式 `(?!expr)`
- 前面还有个表达式A，如下面的java，在A后面进行这个模式的匹配
- java(?!6) 就会匹配java7中的java，而不会匹配java6中的java; 是不是可以(?!6)java
- Windows(?!95|98|NT|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"
- 要用括号包括起来；后面的是一个表达式
"""

"""
To: 定位符
- ^ 匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配
- $
- \b 匹配一个单词边界，即字与空格间的位置。
    - /ter\b/ 匹配bster中的ter，而不匹配bstera中的ter
    - /\bv\b/ 能匹配[v]中的v
- \B
"""

"""
To: 修饰符
re.S        使 . 匹配包括换行在内的所有字符
re.M        多行匹配，影响 ^ 和 $
"""


"""
To: 直接将匹配结果直接转为字典模式 命名分组
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())
{'province': '110', 'city': '223', 'born_year': '1990'}
"""
if __name__ == "__main__":
    choice_num()

