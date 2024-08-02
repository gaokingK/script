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
### cerebro上显示的是索引主分片的大小总和，不包括副本分片的大小
