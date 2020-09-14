"""
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
"""
from math import sqrt


class A_Dot():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move_position(self, move_to_x, move_to_y):
        self.x = move_to_x
        self.y = move_to_y

    def get_distance(self, another):
        distance_x = another.x - self.x
        print(distance_x)
        distance_y = another.y - self.y
        print(distance_y)
        return sqrt(distance_x ** 2 + distance_y ** 2)


dot_1 = A_Dot(3, 4)
dot_1.move_position(5, 12)
dot_2 = A_Dot(0, 0)
print(dot_1.get_distance(dot_2))
