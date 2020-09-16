"""
读写二进制文件
`'b'`二进制模式
"""
filename_1 = 'Day11\\res\\ball.png'
filename_2 = 'Day11\\res\\ball_2.png'
try:
    with open('Day11\\res\\ball.png', 'rb') as binary_file_1:
        data = binary_file_1.read()
        print(data)
    with open(filename_2, 'wb') as binary_file_2:
        binary_file_2.write(data)
except FileNotFoundError:
    print("File is missing.")
except IOError:
    print("Error occured while opening this file.")
