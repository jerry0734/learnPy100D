"""
读写文本文件
| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |
"""
filename = 'Day11\\res\\textfile.txt'
filename_2 = 'Day11\\res\\another_textfile.txt'
try:
    with open(filename, 'r') as text_file_1:
        message = text_file_1.read()
        print(message)
    with open(filename_2, 'w') as text_file_2:
        text_file_2.write(message)
except FileNotFoundError:
    print("File not found!")
