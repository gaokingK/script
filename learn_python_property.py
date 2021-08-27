class TestProperty(object):
    def __init__(self):
        self.__size__ = ''

    # @property
    # def size(self):
    #     return self._size
    #
    # @size.setter
    # def size(self, value):
    #     self._size = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    # @property
    # def size(self):
    #     return self.__size__
    #
    # @size.setter
    # def size(self, value):
    #     self.__size__ = value


if __name__ == '__main__':
    t = TestProperty()
