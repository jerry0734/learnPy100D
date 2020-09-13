"""
杨辉三角
copied from website
"""


def triangles():
    p = [1]
    while True:
        yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [p[i] + p[i+1] for i in range(len(p)-1)]
        p = [1] + p + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
