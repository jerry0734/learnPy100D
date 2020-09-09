"""
实现判断一个数是不是回文数的函数
"""


def is_palindrome(num):
    reverse = num
    sum = 0
    while reverse > 0:
        sum = sum * 10 + reverse % 10
        reverse //= 10
    return sum == num


print(is_palindrome(121))
print(is_palindrome(20211202))
