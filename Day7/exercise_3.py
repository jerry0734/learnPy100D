"""
设计一个函数返回给定文件名的后缀名
"""


def get_suffix(filename, has_dot=False):
    """
    rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1
    """
    position = filename.rfind('.')
    print(position)  # 显示位于哪个位置
    if position > 0 and position < len(filename) - 1:
        if not has_dot:
            # hasdot 参数是为了是否显示后缀名前的点
            index = position + 1
        else:
            index = position
        return filename[index:]
    else:
        return ' '


suffix = get_suffix('filename.txt', has_dot=True)
print(suffix)
print(get_suffix('ggg'))
