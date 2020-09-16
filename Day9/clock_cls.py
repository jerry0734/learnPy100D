"""
@classmethod
cls类方法
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
"""
from time import time, localtime


class Clock():

    def __init__(self, hour, minute, second):
        self.second = second
        self.minute = minute
        self.hour = hour

    # 加入cls参数，不需要类实例化即可使用
    @classmethod
    def now(cls):
        current_time = localtime(time())
        return cls(current_time.tm_hour, current_time.tm_min,
                   current_time.tm_sec)

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0

    def show_clock(self):
        # :02d的作用是指定两位格式,填充左边为0，如9，会被填充为09
        print(f"{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}")


# Clock.show_clock()
Clock.now()
# Clock.show_clock()
