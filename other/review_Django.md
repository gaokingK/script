# 帮助信息
- 文档的阅读说明：https://docs.djangoproject.com/zh-hans/4.2/intro/whatsnext/
- index: https://docs.djangoproject.com/zh-hans/4.2/topics/
# 正文
### 运行端口
- 配置：link：https://blog.csdn.net/lkballip/article/details/109205373
- 在命令中`python manage.py runserver xxx`
### shell 
- 运行djadmin:`shell` 命令`python manage.py shell` 是可交互窗口
# migrate
- link:https://docs.djangoproject.com/zh-hans/4.2/topics/migrations/
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

## 使用类视图
