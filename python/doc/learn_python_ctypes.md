# 
- link
    - 腾讯云帮助中心关于ctypes介绍：https://cloud.tencent.com/developer/section/1370537
- ctypes
    - 一些c的数据类型
    ```py
    from ctypes import CDLL, c_void_p, c_uint, c_bool, c_ulong, c_double, byref, CFUNCTYPE, c_long, c_int, c_char_p
    
    # CDLL represent一个由dll库转化到的类的实例
    QCAP = CDLL("QCAP.X64.DLL")
    # 调用方式可以使用.:QCAP.xxx 或者index：QCAP["xxx"]
  
    # c_void_p # 生成c中的void类型的一个变量
    # CFUNCTYPE -> prototype function 可以通过不同方式调用函数原型来创建可调用对象。
    # ctypes 通过 CFUNCTYPE 支持回调函数。
    ```
    - c中函数的返回值是把要接受返回值的变量的地址给传进去
    ```py
    QCAP_CREATE_ANIMATION_CLIP(&pclip)
    # 在ctypes中对应的方法是
    p_clip = c_void_p(0)
    QCAP_CREATE_ANIMATION_CLIP( byref(pclip))
    ```
    
- 回调函数
    - 函数指针作为某个函数的参数， 回调函数就是一个通过函数指针调用的函数。
    - 通常我们说的指针变量是指向一个整型、字符型或数组等变量，而函数指针是指向函数。
    - 函数指针可以像一般函数一样，用于调用函数、传递参数。
    - python 通过 CFUNCTYPE 支持回调函数
        - https://docs.python.org/zh-cn/3.7/library/ctypes.html#callback-functions
        - CFUNCTYPE是工厂函数， 使用 cdecl 调用约定 创建 回调函数 的类型
        - 工厂函数都是用返回值类型作为第一个参数，回掉函数的参数类型作为剩余参数。
        - 示例
        ```py
        # 总的来说就是以对数组排序为场景举了一个使用回调函数的例子
        # qsort是 调用回调函数 的函数，对qsort的参数做了一些说明
        # 创建回调函数需要两步
        # 第一步创建 回调函数 的类型
        CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int)) # 参数需要与实际的回调函数保持一致
        # 第二步，写实际的回调函数，并绑定
        def py_cmp_func(a, b):
            # 这里只随便写一点东西，真正需要实现的功能看链接
            print("py_cmp_func", a[0], b[0])
            return 0
        cmp_func = CMPFUNC(py_cmp_func)
        # 怎么调用回调函数呢？这里也举一个例子
        qsort(ia, len(ia), sizeof(c_int), py_cmp_func) # 这里qsort的解释见链接
        ```
      - 注意
        - 确保维持 CFUNCTYPE() 对象的引用与它们在 C 代码中的使用期一样长。？为什么呢， 难道使用时不就维持着吗？
        - 可能是这种情况， 在调用C代码之前不能把这个对象给del掉，而这种情况是可行的，比如手动del CFUNCTYPE_OBJ

- 问题
    - c 中void不是代表空吗？怎么还有 device_0 = c_void_p(1) 这种写法呢？
    - 为什么c_void_p, c_bool 为什么这些数据类型有的带p，有的不带p呢?
    - 调用约定
        - 如[调用规范stdcall、cdecl、fastcall、thiscall 、naked call的汇编理解](https://www.cnblogs.com/kwinwei/p/11527081.html) 
    - 回调函数也有类型吗？
    - C语言中函数名是需要大写吗？


# python 和c 混合编程
- link
    - https://blog.csdn.net/m0_37822019/article/details/79709617?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.no_search_link&spm=1001.2101.3001.4242.1
- Python 的 ctypes 要使用 C 函数，需要先将 C 编译成动态链接库的形式，
即 Windows 下的 .dll 文件，或者 Linux 下的 .so 文件。先来看一下 ctypes 怎么使用 C 标准库。
    - Windows 系统下的 C 标准库动态链接文件为 msvcrt.dll
     (一般在目录 C:\Windows\System32 和 C:\Windows\SysWOW64 下分别对应 32-bit 和 64-bit，使用时不用刻意区分，Python 会选择合适的)
    - Linux 系统下的 C 标准库动态链接文件为 libc.so.6 (以 64-bit Ubuntu 系统为例， 在目录 /lib/x86_64-linux-gnu 下)
  
# about python
- 一种判断kw的方式
```
if kw.pop("use_errno", False):
       flags |= _FUNCFLAG_USE_ERRNO
```
- 这个->是代表啥意思？返回值的类型？
```
def CFUNCTYPE(restype, *argtypes, **kw):
    """CFUNCTYPE(restype, *argtypes,
                 use_errno=False, use_last_error=False) -> function prototype.  # there

    restype: the result type
```