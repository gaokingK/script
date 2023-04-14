import time

all_calc_count = 0
note = {}


def get_number(n):
    global all_calc_count
    all_calc_count += 1
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if note.get(n):
        return note.get(n)
    else:
        res = get_number(n - 1) + get_number(n - 2)
        note[n] = res
        return res
    # else:
    #     a = 1
    #     b = 2
    #     temp = 0
    #     for i in range(3, n):
    #         temp = a + b
    #         a = b
    #         b = temp
    #     return temp


def get_number2(n):
    global all_calc_count
    all_calc_count += 1
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        a = 1
        b = 2
        temp = 0
        for i in range(3, n+1):
            temp = a + b
            a = b
            b = temp
        return temp


if __name__ == '__main__':
    a = time.process_time()
    n = 300

    print(f"res is: {get_number(n)}")
    print(f"res is: {get_number2(n)}")
    print(f"all calc count is {all_calc_count}, len note is {len(note)}")
    b = time.process_time()
    print(f"all time is {b - a}")
