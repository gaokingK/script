### 其实这样market为空的也会有匹配，只是自己会默认为匹配不上
```py
# 如果门店没有市场属性会分配market不为空的集群
db.session().query(StoreCluster)
            .filter(StoreCluster.is_deleted == 0)
            .filter(StoreCluster.env == 'prod')
            .filter(func.JSON_UNQUOTE(func.JSON_EXTRACT(StoreCluster.tags, "$.Market"))
                    .like(f"%{market}%"))

select * from store_cluster where is_deleted=0 and JSON_UNQUOTE(json_extract(tags, "$.Market")) like "%%";                                    
```
### getattr要写默认值
```py
getattr(request, "environ", "")  # 没有属性返回 ""
getattr(request, "environ")  # 没有属性报错

```
### 加逗号回变成元组
```
owner = getattr(item, "admin", ""), # 这样owner就会变成一个元组("获得的admin的值", ")
```
### 一些奇怪的写法
```py
class AliRds:
    @staticmethod  # 想这样中间空一行也是可以的

    def create_client() -> Rds20140815Client:

## 这样不会循环引用
res = [1, 2]
res = {
    "total": len(res),
    "disk": res
}


```
### 避免这种问题
```py
all_id = (vm_obj.data_disk + "," + vm_obj.system_disk).split(",")
all_id = [i for i in all_id if i] # 如果不过滤，为空就是查询所有
for id in all_id:
    disk_infos, total = cmp_api.get_disks_info_by_eid(id)
```
### 这个查询请求，如果将请求方法改为get，会有什么问题呢
```py
"""
GET请求不能将参数放在请求体(JSON)中:

1. HTTP/1.1规范中，GET请求不应该包含请求体。虽然技术上可以发送带body的GET请求，但这违反了HTTP设计原则
2. 许多服务器、代理、客户端会忽略GET请求中的请求体
3. GET请求的参数应该通过URL查询字符串(query string)传递
4. 对于需要传递复杂JSON数据的API，应该使用POST方法

因此对于当前这个成本估算接口:
1. 由于参数复杂(CostQuery包含多层嵌套的对象)
2. 参数可能较大,超出URL长度限制
3. 数据不适合放在URL中暴露

建议继续使用POST方法,通过请求体传递JSON数据。
@router.get("/estimation")
def cost_estimation(cost: CostQuery = Depends(), db: Session = Depends(get_db)):
    """
    注意: 不建议将此接口改为GET方法，原因如下:
    1. GET请求的参数会暴露在URL中，而cost参数包含较多嵌套的复杂数据结构，URL长度有限制
    2. GET请求参数通常用于简单的查询参数，而不是复杂的JSON对象
    3. GET请求的参数会被浏览器缓存，可能导致数据不一致
    4. 从语义上讲，成本估算更接近于一个计算/处理操作，而不是简单的数据获取
    建议保持使用POST方法
    """
```
### 重载为什么不生效
```py
Class AliRds:

    @staticmethod  # 静态方法装饰器会将方法转换为一个静态函数对象,不会隐式传入self或cls参数,使其可以直接通过类名调用而无需实例化。它实际上是通过staticmethod类来实现的,该类会返回一个去除了方法对类的绑定的函数对象。
    def map_mariadb_params():
        pass
    @staticmothed
    def map_mariadb_params(payload={}, is_get = False):
        pass
    @staticmothed
    def get_params():
        pass 
        res = AliRds.map_mariadb_params(payload, is_get) # 能调通
        # 但是如果将未定义的方法写在定义的方法下面就会调不通
        # 跟加不加staticmethod没任何关系


```
### 为什么不加classmethod装饰器就访问不到cls.__name --------------no
### pycharm 自动完成
[link](https://blog.csdn.net/migming/article/details/109978585)
### print(1/0)会出错
### 字节字符串、Unicode字符串、打开的二进制文件对象或者打开的文本文件对象都是什么？、BOM（byte order mark)
### 为什么如下所示的yaml文件经过反序列化后再序列化得到的文件格式和原来的不一样？
[link](https://blog.csdn.net/swinfans/article/details/88770119)
```python
document = """
    a: 1
    b:
      c: 3
      d: 4
    """
print(yaml.dump(yaml.load(document)))
a: 1
b: {c: 3, d: 4}
```
因为PyYaml会根据一个集合内是否含有嵌套的集合来决定使用哪种格式来表示这个集合，如果一个集合中含有嵌套的集合
那么PyYaml会使用块样式来表示，否则就会使用流样式来表示（上面的就是流样式）可以通过`dump`的参数`default_flow_style=False`
来使用块样式


### format中的**位置参数**是一个元组，在前面引用的部分是元组的索引
```python
a = "{server}:{0}{1}".format("127.0.0.1", "8080", server="www.xxxx.cn")
```
[format 的填充对齐](https://www.cnblogs.com/lvcm/p/8859225.html)

### Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
[doc](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)
`html.parser` 是python内置的解析器

### 协程看上去也是子程序，但执行过程中，在子程序内部可中断， ，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断
