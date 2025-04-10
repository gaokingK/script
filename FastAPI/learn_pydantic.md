### 定义模型
- link: https://pydantic.com.cn/concepts/models/#_12
  
```py
class VMCountDataSchema(BaseModel):
    total: int = Field(default=0)
    running: int = Field(default=None)  # 默认值是None
    shutdown: int = Field(default=0)  # 默认值是0

class VMCountResponseSchema(BaseModel):
    idc: VMCountDataSchema
    cloud: VMCountDataSchema
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
### 从模型中生成pydantic模型类, 并使用这个pydantic类序列化数据
```py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

F5VIPPoolInfoPydantic = sqlalchemy_to_pydantic(F5VIPPoolInfo)
self.db.query(F5VIPPoolInfo).filter(F5VIPPoolInfo.virtual_ip == virtual_ip).first()
F5VIPPoolInfoPydantic.from_orm(pool).dict()  # 不加dict是json
```
