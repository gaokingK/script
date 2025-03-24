# link
- https://www.cnblogs.com/jia-shu/p/14850982.html
- https://blog.csdn.net/haeasringnar/article/details/109339949
  
## 一些装饰器
- https://marshmallow.readthedocs.io/en/stable/marshmallow.decorators.html#marshmallow.decorators.post_load
```py
# 当反序列化多个对象时，pass_many=True 会让钩子函数接收到一个列表。
@pre_load(pass_many=True)
def preprocess_data(self, data, many, **kwargs):
    # 处理多个对象
    if many:
        return [{'name': item['name'].strip(), 'age': item['age']} for item in data]
    return data

@pre_load
def preprocess_data(self, data, **kwargs):
    # 在加载数据之前对数据进行处理
    if 'name' in data:
        data['name'] = data['name'].strip()  # 去除名字两端的空格
    return data

class SomeSchem(Schema)
    ob_ip = fields.String(required=True, validate=check_ob_ip)
    ob_vip = fields.String(required=True, validate=validate_ip)

    @pre_load
    def add_env(self, data, **kwargs):
        data["tags"] = list(filter(lambda d: d.get("value"), data["tags"]))
        data["ob_ip"] = data["ob_ip"].replace(" ", "")
        data["k8s_ip"] = data["k8s_ip"].replace(" ", "")
        self.context = data
        return data
```
### 当校验函数需要传递参数时
```py
# 1 从外部导入的函数可以使用偏函数或者lambda
from functools import partial

def check_ob_ip(ip, parm1):
    pass

ob_ip = fields.String(required=True, validate=partial(check_ob_ip, param1="value1")

ob_ip = fields.String(required=True, validate=lambda x: check_ob_ip(x, param1="value1")

# 可以再class里定义
class SomeSchem(Schema)
    ob_ip = fields.String(required=True)
    def check_ob_ip(self, ip, parm1="value1"):
        pass
```

### 限定字段可选值
```py
class MySchema(Schema):
    # 限定字段只能是 "small", "medium", "large" 中的一种
    size = fields.String(
        required=True,
        validate=validate.OneOf(["small", "medium", "large"], error="Invalid size.")
    )
```

## dump 和 load
```py
### 定义校验类和实例化
class ServerClusterPatchTicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ServerClusterCreateTicketData
    user_name = fields.String(required=True)
server_cluster_patch_ticket_schema = ServerClusterPatchTicketSchema()
# 获取数据 也是字典格式
payload = request.get_json()
data = server_cluster_patch_ticket_schema.load(payload)
# 如果有字段定义required=true 但是payload里没有该字段会报错，如果payload有校验类中没有定义的字段也会报错

序列化
data = {"xxx": "xxx", ...}
new_data = server_cluster_patch_ticket_schema.dump(data)
# 只会留下校验类中和data中都有的字段，如果data中有其他名字字段或者校验类中定义的字段在data中没有，都不会报错
# 字段名相同，但类型却不一样，如果能转成校验类中定义的类型，不会报错，如果不能转成，会报类型转化错误

payload["ticket_id"]="xxxx"
server_cluster_patch_ticket_schema.dump(payload)
Traceback (most recent call last):
...
ValueError: invalid literal for int() with base 10: 'xxxx'
```
## 从模型中生成校验类
```py
class PuppetSslDeleteTicketCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StoreServerTicketData
        # exclude 不希望出现在请求体中的内容，这些列要在模型中定义
        # 如果请求体中出现dn，会报错；其余的列如果没有在请求体中出现，也会报错
        exclude = ('id', 'created_at', 'updated_at', 'is_deleted', 'ticket_id', "dn")
    process_name = fields.String(required=True) 
    user_name = fields.String(required=True)
    # 表中的列-exclude+这里声明的就是允许出现的，如果出现其他的就会报错
class ClusterCreateTicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        # 如果是从模型为基础生成的校验类，那么在meta中就完成了对模型字段的修改， 外面的字段应该和表没关系
        # 但是这些字段required默认是False的
        model = ServerClusterCreateTicketData
        exclude = ("id", "ticket_id")
        only = ("cluster_name", "env", "gateway", "ip")
    user_name = fields.String(required=True)
    process_name = fields.String(required=True)
```


### 嵌套schema
```py
data = fields.List(fields.Nested(
    ModifyServerInfoTicketCreateSchema(
        exclude=["dn", "process_name", "user_name"]
    )))
```
### 在Netsd中定义schema
```py
class ServerGroupChangeTicketStartSchema(Schema):
    """进入流程前校验请求参数"""
    # data = fields.List(fields.Nested(ChangeServerGroupTicketDataSchema(
    #     only=["store_id"])), validate=validate.Length(min=1), required=True)
    # data = fields.List(fields.Dict(), validate=validate.Length(min=1), required=True)
    data = fields.List(fields.Nested(
        nested={"store_id": fields.String(required=True)}), validate=validate.Length(min=1), required=True)
```
### 想添加对某个字段的校验，并且如果有其他字段也不报错
```py
    data = fields.List(fields.Dict(
        keys=fields.String(), values=fields.String()), validate=validate.Length(min=1), required=True)

    @validates('data')
    def check_server_state(self, data):
        for item in data:
            if "store_id" not in item:
                raise ValidationError(message={"store_id": "sss"})
```
### 单独使用scheam类某个字段来校验

### only、exclude、default_load default_dump dump_only(bool) load_only(bool)
- 在Marshmallow中，exclude参数不会直接受到模型定义中字段是否必须（nullable=False）或者是否有默认值的影响。exclude参数的作用是在序列化和反序列化过程中明确排除某些字段，无论这些字段在模型中是否是必须的或者是否有默认值。
- 使用only时 会受影响，即使字段没有出现在only中，但如果模型中该字段是不能为空的，并且没有默认值的，如果带校验对象中未出现该字段，仍会报错，可以通过load(partial=True) 但这样only中定义的字段确实了也不会报错

## self.context 通常用于访问当前上下文的数据，但它默认并不会自动包含所有字段的值。要确保能够在验证过程中访问其他字段的值你可以在 load() 方法调用时显式地传递上下文。或者写在pre_load里（见上面）
```py
validated_data = schema.load(data, context=data)
class RangeSchema(Schema):
    min_value = fields.Int(required=True)
    max_value = fields.Int(required=True)

    @validates('max_value')
    def validate_max_value(self, max_value):
        # 从上下文中获取 min_value
        min_value = self.context.get('min_value')
        if min_value is not None and max_value < min_value:
            raise ValidationError("max_value must be greater than or equal to min_value.")


```
## 校验两个参数的大小关系
```py
from marshmallow import Schema, fields, validate, ValidationError

def validate_start_end(start, end):
    if start >= end:
        raise ValidationError("开始日期必须早于结束日期。")

class MySchema(Schema):
    start_date = fields.Date(required=True, validate=[validate_start_end])
    end_date = fields.Date(required=True, validate=[validate_start_end])
```
## from_dict() 可以快速创建一个匿名的 Schema，通过字典定义字段。
```py
    # 定义列表，每个元素包含 StoreServerTicketDataSchema 的字段和额外字段
    data = fields.List(fields.Nested(
        Schema.from_dict({
            "store_id": fields.Int(required=True),  # 来自 StoreServerTicketDataSchema
            "store_fullname": fields.Str(),         # 来自 StoreServerTicketDataSchema
            "hostname": fields.Str(),               # 来自 StoreServerTicketDataSchema
            "status": fields.Str(required=True)     # 额外的字段
        })
    ))
    
```

