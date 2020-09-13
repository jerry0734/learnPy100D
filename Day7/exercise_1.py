"""
在屏幕上显示跑马灯文字
"""
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(1)
        """
        第一次循环：'北京欢迎你为你开天辟地…………'
        第二次循环：'京欢迎你为你开天辟地…………' + '北'
        第三次循环：'欢迎你为你开天辟地…………北' + '京'
        """
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
