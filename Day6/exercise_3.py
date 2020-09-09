"""
实现判断一个数是不是素数的函数
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


# for i in range(1, 20):
#     prime = is_prime(i)
#     print("{}, {}".format(i, prime))
