### 类方法、静态方法、实例方法

### copy.copy 与 copy.deepcopy不同的原因
[link](https://blog.csdn.net/u010712012/article/details/79754132)
与其他的OOP语言存储变量不同，Python中为变量赋值，并不是将值赋给变量，而是将对值的引用复制给变量
```
a = [1,2,3]
b = a 将对变量a的引用赋值给b
b[0] = 5这不是赋值，而是改变b[0]数据块所指的值
```
简单的object，copy与deepcopy没有区别，而复杂的object(对象中嵌套对象的)，copy与deepcopy在是引用还是复制其子对象（如嵌套在里面的list）就有所

### 单例模式的几种实现方法
[link](https://www.cnblogs.com/huchong/p/8244279.html)
某些类我们希望在程序运行期间只有一个实例存在，比如读取配置信息的appconfig类
#### 实现单例的几种方法
##### 通过模块
python的模块就是一个天然的单例模式，模块在第一次导入时会生成.pyc文件，在以后import的时候，会直接加载.pyc文件，而不会再重新执行模块代码