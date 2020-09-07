"""
输入圆的半径计算计算周长和面积
"""
import math
radius = float(input("请输入圆的半径，单位为cm： "))

perimeter = math.pi * radius * 2
area = (radius ** 2) * math.pi

# 直接取用pi，而不是3.14，因此小数部分会有偏差
print("PI={}".format(math.pi))
print("您输入的半径为{:.2f}厘米".format(radius))
print("周长为{:.2f}厘米".format(perimeter))
print("面积为{:.2f}平方厘米".format(area))
