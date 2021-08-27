#!/usr/bin/python3


class Singleton:
    def __init__(self):
        print("instance")

    def func1(self):
        print("func1 is run...")
        pass

singleton = Singleton()
