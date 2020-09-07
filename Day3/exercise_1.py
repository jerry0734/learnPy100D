"""
英制单位英寸与公制单位厘米互换
"""
print("英寸与厘米互换小程序")

while True:
    unit_option = int(input("请选择原始数值的单位，输入1为英寸，输入2为厘米，输入其他则退出: "))
    if unit_option != 1 and unit_option != 2:
        print('退出程序！')
        break
    else:
        value = float(input("请输入长度: "))
        if unit_option == 1:
            cm_value = value * 2.54
            print("{value}英寸={cm_value:.2f}厘米".format(
                value=value, cm_value=cm_value))
        else:
            inch_value = value / 2.54
            print("{value}厘米={inch_value:.2f}英寸".format(value=value,
                                                        inch_value=inch_value))
