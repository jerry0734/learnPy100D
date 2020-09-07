"""
输入两个正整数，计算它们的最大公约数和最小公倍数
"""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
number = 0
if y > x:
    x, y = y, x

print("x={0}, y={1}".format(x, y))

for i in range(1, y + 1):
    if x % i == 0 and y % i == 0:
        number = i

print("The greatest common divisor of {} & {} is {}.".format(x, y, number))
print("The least common multiple of {} & {} is {}.".format(
        x, y, x * y // number))
