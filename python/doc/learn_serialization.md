#### yaml.load() 为什么不安全
[link](https://blog.csdn.net/enemy_sprites/article/details/102571523)
因为PyYaml.load()可以随意的调用任何Python函数，这意味着它可以使用调用任何系统命令os.system()。
```
python -c ‘import yaml; yaml.load("!!python/object/new:os.system [echo EXPLOIT!]")’
```

### pickle/msgpack 是和json一样功能的序列化库 会将数据序列化为bytes