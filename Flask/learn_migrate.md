# 数据库版本管理
- 都是管理数据库结构的更改的，而不是数据
[使用alembic管理数据库版本](http://blog.lllyyb.com/p/3e35.html)
[python sqlalchemy-migrate 使用方法](https://www.cnblogs.com/jsben/p/5058606.html)

- django 中makemigrations 和migrate
- python manger.py makemigrations  在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动， 执行python manager.py migrate来将该改动作用到数据库文件，比如产生table之类
