### script需要重新命名 可以改成learn_vir?
```
|-change_pc_90.90.0.140.md
├─python
|   ├─script 脚本
|   └─doc 文档
|     
├─Todo 起了个头， 还待补充
|  └─ project_problem 项目中遇到和解决的问题
├─flask flask及其他组件
|   
├─C_C++ C/C++学习
| 
└other 其他语言
|  └─doc 把一些常用的文档命名为0_xxxx
|  └─ 0_nice_code 一些编码规范, 和坑,巧合
|   
├─MySQL
|  └─ other 一些零碎的
| 
```
#### 格式
- 加`-------------no(大)` 或者`?(小)`来标识有疑问的地方 
- 问题还是放在文件头好, 有必要的话就加上章节给区分下
- 如果不想记录，就只把用到的记下来；把链接贴上
- 优化小标题
    - 小标题统一"###"开头，也允许(### 1.)但不允许(1. ###)
      - 但部分应以## 开头， 总而言之，不应没有#标题
    - 标题下的章节可以缩进，也可不缩进
    - 缩进的格式要统一，以后统一4个space
    - 缩进不一样也没关系，文件中保持一致就好
- 像SQLAlchemy这样，刚开始把东西写到一块，后面详细学习的时候， 不必把里面的东西删掉，而是复制到相关的文档中
- 有时可能会在学某个体系的地方认识到了一些别的东西，就把这些东西放到other里,如MySQL/other.md
- 每个概念性的东西中考虑是否建一个标题 如MySQL/learn_index.md/# ## 索引的一些名词 ##索引的一些语法