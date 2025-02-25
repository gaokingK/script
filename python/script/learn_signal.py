"""
TO: python提供的信号处理功能
- link: 
    - https://www.cnblogs.com/madsnotes/articles/5688681.html
    - https://docs.python.org/zh-cn/3/library/signal.html
- 所谓的信号处理 kill -9 pid 就是向pid发送一个信号
- 实际上signal, pause，kill和alarm都是Linux应用编程中常见的C库函数，在这里，我们只不过是用Python语言来实现了一下。
- signal包的核心是使用signal.signal()函数来预设(register)信号处理函数，然后等程序实际接收到对象的信号时，执行注册的处理函数
- 要注意，signal包主要是针对UNIX平台(比如Linux, MAC OS)，而Windows内核中由于对信号机制的支持不充分，所以在Windows上的Python不能发挥信号系统的功能。
- 信号（signal）-- 进程之间通讯的方式，是一种软件中断。一个进程一旦接收到信号就会打断原来的程序执行流程来处理信号。
"""
"""
TO: 不同的信号
- signal.SIG_IGN 来自键盘的中断 (CTRL + C)。默认的动作是引发 KeyboardInterrupt。
    - 在pycharm使用启动按钮启动时，ctrl + c 不会引发任何动作，但点击停止按钮是等价于ctrl + c
    - 需要在终端中使用命令python xxx.py 然后ctrl + c 会生效
"""


"""
TO: signal.signal(signalnum, handler)
# handler也可以是一些内置的处理函数比如handler为signal.SIG_IGN时，信号被无视(ignore)。当handler为singal.SIG_DFL，进程采取默认操作(default)
"""
import signal

def signal_handler(sig, frame):
    print("Interrupt received! Rolling back and exiting...")
    if db.is_active:
        db.rollback()
        db.close()
    sys.exit(0)



if __name__ == '__main__':
    db = get_db()
    signal.signal(signal.SIGINT, signal_handler)  # 第一个参数是要处理的信号类型
    
    # 注册后，执行下面的代码，如果执行过程中收到了SIGINT信号，就会执行signal_handler
    while True:
        pass # do something #
