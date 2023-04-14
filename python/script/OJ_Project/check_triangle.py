def check(*args):
    args = args[0]
    if len(args) != 3:
        return False
    for i in range(3):
        if args[i] + args[i+1] <= args[i+2]:
            return False
    else:
        if len(set(args)) == 1:
            print(1)
        elif len(set(args)) == 2:
            print(2)
        else:
            print(3)
        return True

if __name__ == '__main__':
    d = [3, 3, 1]
    a, b, c = d
    # check(a, b, c)
    print(check(d))
