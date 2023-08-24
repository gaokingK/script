# 帮助信息
- 文档的阅读说明：https://docs.djangoproject.com/zh-hans/4.2/intro/whatsnext/
- index: https://docs.djangoproject.com/zh-hans/4.2/topics/
# 注意
- 没有返回Response 对象会报错
# 正文
### 运行端口
- 配置：link：https://blog.csdn.net/lkballip/article/details/109205373
- 在命令中`python manage.py runserver xxx`
- Django设置外网、局域网访问 https://blog.csdn.net/dorlolo/article/details/116074074
    - ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.110.1", "*"] 也代表所有能访问
    - 这样设置只能局域网访问，要想从公网访问还得设置内网穿透https://blog.csdn.net/qq_45878803/article/details/121651477 ngrok
### shell 
- 运行djadmin:`shell` 命令`python manage.py shell` 是可交互窗口
# 处理请求
### 保存文件
- link:https://docs.djangoproject.com/zh-hans/4.2/topics/http/file-uploads/
```
def update_conf(self, request):
        handle_uploaded_file(request.FILES["file"])
def handle_uploaded_file(f):
    with open("./new_worker_alert_conf.json", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
```
# module
### field
- models.DateTimeField(default=datetime.fromisoformat("1900-01-01T00:00:00.000"), tzinfo=time_zone) 使用的是datetime.datetime类型
    - 日期转换：https://www.cnblogs.com/presleyren/p/10310859.html
    
# setting.py
### USE_TZ TIME_ZONE 
- https://www.cnblogs.com/zhuminghui/p/9196801.html
- USE_TZ设置为True，Django会自动根据所设的时区对时间进行转换，所以程序中和数据保存的时间都转UTC时间，只有模版渲染时会把时间转为TIME_ZONE所设置的时区的时间。
- datetime.datetime.utcnow()输出的是不带时区的utc时间，称为naive time
- 使用django.utils.timezone.now()输出的是带时区的utc时间，称为active time

### Database
- NAME： 要使用的数据库的名称。对于 SQLite，它是数据库文件的完整路径。当指定路径时，总是使用斜线，即使在 Windows 上也是如此（例如 C:/homes/user/mysite/sqlite3.db）。


# migrate
- link:https://docs.djangoproject.com/zh-hans/4.2/topics/migrations/
- 新建或者修改modules.py
    - makemigrations：修改module.py后使用
    - migrate 然后使用这个
- 删除表后的操作： https://blog.csdn.net/yrx0619/article/details/81387351

- python manage.py command
# QuerySet API 参考
- https://docs.djangoproject.com/zh-hans/4.2/ref/models/querysets/#queryset-api-reference
# 测试
测试文件写在应用下的test.py内；测试系统会自动的在所有以 tests 开头的文件里寻找并执行测试代码。
```
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```
- 运行测试的`python manage.py test polls`
# ORM
## filter
### filter Field  https://docs.djangoproject.com/zh-hans/4.2/ref/models/querysets/#field-lookups
### datatime filter
- https://zhuanlan.zhihu.com/p/113481999
- 可以使用module中datetime 类型的字段名称加上`操作符`来查找符合条件的日期数据 `AlertRecord.objects.filter(end__gt=timezone.now())`
# 路由
## Django如何处理一个请求
- link：
    - https://docs.djangoproject.com/zh-hans/4.2/topics/http/urls/
1. 找到根URLconf模块
    - URLconf是一个纯python代码；位置由setting.py中的 ROOT_URLCONF字段定义，也可以通过中间件设置到httpRequest对象上的urlconf属性上去
    ```python
    # 根urlconf
    from django.urls import path, include

    urlpatterns = [
        # path('admin/', admin.site.urls),
        path('overview/', include('overview.urls')),
        path('grafana/', include('grafana.urls')),
        path('alerts/', include('alerts.urls')),
    ]
    # 模块中的urlconf
    from django.urls import path

    from . import views

    urlpatterns = [
        path("articles/2003/", views.special_case_2003),
        path("articles/<int:year>/", views.year_archive),
        path("articles/<int:year>/<int:month>/", views.month_archive),
        path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    ]
    ```
2. Django加载找到的URLconf模块寻找可用的urlpatterns，它其实是 django.urls.path() 和(或) django.urls.re_path() 实例的序列(sequence)。
3. 按顺序匹配每个url模式，当匹配到第一个后会停止
4. 一旦匹配成功，导入并调用相关的视图，视图获得的参数参照链接
5. 如果没有匹配或者出现异常，会调用一个适当的错误处理视图
## include 
每当 Django 遇到 include() ，它会将匹配到该点的URLconf的任何部分切掉，并将剩余的字符串发送到包含的URLconf进行进一步处理。这实际上将一部分URL 放置于其它URL 下面。

# 视图
## 最简单的视图
- 在应用的view.py中定义处理链接的视图函数
```
def get_handler():
    if request.method == "GET":
        pass
```
- 然后再urlconf中分别把url和处理这个url的视图通过path给对照起来

## action 
- link:https://zhuanlan.zhihu.com/p/278167686
- 视图函数使用action装饰器可以自动生成对该函数的路由
- detail：基于哪个路由生成的新路由
    - 如果是True是基于带id的路由生成的
    - 如果是False，是基于不带id的路由生成的
- methods：什么请求方式会触发被装饰函数的执行
用法
@action(methods=['get'], detail=True)
def 视图类方法
## 使用类视图
