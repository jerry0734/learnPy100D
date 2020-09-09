"""
写一个程序判断输入的正整数是不是回文素数
"""
from exercise_3 import is_prime
from exercise_2 import is_palindrome


def is_prime_and_palindrome(num):
    if is_prime(num) == is_palindrome(num):
        print("{} 是回文素数".format(num))
    else:
        print("{} 不是回文素数".format(num))


num_list = [11, 101, 131, 151, 181, 191]
for num in num_list:
    is_prime_and_palindrome(num)
