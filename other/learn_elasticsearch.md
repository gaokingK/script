# 调整最大分片数解决因为分片数满了不能新建索引 每个节点1000->1200

# cerebro上rest不能用的时候可以试试curl
```js
curl -u elastic:password123 -X GET "https://localhost:9200" --insecure -H 'Content-Type: application/json' -d'
{
  "persistent": {
    "cluster.max_shards_per_node": 2000
  }
}
'
# --insecure 选项用于跳过 SSL 证书验证，仅在测试环境中使用
```
### cerebro报错Elasticsearch output fails with "String index out of range: 0" when using include_fields processor #8117
- This can happen if you have a / character too many in the index url for example an URL like https://elasticsearch.example.com//_index_template/index_name will cause this error. fix it by removing the double slash // you should end up with https://elasticsearch.example.com/_index_template/index_name if you concat strings this is likely to happen
### cerebro上显示的是索引主分片的大小总和，不包括副本分片的大小
### 日志的存储任务（flink）写es的node节点，UQ组件查询配置的是coordinate节点

### 每个物理机8个实例，6个数据实例，其他两个是查询、master、协调节点 
es就是个分布式数据库没啥复杂的架构，三个以上的master，其他节点根据需要部署，对外9200、内部9300，都是配置文件指定的可修改
