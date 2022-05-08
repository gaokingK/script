from learn_python_class_obj import TestClass

def super_func():
    # 调用learn_class_obj 中为其添加的func1方法
    print("调用learn_class_obj 中为其添加的func1方法")
    func1()


class TestClass2:
    def __init__(self, name=5):
        self.testclass = TestClass()
        self.name = name


    def func1(self):
        print("testclass1 func is running...")


if __name__ == '__main__':
    common = TestClass2(7)
    common.func1()
    common2 = TestClass2(8)
    common2.func1()
