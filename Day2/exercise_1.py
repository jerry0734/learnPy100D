"""
华氏温度转摄氏温度
C to F: F=C×1.8+32
F to C: C=(F-32)÷1.8
"""
fahrenheit = float(input("请输入华氏温度: "))


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


# celsius = round(fahrenheit_to_celsius(fahrenheit), 1)
# fahrenheit = round(fahrenheit, 1)
# print(str(fahrenheit) + '华氏度等于' + str(celsius) + '摄氏度')

# another solve the 小数点
celsius = fahrenheit_to_celsius(fahrenheit)
print("%.1f 华氏度等于 %.1f 摄氏度" % (fahrenheit, celsius))
