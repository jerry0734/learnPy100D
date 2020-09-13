"""
设计一个函数返回传入的列表中最大和第二大的元素的值
"""
import random


def get_max(numbers):
    max_1 = numbers[0]
    max_2 = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_1:
            max_2, max_1 = max_1, numbers[i]
        elif numbers[i] > max_2:
            max_2 = numbers[i]
        print(i, max_1, max_2)
    return max_1, max_2


numbers = []
i = 0
while i < 10:
    i += 1
    numbers.append(random.randint(0, 1000))

print(numbers)
print(get_max(numbers))
