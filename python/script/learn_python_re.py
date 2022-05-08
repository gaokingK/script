#!/usr/bin/python3
"""
# 写正则表达式困难的不是匹配到想要的内容，而是尽可能的不匹配到不想要的内容
# 书籍：正则表达式必知必会
- [挺好的](https://deerchao.cn/tutorials/regex/regex.htm)
string = "113/kbox_result_202110180959.txt"
ls 113/*.txt|sed "s/*kbox_r.*t_//g" 为什么kbox前的那个星号没有用，因为sed也能用正则，但是*号代表前个模式匹配0次或者多次， 
但为什没有用呢？难道前面不是null吗
# 问题
    - 如何用re完成if "_get" or "_add" or "_update" in "xxxxx":

[a-z0-9]([-a-z0-9]*[a-z0-9])? == [a-z0-9][-a-z0-9]*
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
“””
if __name__ == "__main__":
    choice_num()

