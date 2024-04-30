### link
- https://www.runoob.com/regexp/regexp-syntax.html
- https://www.runoob.com/regexp/regexp-metachar.html
- https://www.cnblogs.com/ljhdo/p/10678281.html
- https://juejin.cn/post/7025490351032893476常用的正则验证，包含中国手机号，邮箱，银行卡号，身份证，网址等
### 匹配字符
- \s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符。
- \b 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。\B匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
- 如果使用多个字符连在一起的或（比如匹配abr或dcr，应该用括号括起来）
- [ab|dc]r 方括号本来就是或，里面的|就没有用了
- (ab|dc)r 匹配abr 或者cr 是以|分割所有的 ab|dcr匹配ab、dcr、不能匹配abcr
- 可以用`\.`匹配`.`,但是如果想匹配除`.*`外的所有`*`,就不可以用
```cs
>>> print(re.sub(r"([^\.]\*)", "_", "*1*000.*")) 
*_000.*
### 可以这样
>>> print(re.sub(r"(?<!\.)\*", "_", "*1*000.*")) 
_1_000.*
```
### re.sub(r"(?<=\()(\S+)(?=\))", r"\1 IB", event_description) 
- 还可已这样替换
```
a="disk backplane 2 temperature detection point"!
re.sub(r"(?<=backplane )\d(?= temper)", "-", a, 1)
或者直接 re.sub(r"(?<=backplane )\d(?= temper)", "backplane - temper", a, 1)
```

### (?:pattern)	
- 匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式。
### 预查，正向向后，反向向前
### 正向肯定预查 (?=pattern)
- "Windows(?=95|98|NT|2000)"能匹配"Windows2000"中的"Windows"，但不能匹配"Windows3.1"中的"Windows"。
- 预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始
### 正向否定预查 (?!pattern)
- "Windows(?!95|98|NT|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"
### 反向(look behind)肯定预查 (?<=pattern)
- "(?<=95|98|NT|2000)Windows"能匹配"2000Windows"中的"Windows"，但不能匹配"3.1Windows"中的"Windows"。
### 反向否定预查 (?<!pattern)
- 与正向否定预查类似，只是方向相反。例如"(?<!95|98|NT|2000)Windows"能匹配"3.1Windows"中的"Windows"，但不能匹配"2000Windows"中的"Windows"。

### exp1(?=exp2)：查找 exp2 前面的 exp1。
### (?<=exp2)exp1：查找 exp2 后面的 exp1。
- (?<=(mAsserted\(.*\n.*\n.*)) wait_time=20\)
### 匹配x或者h [x,h] 不能[x-h]

### .不能出现在[]中
```cs
re.findall(r'a[.]*b', "acccb")
[]
# 要用\S代替
re.findall(r'a([\S]*)b', "acccb")
['ccc']
```
### {n,m} 匹配n-m次 {n,}匹配N次或以上

```
[\u4e00-\u9fa5] 匹配中文
\w	匹配字母数字及下划线 不匹配中文
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [ \t\n\r\f]。
\S	匹配任意非空字符 能匹配中文
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
? - 0 次或 1 次匹配。
* - 匹配 0 次或多次。
+ - 匹配 1 次或多次
```