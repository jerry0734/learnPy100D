"""
百分制成绩转换为等级制成绩
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E
"""

score = int(input("请输入成绩："))

if score >= 90:
    print("A grade.")
elif score < 90 and score >= 80:
    print("B grade.")
elif score < 80 and score >= 70:
    print("C grade")
elif score < 70 and score >= 60:
    print("D grade")
elif score < 60:
    print("E grade")
else:
    print("分数输入错误")
