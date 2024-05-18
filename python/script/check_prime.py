import time
import math
def check_prime(num):
    if num % 2 == 0:
        return False
    # if num <= 4:
    if num <= 5:
        if num ==4:
            return False
        else:
            return True
    equal_limit = int(math.sqrt(num))
    if num % equal_limit == 0:
        return False
    # 对于范围没有过滤的待确定数 如39,采用下面的方法会判定为素数
    for i in range(5, equal_limit, 6):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False
    return True


def check_prime_secrue(num):
    # 安全版本，对于检验范围没有经过过滤的也能检测出来
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    if num <= 5:
        return True
    equal_limit = int(math.sqrt(num))
    if num % equal_limit == 0:
        return False
    for i in range(5, equal_limit, 6):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False
    return True


if __name__ == "__main__":
    # 代表2和3
    check_num = 39
    print('%d is prime' % check_num) if check_prime(check_num) else print("%d isn't prime" % check_num)
    print('%d is prime' % check_num) if check_prime_secrue(check_num) else print("%d isn't prime" % check_num)
    start_time = time.process_time()
    all_count = 2
    for i in range(5, 1000000, 6):
        all_count += 1 if check_prime_secrue(i) else 0
        all_count += 1 if check_prime_secrue(i + 2) else 0
    all_time = time.process_time() - start_time
    print("all_time is %s" % all_time)
    print("all count is %d " % all_count)
