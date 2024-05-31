# link
- https://blog.csdn.net/qq_43654142/article/details/107413405
- https://blog.csdn.net/weixin_41594007/article/details/79485847
- [一个多线程在多核CPU下交替执行的例子](https://blog.csdn.net/qq_40808154/article/details/89398076)

# 一些疑问？
- 为什么更换解释器的方式不推荐？
- 多线程使用C语言完成，然后在用python调C？
- 如果每个终端中都搞一个python程序去运行？是不是能提高？

# 名词
- 数据完整性
- 状态同步

# 一些问题
### 什么是GIL？GIL的作用是什么？
- GIL(Global Interpreter Lock) 即全局解释器锁。
- 每个 线程 在执行时都需要获取这把锁后才能执行， 以此来保证同一时刻只有一个线程在使用CPU（无论是单核还是多核），即多线程并行并不是真正意义上的同时执行。


### GIL的作用范围是什么？和Python语言的关系是怎样的
- 在使用CPython解释器的python程序， Cpython会加上GIL，来保证同一时刻只有一个线程在执行。
- Python语言和GIL没有什么关系。仅仅是由于历史原因在Cpython释器)，难以移除GIL。
- 我们需要明确的一点是GIL并不是Python的特性，Python完全可以不依赖于GIL。它是在虚拟机(解实现Python解析器(CPython)时所引入的一个概念。
- 同样一段代码可以通过CPython，PyPy，Psyco等不同的Python执行环境来执行。像其中的JPython就没有GIL。然而因为CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python

### 为什么会有GIL？
- Guido van Rossum（吉多·范罗苏姆）创建Python的时候就只考虑了单核CPU，解决多线程之间数据完整性和状态同步的最简单办法就是加锁，所以就有了GIL这把超级大锁。
- Cpython解释器只允许拥有GIL才能运行程序。
- GIL是为了保证在解释器级别的线程唯一使用共享资源（CPU）
- 由于大量的程序开发者接收了这套机制,现在代码量越来越多,已经不容易通过c代码去解决这个问题。

### 一些GIL的误区
- Python使用多进程是可以利用多核的CPU资源的。
- 多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁。然后可以换另一个上。
- 我们需要明确的一点是GIL并不是Python的特性，Python完全可以不依赖于GIL。它是在实现Python解析器(CPython)时所引入的一个概念。

### 如何绕过GIL的限制
- 更换Cpython解释器（不推荐）
- 用多进程完成多线程的任务
- 在使用多线程可以使用c语言去实现

### 什么时候会释放GIL锁
- 遇到像 I/O操作这种 会有时间空闲情况 造成cpu闲置的情况会释放GIL
- 会有一个专门ticks进行计数 一旦ticks数值达到100 这个时候释放GIL锁 线程之间开始竞争GIL锁(说明: ticks这个数值可以进行设置来延长或者缩减获得GIL锁的线程使用cpu的时间)
- 解释器不间断运行了1000字节码（Py2）或运行15毫秒（Py3）

### 互斥锁和GIL锁的关系、GIL锁是线程安全的吗？有了GIL锁为什么还要有互斥锁？
- 互斥锁 : 多线程时,保证修改共享数据时有序的修改,不会产生数据修改混乱
- GIL锁  : 保证同一时刻只有一个线程能使用到cpu
- GIL不是线程安全的
    - 下面的代码就能说明，原因是t1在取n还未加时，t2获取到了锁，并且完成了，然后t1又取到了锁，完成后返回了n，这时t2返回的n就被覆盖了，链接1中有详细的解释。
    ```
    import threading
    n = 0
    def add():
        global n
        for i in range(1000000):
            n = n + 1
    def sub():
        global n
        for i in range(1000000):
            n = n - 1
    if __name__ == '__main__':
        t1 = threading.Thread(target=add)
        t2 = threading.Thread(target=sub)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("n的值为:", n)
    ```
- 假设有一个场景：假设只有一个进程,这个进程中有两个线程 Thread1,Thread2, 要修改共享的数据date, 并且有互斥锁
    - 多线程运行，假设Thread1获得GIL可以使用cpu，这时Thread1获得 互斥锁lock,Thread1可以改date数据(但并没有开始修改数据)
    - Thread1线程在修改date数据前发生了 I/O操作 或者 ticks计数满100 (注意就是没有运行到修改data数据),这个时候 Thread1 让出了GIL,GIL锁可以被竞争
    - Thread1 和 Thread2 开始竞争 GIL (注意:如果Thread1是因为 I/O 阻塞 让出的GIL Thread2必定拿到GIL,如果Thread1是因为ticks计数满100让出GIL 这个时候 Thread1 和 Thread2 公平竞争)
    - 假设 Thread2正好获得了GIL, 运行代码去修改共享数据date,由于Thread1有互斥锁lock，所以Thread2无法更改共享数据date,这时Thread2让出GIL锁 , GIL锁再次发生竞争
    - 假设Thread1又抢到GIL，由于其有互斥锁Lock所以其可以继续修改共享数据data,当Thread1修改完数据释放互斥锁lock, Thread2在获得GIL与lock后才可对data进行修改
    - 如果不加互斥锁，就保证不了数据完整性和



### GIL的好处和坏处？
- 避免了大量的加锁解锁的好处;
- 使数据更加安全，解决多线程间的数据完整性和状态同步。
- 使得比较容易的实现对多线程的支持

- 多核处理器退化成单核处理器，只能并发不能并行。

### 多线程多进程的选择
- 线程和进程切换都需要开销，进程切换的代价比较大

- 对于I/O密集型，选择多线程，因为线程遇到I/O会自动释放GIL，可以换另一个线程上（这样就相当于有两个线程在同时执行）把单线程换成多线程，就可以在不同的cpu上抢，效率就比单线程高
- 对于计算密集型，只适合多进程。