### celery中的beat是干什么的 定时任务起不来
- beat 是一个用于定时调度任务的组件。它是 Celery 的定时任务调度器，负责按照预定义的时间表触发任务的执行，而不需要手动调用。
- beat只是到时间把任务触发一下，实际上还是发给worker处理，所以worker也是需要起来的
- `celery -A celery_worker.celery beat --loglevel=info --logfile="/var/log/mp/app/devops-wukongiaasserv/${POD_NAME}_celery.log" &`
### windows起不起来
```
celery -A celery_worker.celery worker --loglevel=info 报错
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-wukongiaasserv\lib\site-packages\billiard\spawn.py", line 164, in spawn_main
    exitcode = _main(fd)
  File "C:\Users\CN-jinweijiangOD\Desktop\project\ENV\devops-wukongiaasserv\lib\site-packages\billiard\spawn.py", line 206, in _main
    self = pickle.load(from_parent)
ModuleNotFoundError: No module named 'app'
```
### 在windows上运行celery worker正确姿势
- link: https://beltxman.com/4176.html
- solo pool （单进程执行） 即在 worker 所在的进程和线程上处理任务，严格来说，他不算一个 pool `celery -A celery_worker.celery worker --pool=solo --loglevel=info`
- Threads pool 线程池类型中的线程由操作系统内核直接管理，只要 Python 的 ThreadPoolExector 支持 Windows 线程，这种池类型就可以在 Windows 上工作，推荐使用在IO负载的场景 `celery -A app.app worker -l info -P threads --concurrency=4`
- gevent pool 通过 Greenlet 实现并发。 Greenlet 类似于 asyncio 中的协程。当一个任务等待它的结果时，它会让给另一个任务来做它的事情。

因为 gevent 包支持 Windows ，只要您了解一些 gevent 的复杂性， gevent pool 仍然是 Windows 上IO任务处理的合适选项。
`C:\Dev\celery-demo>celery -A app.app worker -l info -P gevent --concurrency=4`
### 定时任务的任务名 
- 用的是celery.task(name="xxx")中的name
```py
 ####### CELERY ###################
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                       'redis+sentinel://redis-sentinel-headless-rs-dfs-dev-rke.ninja-public.svc.cluster.local:26379/mymaster')
    # CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis+sentinel://redis-sentinel-headless-rs-dfs-dev-rke.ninja-public.svc.cluster.local:26379/0')
    CELERY_IMPORTS = ('app.ticket.dns_check_task', 'app.store_server.task', 'app.store.task','app.ticket.delete_store_dns_check_task')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')
    SYNC_STORE_HOUR = os.environ.get('SYNC_STORE_HOUR', 1)
    SYNC_STORE_MIN = os.environ.get('SYNC_STORE_MIN', 30)

    CELERY_BEAT_SCHEDULE = {
        'server_cluster_dns_check_cronxxx': {
            'task': 'server_cluster_dns_check_cron1',
            'schedule': crontab(minute="30", hour="0"),
            # 'schedule': crontab(minute="*/3"),
        },
    }


@celery.task(name="server_cluster_dns_check_cron1")
@distributed_lock("periodic_server_cluster_dns_check")
def server_cluster_dns_check_cron2():
    """
    定时检查DNS是否创建成功
    :return:
    """
    dns_service = DnsService()
    ticket_data_list = dns_service.get_create_server_cluster_tickets_with_step_3()

    cron_res = []

    for ticket_data in ticket_data_list:
        cluster_dto_obj = ClusterInfoDTO(**ticket_data["ticket_extend_data"])
        dns_operation = DnsOperation(cluster_info=[cluster_dto_obj])
        result = dns_operation.add_dns_check(ticket_data["ticket_id"])
        cron_res.append(result)

    logger.info(f"crontab execute: {ticket_data_list}")

    return cron_res


```
