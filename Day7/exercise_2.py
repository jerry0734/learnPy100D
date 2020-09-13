"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
"""
import string
import random

i = 0


def generate_code(code_len=4):
    all_chars = string.digits + string.ascii_letters
    code = ''
    for i in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code


while i < 10:
    i += 1
    print(generate_code())
