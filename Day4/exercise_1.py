"""
输入一个正整数判断是不是素数(prime number)
提示：素数指的是只能被1和自身整除的大于1的整数
"""
from math import sqrt
num = int(input("input a number: "))
# 最大取到平方根的整数，可以有效减少循环的次数
sqrt_num = sqrt(num)
is_prime = True

if num > 1:
    for i in range(2, int(sqrt_num) + 1):
        if num % i == 0:
            is_prime = False
        else:
            is_prime = True
else:
    print("This is not prime number.")

if is_prime:
    print("{} is prime number.".format(num))
else:
    print("{} is not prime number.".format(num))
