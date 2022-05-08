### 包含除python， linux之外的
### SQL
1. 如果要给 SQL 语句传递参数，请在语句中使用问号来代替参数，并把参数放在一个列表中 一起传递。不要用字符串格式化的方式直接把参数加入 SQL 语句中，这样会给应用带来 SQL 注入 的风险。
    `user = query_db('select * from users where username = ?', [the_username], one=True)`

### SmallTalk
被认为最具代表性和运用最广泛的面向对象程序设计语言。
四十年前，他的动态更新和反射就领先
