#!/usr/bin/python3

from pynput.keyboard import KeyCode, Controller, Key
import pyautogui


def print_by_pyautogui():
    result = input("按键码为{}的键值为:")
    pyautogui.keyDown('num0')
    pyautogui.keyUp('num0')
    print("result:{}".format(result))
    #print("按下num_lock键")
def print_keycode(keycode):
    controller = Controller()
    controller.press("a")
    controller.release("a")
    key = KeyCode.from_vk(keycode)
    print(type(key))
    print(key.value)
    result = input("按键码为{}的键值为:".format(keycode))
    #controller.press(key)
    #controller.release(key)
    controller.press("a")
    controller.release("a")
    controller.press("0")
#    print("按下num_lock键")
#    controller.press(Key.num_lock)
#    controller.release(Key.num_lock)
    controller.release("0")
    controller.press("1")
    controller.release("1")
    controller.press(Key.enter)
    controller.release(Key.enter)
#    print(result)

        
if __name__ == "__main__":
    #print_keycode(65535)
    print_by_pyautogui()
