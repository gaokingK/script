# 了解为啥会抛出两次异常 During handling of the above exception, another exception occurred
# 因为异常1虽然被捕获了,但是excpet 语句并没有走完(里面又发生了异常2), 所以异常2和异常1被一起抛了出来(并且先出现的异常的在前)
# 只有excpet 无异常走完了, 这次异常才不会被解释器所捕捉到

have_exception = True
get_exception = False
times = 0


def func_action():
    global times
    times += 1
    if have_exception:
        raise AssertionError(f"with some error in 第{times}次")


def catch_exception():
    global get_exception
    try:
        func_action()
    except AssertionError as e:
        print("不 raise e")
        get_exception = True
    if get_exception:
        func_action()


if __name__ == '__main__':
    catch_exception()
