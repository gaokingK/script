import sys
import traceback
# from retrying import retry

from learn_get_func_name import get_function_name


def is_repeat():
    """
    确保函数出错后只重试一次
    """
    if func_stack[-1] != func_stack[-2]:
        print("即将重复执行 func_stack[{}]".format(func_stack))
        func_stack.clear()
        return True
    return False



func_stack = []
have_exception = True
def catch_except(func):
    """用来测试遇到重复异常时退出"""
    def wrapper(*args, **kwargs):
        global func_stack
        try:
            func_stack.append(func.__code__.co_name)
            # print(func_stack)
            func(*args, **kwargs)
        except AssertionError as e1:

            # exc_type, exc_value, exc_obj_1 = sys.exc_info()
            # print(exc_obj_1)
            # e_1 = traceback.print_exception(exc_type, exc_value, exc_obj_1, limit=2,)
            #                                 file=sys.stdout)
            # e_1 = traceback.format_exc(limit=2)
            # raise e
            exception_handler()
            # kwargs["have_exception"] = have_exception
            func_stack.append(func.__code__.co_name)
            # func(*args, **kwargs)

            # print(func_stack)

            if is_repeat():
                exc_type, exc_value, exc_obj_2 = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_obj_2,
                                          limit=2)
            else:
                func(*args, **kwargs)
                # func_stack.clear()
                # raise e2

            # try:
            #     func_stack.append(func.__code__.co_name)
            #     func(*args, **kwargs)
            # except AssertionError as e2:
            #     # print(exc_obj_2)
            #     # e_2 = traceback.format_exc(limit=2)
            #
            #     # print(e_1, end="\n\n")
            #     # print(e_2, end="\n\n")
            #     # if exc_obj_1 != exc_obj_2:
            #
            #     # print("nosence")


    return wrapper


@catch_except
# @retry
def test_catch_exception():
    get_function_name("start")
    # if have_exception:
    #     raise AssertionError("出错了")

    test_catch_exception_child()
    # test_catch_exception_child()
    if have_exception:
        raise AssertionError("{}出错了".format(get_function_name()))
    get_function_name("end")


times = 0
@catch_except
def test_catch_exception_child(have_exception=True):
    global times
    times += 1
    get_function_name("第{}次 start".format(times))
    if have_exception:
        raise AssertionError("第{}次运行{}出错了".format(times, get_function_name()))
    get_function_name("第{}次 end".format(times))


def exception_handler():
    global have_exception
    have_exception = False
    get_function_name("end")


from tenacity import *

def return_last_value(retry_state):
    print("执行回调函数")
    global have_exception
    have_exception = False
    # print(retry_state.outcome.result())  # 表示返回原函数的返回值

def is_false(value):
    return value is False

@retry(stop=stop_after_attempt(1),
       retry_error_callback=return_last_value,
       # retry=retry_if_result(is_false))
       retry=retry_if_exception_type(AssertionError))
def test_retry():
    print("start...")
    if have_exception:
        print("have error")
        assert False
    print("end...")


from retrying import retry

@retry
def do_something_unreliable():
    if have_exception:
        print("have error")
        assert False
    else:
        print("Awesome sauce!")


if __name__ == '__main__':
    # 捕获异常
    test_catch_exception()
    # test_catch_exception()
    # test_retry()
    # do_something_unreliable()
