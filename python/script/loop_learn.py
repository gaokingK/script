def loop1():
    for i in range(1, 5):
        for j in range(2, 7):
            print(i, j)
            if j == 5:
                break
        else:
            continue
        break

def loop2():
    for i in range(1, 5):
        for j in range(2, 7):
            print(i, j)
            if j == 6:
                break
        else:
            break
        continue
if __name__ == "__main__":
    loop2()