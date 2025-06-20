### 定义模型
- link: https://pydantic.com.cn/concepts/models/#_12
```py
from datetime import datetime

class VMCountDataSchema(BaseModel):
    model_config = {"extra": "forbid"} # 假设有一个客户端尝试在查询参数中发送一些额外的数据，它将会收到一个错误响应。
    total: int = Field(default=0)
    running: int = Field(default=None)  # 默认值是None 必填 ，如果没有默认值就会报错
    shutdown: int = Field(default=0)  # 默认值是0
    updated_at: Optional[str] = Field(None, description="更新时间") # 选填 也要加默认值
    instance_type: Dict[str, Union[str, int]] = Field(description="询价资源ID对象")
    instance_type: Dict[str, Union[str, int, List[Union[str, int]]]] = Field(description="询价资源ID对象")
    # 这样已经能校验某些类型的输入了 比如输入的是str类型的18,会返回1970-1-1 00:00:18，输入x就会报错 输入18：18也会报错，校验不全面 而且返回的类型是datetime类型的，所以还是自己写一个str类型字段定义，再写一个验证方法把
    updated_at_r: Optional[datetime] = Field(None, description="更新时间", format="%Y-%m-%d %H:%M:%S")


    @field_validator('l_time', 'r_time', mode='before')
    @classmethod # field_validator 必须装饰类方法
    def parse_datetime(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError("时间格式应为 YYYY-MM-DD HH:MM:SS")
        return value


class VMCountResponseSchema(BaseModel):
    idc: VMCountDataSchema
    cloud: VMCountDataSchema


@app.get("/records")
def get_records(params: RecordQuerySchema = Depends()):
    pass
    # GET 请求不能用 request body，所以你必须用 Depends() 来自动把 query 参数映射到模型。
```
### get请求的模型
```py
# http://0.0.0.0:9000/virtual_machine/export?vm_name=ab 如果要传多个vm_name就继续写
# http://0.0.0.0:9000/virtual_machine/export?vm_name=ab&vm_name=c 如果要传多个vm_name就继续写

class VirtualMachineQuerySchema(BaseModel):
    page: int
    page_size: int
    vm_name: Optional[Union[str, List[str]]]

# 方式一：使用 Annotated + Query()
def list_vm_device(query: Annotated[VirtualMachineQuerySchema, Query()]):
# FastAPI 直接将查询参数映射为模型字段 明确是从 query 参数中提取字段组成模型

# 方式二：使用 Depends
def list_vm_device(query: VirtualMachineQuerySchema = Depends()):
# FastAPI 把 Model 当作一个“依赖项”，调用其构造函数 适用于从 query/header/path/form/body 等多种来源组合依赖

```
### 模型序列化
```py
class GeneralQueryParamSchema(BaseModel):
    page: int = Field(default=1)
    page_size: int = Field(default=50)

class PriceQueryParamSchema(GeneralQueryParamSchema):
    resource_type: Optional[str] = Field(None, description="资源类型")
    host_env: Optional[str] = Field(None, description="宿主环境")
    created_at: Optional[str] = Field(None, description="创建时间")
    updated_at: Optional[str] = Field(None, description="更新时间")

@router.post("", response_model=PriceQueryResSchema, summary="查询定价策略")
def get_all_resource_price(payload: PriceQueryParamSchema, db: Session=Depends(get_db)):
    pass

# 请求体
{}

payload.model_dump()
{'page': 1, 'page_size': 50, 'resource_type': None, 'host_env': None, 'created_at': None, 'updated_at': None}
payload.model_dump(exclude_defaults=True) # 排除和默认值相同的
{}
payload.model_dump(exclude_unset=True)
{}
payload.model_dump(exclude_none=True)
{'page': 1, 'page_size': 50}
# 请求体
{
    "page": 1
}
payload.model_dump(exclude_none=True)
{'page': 1, 'page_size': 50}
payload.model_dump(exclude_unset=True)
{'page': 1}
payload.model_dump(exclude_defaults=True)
{}
```
### 
### 从模型中生成pydantic模型类, 并使用这个pydantic类序列化数据
```py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

F5VIPPoolInfoPydantic = sqlalchemy_to_pydantic(F5VIPPoolInfo)
self.db.query(F5VIPPoolInfo).filter(F5VIPPoolInfo.virtual_ip == virtual_ip).first()
F5VIPPoolInfoPydantic.from_orm(pool).dict()  # 不加dict是json
```
### 校验
```py
def validate_rds_resource_type(vlaue: str) -> str:
    valid_v = ["mysql", "msqls", "pgsql", "mariadb"]
    if vlaue not in valid_v:
        raise ValueError(f"rds资源类型只能是{valid_v}的一种")
    return vlaue

class RdsParamsGetSchema(BaseModel):
    # 如果有多个validator函数,会按照列表顺序依次执行
    # 前一个validator的输出会作为后一个validator的输入
    # 如果任一validator校验失败会抛出ValidationError
    engine: str = Field(description="询价资源类型", validators=[validate_rds_resource_type])
    # 是的，你提供的写法在 Pydantic V2 中是 不正确的。
    # Pydantic V2 不再支持 Field(..., validators=[...]) 的用法。字段级验证应使用 @field_validator 装饰器。
    @field_validator("engine", mode="before") # mode = before/after before时会先用下面的函数转换参数的值，然后再传到模型里做校验，如果类型不一致会抛出异常
    @classmethod
    def validate_engine(cls, v):
        return validate_rds_resource_type(v)  
```
