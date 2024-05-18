### 为什么序列化后再反序列化得到的结果和原来的不一样呢？
```python
import yaml
document = """
a: 1
b:
  c: 3
  d: 4
"""
print(yaml.dump(yaml.load(document)))
# 输出是：
a: 1
b: {c: 3, d: 4}
```
- 这是因为PyYAML默认会根据一个集合中是否有嵌套的集合来决定用哪种格式表示这个集合， 如果一个集合中嵌套有其他集合（如上面），那么会使用块样式来表示，否则会使用流样式来表示。
- 如果想要集合总是以流样式表示，可以将 dump() 方法的 default_flow_style 参数值设为 True `yaml.dump(yaml.load(document), default_flow_style=True)`

### yaml.load() 为什么不安全
[link](https://blog.csdn.net/enemy_sprites/article/details/102571523)
因为PyYaml.load()可以随意的调用任何Python函数，这意味着它可以使用调用任何系统命令os.system()。
```
python -c ‘import yaml; yaml.load("!!python/object/new:os.system [echo EXPLOIT!]")’
```

### pickle/msgpack 是和json一样功能的序列化库 会将数据序列化为bytes