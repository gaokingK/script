import inspect

# sys.__getframe().f_code.co_name) 只能获取类中方法名
# func.__code__.co_name 获取函数的名字, 但如果func被装饰器装饰, 即使wrapper有functools.wraps, 也只能解决func.__name__, co_name仍然会是wrapper

import inspect


def get_function_name(status=None):
    """
    获取正在运行函数(或方法)名称
    """
    # return inspect.stack()[1][3]
    if status:
        print("[{}] {}".format(inspect.stack()[1][3], status))
    else:
        return inspect.stack()[1][3]
