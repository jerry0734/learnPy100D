"""
输出100以内所有的素数
"""
from math import sqrt


prime_numbers = []
for num in range(2, 100):
    is_prime = True
    sqrt_num = int(sqrt(num))
    # 注意要从2开始
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        prime_numbers.append(num)
        # print(num)

for prime_number in prime_numbers:
    print(prime_number, end=' ')
