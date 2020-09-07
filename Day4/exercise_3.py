"""
打印三角形图案
"""


def show_triangle_1(number):
    for i in range(1, number + 1):
        print(i * '*')
    print()


def show_triangle_2(number):
    for i in range(1, number + 1):
        print((number - i) * ' ' + i * '*')
    print()


def show_triangle_3(number):
    for i in range(1, number + 1):
        side = (number - i) * ' '
        middle = (2 * i - 1) * '*'
        print(side + middle + side)
    print()


while True:
    number = int(input("Please input a number: "))
    show_triangle_1(number)
    show_triangle_2(number)
    show_triangle_3(number)
