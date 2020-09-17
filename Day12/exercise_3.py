"""
替换字符串中的不良内容
"""
import re


def change_bad_message(message):
    messageRegex = re.compile(r'fuck|shit|傻[Xx]|屎')

    treated_message = messageRegex.sub('*', message)

    return treated_message


message1 = '你这个傻X ; 哈哈哈;你是shit'
message1 = change_bad_message(message1)
print(message1)
message2 = '拉屎去，fuck鱿'
message2 = change_bad_message(message2)
print(message2)
