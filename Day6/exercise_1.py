"""
实现计算求最大公约数和最小公倍数的函数
"""
def get_gcd(x, y):
    gcd = 1
    if y > x:
        x, y = y, x
    for i in range(1, y + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

def get_lcm(x, y):
    lcm = x * y // get_gcd(x, y)
    return lcm

gcd = get_gcd(12, 18)
lcm = get_lcm(12, 18)
print(gcd)
print(lcm)
