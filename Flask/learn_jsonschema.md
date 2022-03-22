# 参数校验
## link:
    - https://www.cnblogs.com/terencezhou/p/10474617.html

## 使用
- "enum": ["red", "amber", "green"] 限定可选值
- 关于命名
```
@docker.route("/docker_create", methods=['POST'])
@validate_schema(docker_schema.docker_create_schema)
def create_docker():
```
- 可以通过POST、GET为接口定义通用的验证规则
```
class TaskScheme(object):
    POST = {
        "title": "post_parameter",
        "description": "添加入参校验",
        "type": "object",
        "properties": {
            "case_name": {
                "description": "用例名称",
                "type": "string",
                "maxLength": 32,
            },
            "executor": {
                "description": "执行人",
                "type": "string",
                "maxLength": 32,
            },
            },
        "additionalProperties": True,
        "required": ["case_name", "executor"]
        }
    GET = {
        略
    }
@task.route("/task_get", methods=["GET", "POST"])
@validate_schema(TaskScheme)
def get_task():
    pass
```