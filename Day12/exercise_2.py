"""
从一段文字中提取出国内手机号码
"""
import re


def find_phone_number(message):
    # phoneRegex = re.compile(r'^1[3458]\d{9}$')
    """
    (?<=exp) 匹配exp后面的位置
    (?=exp) 匹配exp前面的位置
    """
    phoneRegex = re.compile(r'(?<=\d)1[34578]\d{9}(?=\d)')
    strings = phoneRegex.findall(message)

    print(strings)


message = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
find_phone_number(message)
