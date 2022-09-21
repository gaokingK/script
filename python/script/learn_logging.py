"""
#关于logger的配置
## link
    - [多模块使用logging、日志回滚](https://www.cnblogs.com/qianyuliang/p/7234217.html)
        - 如果在同一个程序中一直都使用同名的logger，其实会拿到同一个实例，使用这个技巧就可以跨模块调用同样的logger来记录日志。
        - 略
    - [更详细的一篇文章](https://blog.csdn.net/lilong117194/article/details/82852054)
        - 主要参考这个来了解logging模块， 具体的使用看别的
    - [配置日志的几种方式](https://www.cnblogs.com/yyds/p/6885182.html)
    - [logging.handlers.TimedRotatingFileHandler()使用](https://www.codingdict.com/sources/py/logging.handlers/9083.html)
## 问题
    - ValueError: Unable to configure handler 'file_handler'
        - 是yaml里面的file_handler的配置没有写对，比如日志存放的文件夹可能没有创建（他自己不会创建)
    - TimedRotatingFileHandler 另一个程序正在使用此文件,进程无法访问
        - link： https://www.cnblogs.com/zepc007/p/10936623.html
        - 未解决：因为是window上出现的，放在linux就没问题
        - 或者delay=True（有时有用，有时没有用）
    - 如果是按分钟切割， 一次请求持续了5分钟，会在这个请求完成后才把所有的日志给生成出来
    - logger.removeHandler(file_handler) 移除handler
    - 日志应该实例化，而不应该写在自定义的get_logger（）里，如果get_logger()里有添加handler， 那每次调用get_logger()就会添加一个handler，造成重复输出日志
    - root logger 的问题
        - root日志器会重复输出其他日志器输出的日志
    - 文件锁、过滤
    - get_logger/getLogger
        - 如果参数为空，默认获取rootlogger
        - 如果获取name logger不存在，也获取rootlogger
    - ValueError: Unable to configure handler 'file_handler'
        - file_handler 中指定的文件路径应该被创建
## logging 简介
    - logging里定义了五个日志级别， 从低到高分别是debug<info<warning<error<critacal, 也可以自己定义日志级别，但不推荐，因为会对别人带来影响
## logging模块的使用方式介绍
    - 第一种方式是使用logging提供的模块级别的函数 快速使用
    - 第二种方式是使用Logging日志系统的四大组件
    - 其实，logging所提供的模块级别的日志记录函数也是对logging日志系统相关类的封装而已。
## 使用logging提供的模块级别的函数记录日志
    ```
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
    # basicConfig()可接受的其他关键字参数见link
    # logging模块中定义好的可以用于format格式字符串中字段 见link
    logging.debug("This is a debug log.")
    ```
    - basicConfig()可接受的其他关键字参数见link
        - stream: 指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
        - handlers: ：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常.
    - 注意：
        - logging.basicConfig()函数是一个一次性的简单配置工具使，也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作
        - 日志器（Logger）是有层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，其名称为'root'，它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的。
    - 如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息（logging.debug、logging.info等函数的第一个参数），然后将变量数据作为第二个参数*args的值进行传递
    如`logging.warning('%s is %d years old.', 'Tom', 10)`
    -  logging.info()等方法的定义中,除了msg和args参数外，还有一个**kwargs参数。它们支持3个关键字参数: exc_info, stack_info, extra，下面对这几个关键字参数作个说明。
        - exc_info： 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。
        - stack_info： 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。
        - extra： 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。
    - Logger.exception() 创建一个类似于Logger.error()的日志消息
        - Logger.exception()与Logger.error()的区别在于：Logger.exception()将会输出堆栈追踪信息，另外通常只是在一个exception handler中调用该方法。
## logging模块日志流处理流程
在介绍logging模块的高级用法之前，很有必要对logging模块所包含的重要组件以及其工作流程做个全面、简要的介绍，这有助于我们更好的理解我们所写的代码（将会触发什么样的操作）。
    - logging日志模块四大组件
        - 日志器(对应类名：Logger)：提供了应用程序可一直使用的接口
        - 处理器(Handler): 将logger创建的日志记录发送到合适的目的输出
        - 过滤器(Filter): 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
        - 格式器(Formatter): 决定日志记录的最终输出格式
        - 上面所使用的logging模块级别的函数也是通过这些组件对应的类来实现的。
    - 这些组件之间的关系描述：
        - 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
        - 不同的处理器（handler）可以将日志输出到不同的位置；
        - 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
        - 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
        - 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方
        - 日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。
    - logging日志模块相关类及其常用方法介绍
        - logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。
        - 略
    - 略
## 配置日志的几种方式
    - 有三种方式来配置
        - 使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数；
            - logging.basicConfig()也就是这种方式
            - 略
        - 创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容；
        - 创建一个包含配置信息的dict，然后把它传递个dictConfig()函数；
            - 更加灵活，因为我们可把很多的数据转换成字典。
## TimedRotatingFileHandler
- when: midnight [取值](https://docs.python.org/2/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler)

## 一个实际的配置
"""
import logging
import logging.config
import yaml

"""
To: 创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容
如 learn_logging_wingman.conf
# 怎么在里面使用中文呢
- 配置里的propagate属性
    - 这说明simpleExample这个logger在处理完日志记录后，把日志记录传递给了上级的root logger再次做处理，所有才会有两个地方都有日志记录的输出。
    通常，我们都需要显示的指定propagate的值为0，防止日志记录向上层logger传递。
- 我们试着用一个没有在配置文件中定义的logger名称来获取logger：
logger = logging.getLogger('simpleExample1')
    - 当一个日志器没有被设置任何处理器是，系统会去查找该日志器的上层日志器上所设置的日志处理器来处理日志记录。
"""


def logging_by_conf():
    # 读取日志配置文件内容
    logging.config.fileConfig(fname='learn_logging_wingman.conf', )

    # 创建一个日志器logger
    logger = logging.getLogger('simpleExample')

    # 日志输出
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


"""
To: 创建一个包含配置信息的dict，然后把它传递个dictConfig()函数
- 我们可把很多的数据转换成字典。
    - 比如，我们可以使用JSON格式的配置文件、YAML格式的配置文件，然后将它们填充到一个配置字典中；
    - 或者，我们也可以用Python代码构建这个配置字典，或者通过socket接收pickled序列化后的配置信息。总之，你可以使用你的应用程序可以操作的任何方法来构建这个配置字典。
- 字典对象只能包含的key见链接
- 关于外部对象的访问
    - 上面所使用的对象并不限于loggging模块所提供的对象，我们可以实现自己的formatter或handler类
    - 这些类的参数也许需要包含sys.stderr这样的外部对象。如果配置字典对象是使用Python代码构造的，可以直接使用sys.stdout、sys.stderr；
    但是当通过文本文件（如JSON、YAML格式的配置文件）提供配置时就会出现问题，因为在文本文件中，没有标准的方法来区分sys.stderr和字符串'sys.stderr'。
    为了区分它们，配置系统会在字符串值中查找特定的前缀，例如'ext://sys.stderr'中'ext://'会被移除，然后import sys.stderr。
    
以yaml为例：learn_logging_wingman.yml
"""
def logging_by_dict_yaml():

    with open('learn_logging_wingman.yml', 'r') as f_conf:
        dict_conf = yaml.safe_load(f_conf)
    logging.config.dictConfig(dict_conf)

    logger = logging.getLogger('simpleExample')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


"""
To: 一个实际的配置
生产中会把很多配置写在一个文件里
"""
# 会把logger写在conf文件夹下的__init__里
# ls conf
# dev.yml
# __init__.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# import yaml
# import logging.config
#
#
# def get_fold_root():
#     return os.path.dirname(__file__)
#
#
# def check_cfg():
#     r_conf_name = os.path.join(get_fold_root(), "dev.yml")
#     if os.path.exists(r_conf_name):
#         return r_conf_name
#     else:
#         sys.exit(1)
#
#
# with open(check_cfg(), 'r', encoding='utf-8') as f:
#     conf = yaml.safe_load(f)
#
# logging.config.dictConfig(conf.get("log"))
# logger = logging.getLogger()

if __name__ == '__main__':
    # logging_by_conf()
    logging_by_dict_yaml()
