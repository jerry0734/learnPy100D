"""
练习1：定义一个类描述数字时钟
"""


class Clock():

    def __init__(self, hour, minute, second):
        self.second = second
        self.minute = minute
        self.hour = hour

    def show_clock(self):
        # :02d的作用是指定两位格式,填充左边为0，如9，会被填充为09
        print(f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}")

    def run_clock(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
        print(f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}")


clock1 = Clock(23, 59, 59)
clock1.show_clock()
clock1.run_clock()
clock2 = Clock(12, 48, 59)
clock2.run_clock()
clock3 = Clock(6, 59, 59)
clock3.run_clock()
