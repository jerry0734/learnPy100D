"""
输入年份判断是不是闰年

"""
try:
    year = int(input("请输入年份: "))
except ValueError:
    print("请按照正确的形式输入年份")
else:
    print("您输入的年份为: {}".format(year))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("这一年是闰年呢")
    else:
        print("这不是闰年呢")
