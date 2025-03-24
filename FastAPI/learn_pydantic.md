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
### 从模型中生成pydantic模型类, 并使用这个pydantic类序列化数据
```py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

F5VIPPoolInfoPydantic = sqlalchemy_to_pydantic(F5VIPPoolInfo)
self.db.query(F5VIPPoolInfo).filter(F5VIPPoolInfo.virtual_ip == virtual_ip).first()
F5VIPPoolInfoPydantic.from_orm(pool).dict()  # 不加dict是json
```
