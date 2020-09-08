"""
找出10000以内的完美数
"""
perfect_numbers = []
for num in range(2, 10000):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        perfect_numbers.append(num)

print(perfect_numbers)
