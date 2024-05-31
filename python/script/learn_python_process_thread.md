# TO: 进程和线程的使用及区别
## hello_world
```py
def func(arg1, arg2):
    pass
target = threading.Thread(target=func, args=(arg1, arg2)) # 注意这里时func 不能写为func() 这样虽然也能运行，但是下面的语句就不会运行了 
# 如果只有一个参数args=(arg1,) 因为传进去的是个元组
target.start()
target.join(timeout=10) # join的意思时主程序会等待进程结束后才结束 timeout如果有值，主进程会等待10s， 10s后会继续执行，如果没有其他代码，会等这个线程结束
# 如果不join，主进程结束后子线程也会结束
# 一个线程可以被join多次调用 ,结束了后也能join
# start和join要放在两个循环里面，因为join会阻塞主进程，只有当前线程结束后才会继续运行
# 在 Python 中，当你调用线程（threading.Thread 对象）的 join 方法时，调用这个方法的线程将会被阻塞，直到被 join 的线程终止。这允许程序等待线程完成其任务，确保线程有序和安全地退出。重要的是要理解 join 方法仅阻塞调用它的线程，而不会影响其他线程的执行。
```

## 注意
- cpu是指一核cpu
- 并行性和并发性：并行性是同一时刻多个任务同时执行，并发性是一个时间段内，会执行多个任务。但并行也需要多个cpu
## 区别
- 独立性：进程是操作系统中资源分配的最小单位，线程是cpu调度的最小单位；进程拥有独立的内存空间和资源，线程是进程内部的执行单元，多个线程共享一个进程的空间和资源。
- 资源消耗：因为进程需要独立的内存空间和资源，所以进程的创建和销毁是比较消耗资源的；而由于线程共享进程的资源，创建和销毁的开销比较小。
- 通信方式：进程之间需要通过操作系统提供的IPC（进程间通信）机制如管道、消息队列、共享内存来进行通信；而线程因为能直接访问共享内存，所以通信相对方便
- 稳定性：进程之间是相互独立的，但由于线程共享进程的资源，一个线程的崩溃可能会影响整个进程
- 并行和并发：在多核cpu上，进程能做到真正的并行；线程在单核处理器上通过多任务切换实现并发执行，但不同线程之间可能会因为GIL（全局解释器锁）的存在而受限制。
- 在python中，I/O密集型的适合采用多线程来承载，计算密集型的适合使用多进程来完成
- 对于其他语言：在一些具有多核处理器的系统中，可以实现并行执行，多个线程可以同时在不同的核心上运行。但是，如果是单核处理器或者操作系统采用时间片轮转调度策略，那么多线程通常会在并发执行的方式下进行。

## 一个进程可以同时占用多个cpu吗
一个进程通常不能同时占用多个CPU核心，因为在大多数操作系统中，进程是操作系统分配资源的基本单位，而每个CPU核心都是一个独立的执行单元。然而，有一些情况下可以实现多个CPU核心上的并行执行，例如：

多线程并行： 一个进程可以创建多个线程，这些线程可以在多个CPU核心上并行执行。每个线程共享同一个进程的资源，如内存空间，但是它们可以在不同的CPU核心上并行运行。

多进程并行： 一个进程可以创建多个子进程，这些子进程可以在不同的CPU核心上并行执行。每个子进程有自己独立的内存空间和资源，可以在多个CPU核心上并行运行。

并行计算： 在某些特定的应用场景下，可以使用并行计算的技术，将一个任务分解成多个子任务，每个子任务在不同的CPU核心上执行，最终汇总结果。

向量化指令： 一些特定的处理器提供了向量化指令，允许在单个指令中处理多个数据元素，从而实现数据级并行。

需要注意的是，多个CPU核心的并行执行需要操作系统和硬件的支持。一些操作系统会自动将进程或线程分配到可用的CPU核心上，从而实现并行执行。但是，要充分利用多核处理器的性能，需要进行适当的并行编程和优化。

# 在python中，线程在执行过程中遇到IO时，操作系统会怎么调度他呢
- 发生IO，操作系统会将此进程至于阻塞状态，然后回执行其他处于就绪状态的进程，同时 cpu会监控IO操作，一旦IO操作完成，相关的线程会被修改为就绪状态，等待操作系统根据调度策略（如搭配使用优先级、轮转、公平分享等）再次调度。

- 在 Python 中运行的一个线程如果在执行过程中发生了 IO 操作（比如使用 wget 命令将日志输出到文件），操作系统会执行以下步骤来调度线程及 IO 操作：

- 阻塞 (Blocking):当线程试图进行读写文件等 IO 操作时，线程会进入一个等待状态，因为 IO 操作通常比 CPU 计算要慢得多。在这个等待状态中，线程不会继续执行 Python 代码，操作系统会将其标记为 "阻塞" 状态。

- 上下文切换 (Context Switch):一旦线程被阻塞，操作系统会执行一个上下文切换，这是一个把 CPU 的控制权从当前线程转移给另一个线程的过程。目的是让 CPU 不在 IO 阻塞的线程上浪费时间，而是去执行其他就绪（Ready）状态的线程。

- 等待 IO 完成:IO 操作在后台执行，与此同时，线程保持阻塞。操作系统会监控该 IO 请求，等待 IO 操作完成。对于写入文件的操作，操作系统通常会将数据写入内核缓冲区（Kernel Buffer），然后由系统在适当的时候将数据写入磁盘。

- 唤醒线程 (Wakeup):当 IO 操作完成后，操作系统会唤醒被阻塞的线程。这意味着操作系统会再次将该线程置于就绪状态，准备获取 CPU 时间来继续执行。
  
- 重新调度 (Rescheduling):随着 CPU 时间变得可用，操作系统会根据调度策略（如搭配使用优先级、轮转、公平分享等）重新调度之前阻塞的线程，以便它们可以继续执行剩余的任务。
  
- 总而言之，Python 线程在执行 IO 操作时会被挂起，释放 CPU 以供其他线程使用。操作系统管理着线程间的协作，确保 CPU 资源有效利用，尤其是在面对阻塞操作时。这些都是内核级别的调度细节，对于 Python 开发者来说，通常是透明的。

### 如果一个python程序里面新建了3个进程，那么一个有几个python的进程
- 4个 一个启动应用程序的原始进程和3个用户在程序里新建的进程，每个进程都有自己独立的python解释器会话和内存空间。这样可以有效利用多核CPU，因为每个用户都有自己的GIL

# 确保多进程之间访问共享数据的安全性是通过使用以下方法实现的：
multiprocessing.Manager: 提供进程间共享的高级管理对象，如列表、字典等。
multiprocessing.Value 和 multiprocessing.Array: 共享简单数据类型和数组，并使用内置的锁保护。
multiprocessing.Queue: 用于进程间通信的线程安全队列。
multiprocessing.Lock: 保护任何共享数据，确保在同一时刻只有一个进程能访问临界区。
根据实际需求选择合适的数据共享和同步方法，确保多进程环境下的数据安全性、同步性及一致性。

# 线程状态隔离和锁的使用适用场景有区别吗
是的，线程状态隔离和锁的使用在适用场景上有不同的侧重点和应用方式。下面详细说明它们各自的适用场景以及优缺点：

### 线程状态隔离

#### 适用场景
- **独立线程状态**: 每个线程都需要独立的状态，并且这些状态在不同线程之间完全独立。一些线程特有的数据不需要在线程之间共享或传递。
- **避免数据竞争**: 数据在某个线程中的操作不会影响其他线程的状态，例如处理特定的请求、用户对话等。
- **提升性能**: 通过避免锁和同步机制来提升程序性能。例如，不需要锁的开销。

#### 示例应用
- **Web服务器**: 每个线程处理独立的HTTP请求，且每个请求都有自己的上下文数据。
- **任务执行器**: 线程在执行任务时需要独立的配置和状态，而不需要共享状态。

#### 优缺点
- **优点**: 
  - 简单易用。
  - 没有锁的竞争，提升了性能。
  - 减少了死锁的风险。
- **缺点**:
  - 不能处理需要共享状态的场景。
  - 更适合于彼此独立的任务，无法利用线程之间的数据共享。

#### 示例代码
```python
import threading

local_data = threading.local()

def worker():
    local_data.value = threading.current_thread().name
    print(f'Thread {local_data.value} is running')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 锁的使用

#### 适用场景
- **共享资源同步**: 多线程需要访问和修改共享资源。锁可以保证在同一时刻只有一个线程能访问和修改共享资源，从而避免数据竞争和不一致性。
- **原子操作**: 需要对共享数据进行多个步骤的原子操作，确保这些步骤在其他线程干扰之前完成。
- **数据一致性**: 需要确保数据的一致性和完整性。例如计数器递增、链表操作等。

#### 示例应用
- **计数器**: 多线程环境下，多个线程需要递增一个全局计数器。
- **资源池**: 线程从资源池中获取和释放资源，需要确保资源的唯一性和可用性。
- **生产者-消费者问题**: 需要在生产和消费的动作之间进行同步，确保数据的正确处理。

#### 优缺点
- **优点**: 
  - 保证数据一致性和完整性。
  - 适用于需要共享和同步的场景。
  - 可以实现复杂的并发控制。
- **缺点**:
  - 可能带来性能下降，特别是在锁竞争激烈的情况下。
  - 存在死锁的风险，需要小心设计。
  - 增加了代码的复杂性和可维护性。

#### 示例代码
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        local_counter = counter
        local_counter += 1
        counter = local_counter

threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Final counter value: {counter}')
```

### 总结
- **线程状态隔离** 更适用于线程间状态彼此独立不需要共享的情况。适用于需要避免锁竞争并提升效率的场景。
- **锁的使用** 则更适用于需要对共享数据进行同步访问的情况。适用于需要保证数据正确性和一致性的场景。

综合来看，具体使用哪种方式取决于实际的应用场景和需求。在设计多线程程序时，需要根据数据共享的要求、性能需求、安全性等多方面因素来选择合适的方式。

# 怎么做到线程状态的隔离，协程怎么做隔离？有没有什么轻量级的方法，python内置的？
在 Python 中，实现线程状态和协程状态的隔离是确保并行和并发编程中数据一致性和安全性的关键。以下是实现这些隔离的几种方法：

### 线程状态的隔离

#### 1. 使用 `threading.local()`
Python 提供了 `threading.local()` 类，这使得每个线程都有其独立的状态。我们可以将需要隔离的状态绑定到 `threading.local()` 对象上，使每个线程拥有独立的这些变量。

示例代码：
```python
import threading

# 创建一个线程本地数据对象
local_data = threading.local()

def worker():
    # 每个线程都设置自己的 local_data 属性
    local_data.some_data = threading.current_thread().name
    print(f'Thread {threading.current_thread().name} has data: {local_data.some_data}')

# 创建并启动多个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

#### 2. 使用锁（Lock）
对于共享资源的访问，使用锁（`threading.Lock`）来确保同一时间只有一个线程能访问该资源，从而保证数据的一致性和正确性。

示例代码：
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        local_counter = counter
        local_counter += 1
        counter = local_counter

threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Final counter value: {counter}')
```

### 协程状态的隔离

#### 1. 使用 `contextvars` 模块
Python 3.7 引入了 `contextvars` 模块，这个模块提供了协程状态隔离的能力，可以在不同的协程中使用独立的上下文变量。

示例代码：
```python
import asyncio
import contextvars

# 创建一个上下文变量
var = contextvars.ContextVar('var', default='default')

async def worker(value):
    # 设置上下文变量的值
    var.set(value)
    print(f'Coroutine {value}, var value: {var.get()}')
    await asyncio.sleep(1)
    print(f'Coroutine {value}, var value after sleep: {var.get()}')

async def main():
    await asyncio.gather(
        worker('A'),
        worker('B'),
    )

asyncio.run(main())
```

#### 2. 使用 Task Local 存储
异步库如 `asyncio` 本身就支持任务本地存储，虽然不像线程本地存储那么直接，但可以通过上下文变量来实现。

示例代码：
```python
import asyncio

# 创建一个任务本地数据存储字典
task_data = {}

async def worker(value):
    task_data[asyncio.current_task()] = value
    print(f'Coroutine {value}, data: {task_data[asyncio.current_task()]}')
    await asyncio.sleep(1)
    print(f'Coroutine {value}, data after sleep: {task_data[asyncio.current_task()]}')

async def main():
    await asyncio.gather(
        worker('A'),
        worker('B'),
    )

asyncio.run(main())
```
### 轻量级方法和内置支持
- `threading.local()` 和 `contextvars` 是 Python 内置的轻量级方法，可以有效隔离线程和协程状态。
- 对于线程隔离，可以使用 `threading.Lock` 等同步原语来保障资源访问安全。
- 对于协程隔离，使用 `contextvars.ContextVar` 进行上下文变量的隔离是最灵活和推荐的方式。

这些方法不需要第三方库，直接利用 Python 标准库提供的工具就可以实现线程和协程状态的隔离。总之，根据不同的使用场景，选择合适的状态隔离技术可以显著提升并发代码的安全性和可维护性。
