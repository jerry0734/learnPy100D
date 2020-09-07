"""
输入三条边长，如果能构成三角形就计算周长和面积
"""


def triangle_area(a, b, c):
    """求三角形面积"""
    s = (a + b + c) / 2  # 三角形半周长
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and c + b > a:
    area = triangle_area(a, b, c)
    print("面积为{:2f}".format(area))
else:
    print("不能构成三角形")
