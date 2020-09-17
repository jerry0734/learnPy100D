"""
验证输入用户名和QQ号是否有效并给出对应的提示信息
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def check_name(username, qq_number):
    name_regex = re.compile(r'^[a-zA-Z0-9_]{6,20}')
    number_regex = re.compile(r'^[1-9]\d{4,11}$')

    name_vaild = name_regex.match(username)
    number_vaild = number_regex.match(qq_number)

    if name_vaild:
        print(f'{username} is OK.')
    else:
        print(f'{username} is BAD.')

    if number_vaild:
        print(f'{qq_number} is OK.')
    else:
        print(f'{qq_number} is BAD.')


while True:
    name = input('Please input your name: ')
    number = input('Please input your number: ')

    check_name(name, number)
