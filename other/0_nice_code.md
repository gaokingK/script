# 好的代码
# [文件名][方法名] point 默认是python当中的

### 关键的日志最好有标识
```python
    print(script_log_path) 
    print(f"get path is: [{script_log_path}])
    # 否则日志中的这种情况就会puzzle
huawei@huawei-PC:~/Desktop/autotest$ python3 find_author.py kbox_result_202110201517.txt 
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_004_test-20211020152149
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_005_test-20211020152423
/home/huawei/Desktop/autotest/log/20211020/aiqiyi_open_006_test-20211020152602
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_004_test-20211020155833
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_005_test-20211020160110
/home/huawei/Desktop/autotest/log/20211020/bilibili_open_006_test-20211020160409
/home/huawei/Desktop/autotest/log/20211020/dingding_open_004_test-20211020164144
/home/huawei/Desktop/autotest/log/20211020/dingding_open_005_test-20211020164422
/home/huawei/Desktop/autotest/log/20211020/dingding_open_006_test-20211020164643
/home/huawei/Desktop/autotest/log/20211020/douban_open_004_test-20211020170055
/home/huawei/Desktop/autotest/log/20211020/douban_open_005_test-20211020170226
/home/huawei/Desktop/autotest/log/20211020/douban_open_006_test-20211020170405
/home/huawei/Desktop/autotest/log/20211020/douyin_open_004_test-20211020171500
/home/huawei/Desktop/autotest/log/20211020/douyin_open_005_test-20211020171933
/home/huawei/Desktop/autotest/log/20211020/douyin_open_006_test-20211020172401
# 上面的几行就会迷惑, 而实际是log_path是空
huawei@huawei-PC:~/Desktop/autotest$ 
# 调试这个错误时, 应该直接把命令打出来
```
### 我没改完，我没验证完
### 清空日志 `cat /dev/null > /var/log/RemoteSyslog/syslog.log`
### learn_structure_tree find_child_tree
   -  while 后不要跟不会变的变量,会死循环
### 方法注释中参数的类型应该怎么写

### 使用这种方法来解决拼接路径导入os `self.download_path = self.bmcweb.download_dir + "\\video_osreset.rep"`
# 巧合问题
- "Identifier name '<bound method ? of <class 'common.model.test2_model.Child'>>_ibfk_1' is too long") 使用声明系统创建一个表时表名太长。 
```
# 出错代码
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename_ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    # parent = relationship("Parent", back_populates="children")

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     children = relationship("Child")
#
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))

# 分析流程，和其他的对比没有对比出来出错原因，后来采用重写方案，把源代码给复制过来，发现能好，又对比了一波，还没对比出来，后来用”compare with clipbord“ 也费了好久才发现是__tablename__写成了__tablename_
# 影响：1. 发现不了就重写，这样能把不易发现的错误给避免。2. 没错的东西应该相信没错，不要再对比了3. 类似对比__tablename__的过程中，对比了好几次，不应该忽略tablename此外的东西,包括__这些符号
```