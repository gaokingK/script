#### [Mixin是什么概念](https://www.zhihu.com/question/20778853)
- Min-in 混入的意思
- ##### 功能和特点：
  - Mixin 实质上是利用语言特性（比如 Ruby 的 include 语法、Python 的多重继承）来更简洁地实现组合模式。
  - 但通常混入 Mixin 的类和 Mixin 类本身不是 is-a 的关系，混入 Mixin 类是为了添加某些（可选的）功能。自由地混入 Mixin 类就可以灵活地为被混入的类添加不同的功能
  - 在python中，把要组合的内容放在单个的类中，然后去让别的类去继承这些类来获得各种各样的功能
  ```python
  class TagMixin(object):
      pass
  class Post(Model, TagMixin):
      pass
  ```
  - python这种使用多重继承的做法：
    - TagMixin 类是单一职责的
    - TagMixin 类对宿主类（Post）一无所知，除了要求宿主类有 ident 和 kind 这两个属性（等价于 Java 中要求宿主类实现 Entity 接口）
    - 宿主类的主体逻辑不会因为去掉 TagMixin 而受到影响，同时也不存在超类方法调用（super）以避免引入 MRO 查找顺序问题

- ##### Mixin和多重继承
    - 因为Mixin的出现就是为了解决多重继承的问题，那么多重继承有什么问题呢？
      >1. 结构复杂化：如果是单一继承，一个类的父类是什么，父类的父类是什么，都很明确，因为只有单一的继承关系，然而如果是多重继承的话，一个类有多个父类，这些父类又有自己的父类，那么类之间的关系就很复杂了。
      2. 优先顺序模糊：假如我有A，C类同时继承了基类，B类继承了A类，然后D类又同时继承了B和C类，所以D类继承父类的方法的顺序应该是D、B、A、C还是D、B、C、A，或者是其他的顺序，很不明确。
      3. 功能冲突：因为多重继承有多个父类，所以当不同的父类中有相同的方法是就会产生冲突。如果B类和C类同时又有相同的方法时，D继承的是哪个方法就不明确了，因为存在两种可能性。
    - 为了解决多重继承的问题，Java引入了接口 （interface）技术，Lisp、Ruby引入了 Mix-in 技术。
    - 继承强调 I am，Mixin 强调 I can
    - Mixin是静动态语言的组合模式的实现，只有方法，不实例化（所以Mixin class本身没有成员函数）《effective python》里item26专门介绍了Mixin。

#### 其他链接
- https://www.liaoxuefeng.com/wiki/897692888725344/923030524000032
