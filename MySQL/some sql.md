```sql
alter table server_cluster_create_ticket_data add column domain varchar(100) not null default "";
drop table server_cluster_create_ticket_data;
alter table server_cluster_create_ticket_data drop column domain;
CHECK TABLE server_cluster_create_ticket_data;
SELECT @@sql_mode;
SELECT * FROM performance_schema.data_locks;
SHOW TABLE STATUS WHERE Name = 'server_cluster_create_ticket_data';
SELECT * FROM performance_schema.data_locks;
SHOW ENGINE INNODB STATUS;
SHOW TABLE STATUS WHERE Name = 'server_cluster_create_ticket_data';
SHOW STATUS LIKE 'Threads_connected';
KiLL 1263205;
SHOW full PROCESSLIST;
SHOW VARIABLES LIKE 'log_error';
SELECT * FROM information_schema.PROCESSLIST;
SELECT * FROM information_schema.innodb_trx;
show process_list;
SELECT 
    dl.ENGINE_LOCK_ID AS lock_id,
    dl.LOCK_TYPE AS lock_type,
    dl.LOCK_MODE AS lock_mode,
    dl.LOCK_STATUS AS lock_status,
    dl.OBJECT_SCHEMA AS schema_name,
    dl.OBJECT_NAME AS table_name,
    dl.INDEX_NAME AS index_name,
    t.THREAD_ID AS thread_id,
    t.PROCESSLIST_ID AS connection_id,
    t.PROCESSLIST_USER AS user_name,
    t.PROCESSLIST_HOST AS host_name,
    t.PROCESSLIST_COMMAND AS command
FROM 
    performance_schema.data_locks dl
JOIN 
    performance_schema.threads t 
ON 
    dl.THREAD_ID = t.THREAD_ID;
    
 
```
