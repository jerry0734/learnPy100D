"""
拆分长字符串
"""
import re


def split_long_string(message):
    longRegex = re.compile(r'[,.，。]')
    messages = longRegex.split(message)

    return messages


message1 = """
独立寒秋，湘江北去，橘子洲头。
看万山红遍，层林尽染；漫江碧透，百舸争流。
鹰击长空，鱼翔浅底，万类霜天竞自由。
怅寥廓，问苍茫大地，谁主沉浮？
携来百侣曾游，忆往昔峥嵘岁月稠。
恰同学少年，风华正茂；书生意气，挥斥方遒。
指点江山，激扬文字，粪土当年万户侯。
曾记否，到中流击水，浪遏飞舟？
"""

messages = split_long_string(message1)
print(messages)
for message in messages:
    # 去换行符
    print(message.strip('\n'))
