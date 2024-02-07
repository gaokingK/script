### link
- https://www.runoob.com/regexp/regexp-syntax.html
- https://www.runoob.com/regexp/regexp-metachar.html
- https://www.cnblogs.com/ljhdo/p/10678281.html
### 匹配字符
- \s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符。
- \b 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。\B匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
- 如果使用多个字符连在一起的或（比如匹配abr或dcr，应该用括号括起来）
- [ab|dc]r 方括号本来就是或，里面的|就没有用了
- (ab|dc)r 匹配abr 或者cr 是以|分割所有的
### re.sub(r"(?<=\()(\S+)(?=\))", r"\1 IB", event_description) 
- 还可已这样替换
```
a="disk backplane 2 temperature detection point"
re.sub(r"(?<=backplane )\d(?= temper)", "-", a, 1)
或者直接 re.sub(r"(?<=backplane )\d(?= temper)", "backplane - temper", a, 1)
```
### (?<=(mAsserted\(.*\n.*\n.*)) wait_time=20\)
### exp1(?=exp2)：查找 exp2 前面的 exp1。

### 匹配x或者h [x,h] 不能[x-h]

### .不能出现在[]中
```cs
re.findall(r'a[.]*b', "acccb")
[]
# 要用\S代替
re.findall(r'a([\S]*)b', "acccb")
['ccc']
```
### {n,m} 匹配n-m次