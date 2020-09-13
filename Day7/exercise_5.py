"""
计算指定的年月日是这一年的第几天
"""


def get_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days(year, month, date):
    is_leap_year = get_leap_year(year)
    month_list = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    days = 0
    temp_list = month_list[is_leap_year]
    for i in range(month - 1):
        days += temp_list[i]
    days += date
    return days


print(get_days(2020, 1, 1))
print(get_days(1980, 11, 28))
print(get_days(2020, 2, 29))
