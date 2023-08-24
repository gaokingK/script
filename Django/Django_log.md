# 日志
> django 的日志使用
- 最简单的使用：https://blog.csdn.net/zhouzhiwengang/article/details/119606262
- 进阶：
    - https://zhuanlan.zhihu.com/p/133864368
    - https://pythondjango.cn/django/advanced/14-logging/
## 注意
- handler和loggers中的leveal并不冲突，因为一个logger可能有多个handler
- 日志切割时，需要加上noreload 参数， python manage.py runserver --noreload  这样才会有效，否则就会提示log文件被另外一个程序使用
### 过滤器
- link：
    - Django 日志过滤器实战: https://www.guoyong.dev/programing/django-logging-filter-in-action/
- Django 的日志配置采用标准的 Python 日志配置方式，默认采用 dictConfig 的格式
- A  filter is used to provide additional control over which log records are passed from logger to handler.
- filter 函数里一定要有返回True，要不然所有的日志都不显示了
```cs
# 配置文件的格式是dictConfig的格式
'filters': {
    'require_debug_false': { # 指定一个别名 'require_debug_false'作为 key，value 又是一个 dict
        # 这个 dict 用来描述过滤器如何被实例化。其中，'()'作为特殊的 key 用来指定过滤器是哪个类的实例（见 logging.config.DictConfigurator）。其它的 key （如extr_info）用来指定实例化过滤器是传给 __init__ 方法的参数。
        '()': 'django.utils.log.RequireDebugFalse',
        "extr_info": "bar",
    }
},
# 过滤器
class StaticFieldFilter(logging.Filter):

    def __init__(self, extr_info):
        super().__init__()
        self.extr_info = extr_info

    // def filter(self, record): # 重载filter方法 日志信息是record.msg
    //     for k, v in self.static_fields.items():
    //         setattr(record, k, v)
    //     return True
    def filter(self, record: logging.LogRecord) -> bool:
        record.exc_text = None # 不让控制台中打印异常栈
        record.exc_info = None
        if "/alerts/api/v2/alerts" in record.msg:
            return False
        else:
            return True
```
### django.template.base.VariableDoesNotExist: Failed lookup for key [exception_notes] in 报错，
- 这种就一直往上翻，看最上面的错误，下面的都是无用的信息，但是这些额外的信息是django的bug：https://blog.csdn.net/weixin_40841752/article/details/79312314
    - 找到解决办法了

### 一个实际的配置
```cs
# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        "default": {
            "format": '%(asctime)s %(name)s  %(pathname)s:%(lineno)d %(module)s:%(funcName)s '
                      '%(levelname)s- %(message)s',
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    # "filters": {
    #     "special": {
    #         "()": "utils.StaticFieldFilter",
    #         "extr_info": "bar",
    #     },
    #     # "require_debug_true": {
    #     #     "()": "django.utils.log.RequireDebugTrue",
    #     # },
    # },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            # 'filters': ['special']
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            'when': "D",
            'interval': 1,
            'formatter': 'default'
        },
        "request": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/request.log'),
            'formatter': 'default'
        },
        "server": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/server.log'),
            'formatter': 'simple'
        },
        "root": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/root.log'),
            'formatter': 'default'
        },

        "db_backends": {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/db_backends.log'),
            'formatter': 'default'
        },
        "autoreload": {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/autoreload.log'),
            'formatter': 'default'
        }
    },
    'loggers': {
        # 应用中自定义日志记录器
        'mylogger': {
            'level': 'DEBUG',
            'handlers': ['file', "console"],   # file的放在前面，不受console过滤函数的影响，而经过console处理后会再传到root里，所以root的就受影响了
            'propagate': True,
        },
        'test_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
        # 下面这些不注释掉的话报错的话会打印出好多日志
        # "django": {
        #     "level": "DEBUG",
        #     "handlers": ["console", "file"],
        #     'propagate': False,
        # },
        # "django.request": {
        #     "level": "DEBUG",
        #     "handlers": ["request"],
        #     'propagate': False,
        # },
        # "django.server": {
        #     "level": "DEBUG",
        #     "handlers": ["server"],
        #     'propagate': False,
        # },
        # # 只注释下面两个的话控制台会打印好多backend和autoreload的日志
        # "django.db.backends": {
        #     "level": "DEBUG",
        #     "handlers": ["db_backends"],
        #     'propagate': False,
        # },
        # "django.utils.autoreload": {
        #     "level": "INFO",
        #     "handlers": ["autoreload"],
        #     'propagate': False,
        # }
    },
    'root': {
        "level": "DEBUG",
        "handlers": ["root"],
    }
}
```