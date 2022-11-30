class TestProperty(object):
    def __init__(self):
        self.__owningDevice__ = ''

    # @property
    # def owningDevice(self):
    #     return self._owningDevice # 带不带 __
    #
    # @owningDevice.setter
    # def owningDevice(self, device):
    #     self._owningDevice = device

    @property
    def owningDevice(self):
        return self.__owningDevice

    @owningDevice.setter
    def owningDevice(self, device):
        # device.func() 这样就可以双向注册了
        self.__owningDevice = device

    # @property
    # def owningDevice(self):
    #     return self.__owningDevice__
    #
    # @owningDevice.setter
    # def owningDevice(self, device):
    #     self.__owningDevice__ = device


def debug_Demo1():
    demo = TestProperty()
    # demo.__owningDevice # 提示没有这个属性
    print(demo.owningDevice)
    demo.owningDevice = 2  # 这样设置
    print(demo.owningDevice)


if __name__ == '__main__':
    t = TestProperty()
