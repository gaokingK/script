# TO: python 中队列的使用
- queue包提供了同步的，线程安全的队列类
- 当队列为空而执行get操作时，该操作将会被阻塞;当队列满而执行put操作时，该操作同样会被阻塞。
# link：
- https://blog.csdn.net/weixin_43533825/article/details/89155648
# hello_world
```py
from queue import Queue
# 先进先出队列 FIFO
q=Queue(maxsize=5)  # maxsize=0则不限制大小
# 放入队列
q.put("msg")
# 读取
q.get()
q.task_done() # 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。
``` 
# 不同的队列 和队列常用的基本方法
- queue.Queue(maxsize=0)：先进先出，最早进入队列的数据先出队列；
- queue.LifoQueue(maxsize=0)：最后进入队列的数据先出队列；
- PriorityQueue(maxsize=0)：比较队列中每个数据的大小，值最小的数据先出队列；
- queue.SimpleQueue：与①相似，只是一个简单队列，缺少一些高级的方法。
```cs
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False，Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当于Queue.get(False)，非阻塞方法，为空就报错
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait()
Queue.task_done()
每当执行一次put操作，unfinished_tasks就加一，可理解为put代表增加了一个任务；
每执行一次task_done操作，unfinished_tasks就减一，可以把task_done放在get操作之后，当get成功执行后，再执行task_done使得unfinished_tasks减一，代表完成了一个任务；

而join则通过判断unfinished_tasks是否为零执行wait操作；
Queue.join() 实际上意味着等到队列为空，再执行别的操作
```

# TO: 多线程中其他的东西
- event 可以用来判断某个事件是否结束，相当于flag
```py
end_event=threading.Event()

# 线程1结束后
end_event.set()
# 线程2
while not self.end_event.is_set() or not self.need_dns_url.empty():
```
