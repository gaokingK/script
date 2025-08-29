### 中间件的执行顺序
```py
app.add_middleware(MCDUserProfileMiddleware)  # 第一个注册
app.add_middleware(AccessLogMiddleware)       # 第二个注册

请求进入：AccessLogMiddleware → MCDUserProfileMiddleware → 路由处理
响应返回：MCDUserProfileMiddleware → AccessLogMiddleware → 客户端
```
### 异常处理
- 异常流程：
任何阶段出现异常都会被对应的异常处理器捕获，然后直接返回响应，跳过后续处理但仍会执行中间件的响应部分。
- 中间件包装 → 路由/验证 → 异常处理（如需要） → 中间件响应
