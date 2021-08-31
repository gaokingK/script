# 在函数内生命全局变量，函数重复运行时会不会覆盖

# add = 0
add = [0]

def count(num):
    print("---")
    add.clear()
    add.append(num)
    add.append(num)
    print(add)
    add.pop()
    print(add)


if __name__ == '__main__':
    count(1)
    count(2)
    print(add)