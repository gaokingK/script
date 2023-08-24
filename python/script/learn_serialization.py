#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# 序列化(dump)和反序列化(load)以及 pickling/unpickling 
    序列化 变量从内存中变为可存储或者可传输的 过程
    反序列化 变量从序列化的对象重新读到内存里的过程 是流转为对象
    picking 是序列化在python中的称呼

# yaml
yaml 简单使用 link: https://www.cnblogs.com/klb561/p/9326677.html
yaml 构造器、表示器、解析器 link：https://www.cnblogs.com/klb561/p/9326677.html
### yaml 语法 
- doc
   - https://www.runoob.com/w3cnote/yaml-intro.html
   - https://ruanyifeng.com/blog/2016/07/yaml.html
- 变量被引用时如下，处于开头的位置时需要加上引号`"{{ nginx.conf80 }}"` 这个可能时ansible特有的内容
- 只有列表的元素才带`-`, 字典的键和值都不带, 如果缩进是一样的，说明是同一级
```
---
all: # 最上层的key，value是一个字典
  vars: # value也是一个字典
    cluster: "mylocal" 
    appdir: "/apt"
    logmounts: 
      - /var/log
      - /home
    logs:
      - name: qtrade # 这个-并不是name的，而是和name同一等级的
        file: /home/qdam/qtrade*/*/*.log # file 和 name 的缩进是一样的，就是属于同一个字典
        encoding: gbk
{
   all: {
      var: {
         "cluster": "mylocal",
         "appdir": "/apt",
         "logmounts": ["/var/log", "/home"]
         "logs": [{"name": "qtrade", "file": "/home/qdam/qtrade*/*/*.log", "encoding": "gbk"}]
      }
   }
}
```
# json
    json中load和loads区别: https://www.cnblogs.com/bigtreei/p/10466518.html
    load loads 区别: 前者读取文件/后者读字符串 可以把多的s 理解为 string(load string)
    dump dumps 区别: 前者存入文件/后者转为字符串
        - conf_str = json.dumps(conf, indent=4) 这样就是格式化的数据，不再是一整行
    json文件 格式 必须有一个主节点，这个主节点，没有主节点的话必须使用{}把所有内容括起来
    所有的key，value必须用双引号包括
# pickle/cpickle
    cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
"""
import yaml

f_r = open(r"./learn_yaml_load_config.yml", encoding="gbk", errors="ignore")
f_w = open(r"./learn_yaml_dump_config.yml", "w")


def simple_yaml_load():
    # 没有Loader 会报错，因为load能随意调用任何python函数，
    # 所以需要用该参数指定一个加载器：FullLoader，这个加载器禁止执行任意参数
    # config = yaml.load(f, Loader=yaml.FullLoader)
    config = yaml.safe_load(f_r)
    print(config)


def multiple_yaml_load():
    # config: generator
    config = yaml.load_all(f_r, Loader=yaml.FullLoader)
    for config in config:
        print(config)


def simple_yaml_dump(obj, f_name=None):
    dump_res = yaml.dump(obj, stream=f_name)  # 有stream和没有stream的返回时不一样的
    print(dump_res, )
    print("dump_res's types: {}".format(type(dump_res)))


def multiple_yaml_dump():
    obj1 = {"key": "value", "key1": "value"}
    obj2 = [0, 1, 2]
    dump_res = yaml.dump_all([obj1, obj2], stream=f_w)
    print(dump_res)
    print("dump_res's types: {}".format(type(dump_res)))

# 上面是使用yaml 序列化python的内置对象（int、float、str、list、dict、bool、time、datetime）
# 怎么序列化自定义的对象呢？


class Person(yaml.YAMLObject):
    # 不重新声明这个变量也是可以的，他的默认值是（!python/object:__main__.Person)
    yaml_tag = "!person"

    def __init__(self, name, age):
        """
        yaml.YAMLObject用元类来注册一个构造器，让你把yaml节点转为Python对象实例
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def __repr__(self):
        """
        表示器是返回实例的自我描述信息：print(instance)
        这里用表示器（也就是代码里的 repr() 函数）来让你把Python对象转为yaml节点
        不加这个magic方法，也能正常的dump和load
        :return:
        """
        return '{}(name={}, age={})'.format(self.__class__.__name__,
                                            self.name, self.age)


def serialization_instance():
    # 序列化与反序列化python对象实例
    jam = Person("jame", 20)
    print(jam)
    dump_res = yaml.dump(jam)
    print(dump_res)

    # yaml.constructor.ConstructorError: could not determine a constructor for
    # the tag '!persson'
    load_res = yaml.load('!person {name: jam, age: 20}', Loader=yaml.FullLoader)
    print(load_res)
    print("type of load_res %s" % (type(load_res)))


# 上面的类的实例虽然能被序列化，可是类是通过元类的方式，怎么序列化正常定义的类呢
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person({} {})".format(self.name, self.age)


if __name__ == '__main__':
    # simple_yaml_load()
    # multiple_yaml_load()
    # simple_yaml_dump({"key": "value"}, f_name=f_w)
    # multiple_yaml_dump()

    # serialization_instance()

    # 序列化正常定义的类
    jam = People("gagaga", 22)
    print(yaml.dump(jam))
    print(yaml.load(yaml.dump(jam), Loader=yaml.FullLoader))
    print(yaml.load("!!python/object:__main__.People {age: 22, name: gagaga}",
                    Loader=yaml.FullLoader))

    # 创建表示器
    def people_repr(dumper, data):
        # represent_mapping表示器，用于dict
        return dumper.represent_mapping(u"!people",
                                        {"name": data.name, "age": data.age})
    # 添加表示器
    yaml.add_representer(People, people_repr)
    print(yaml.dump(jam))

    # 构造器
    def people_cons(loader, node):
        value = loader.construct_mapping(node)
        name = value["name"]
        age = value["age"]
        return People(name, age)
    # 这个是为指定的yaml标签添加构造器
    yaml.add_constructor(u"!people", people_cons)
    jam = yaml.load("!people {name: wawa, age: 20}", Loader=yaml.FullLoader)
    print(jam)
    print("over")
