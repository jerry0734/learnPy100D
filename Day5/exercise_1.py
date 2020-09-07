"""
生成斐波那契数列的前20个数
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""
fibonacci_numbers = []

a = 0
b = 1
i = 0
while i < 20:
    a, b = b, a + b
    fibonacci_numbers.append(a)
    i += 1

print(fibonacci_numbers)
