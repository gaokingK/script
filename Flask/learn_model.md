### 定义表
```py
Base = declarative_base()

engine = create_engine(app_config.SQLALCHEMY_DATABASE_URI, **app_config.SQLALCHEMY_ENGINE_OPTIONS)


class BaseModel(Base):
    __abstract__ = True
    id = mapped_column(BIGINT, primary_key=True, autoincrement=True, comment='id')

    created_at = mapped_column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')
    updated_at = mapped_column(TIMESTAMP, nullable=False,
                               server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')
    is_deleted = mapped_column(TINYINT, nullable=False, server_default=text("'0'"), comment='是否删除')

    def to_dict(self, tran_date=True):
        res = {column.name: getattr(self, column.name) for column in self.__table__.columns if
               hasattr(self, column.name)}
        if tran_date:
            if res.get("updated_at"):
                res["updated_at"] = res["updated_at"].strftime("%Y-%m-%d %H:%M:%S")
            if res.get("created_at"):
                res["created_at"] = res["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            if res.get("resource_created_at"):
                res["resource_created_at"] = res["resource_created_at"].strftime("%Y-%m-%d %H:%M:%S")
            if res.get("resource_updated_at"):
                res["resource_updated_at"] = res["resource_updated_at"].strftime("%Y-%m-%d %H:%M:%S")
        if res.get("service_date"):
            res["service_date"] = res["service_date"].strftime("%Y-%m-%d")
        if res.get("start_u") and res.get("start_u") == -1:
            res["start_u"] = ""
        return res
class IPResourcesType(BaseModel):
    __tablename__ = 'ip_resoure_type'
    __table_args__ = (
        UniqueConstraint('ip_addr', 'resource_type', name='idx_ip_type'),
    )

    id = mapped_column(Integer, primary_key=True, autoincrement=True, comment='id')
```
