import keyword as kw

# 1.基本数据类型分为:
#     数值(整数，浮点，复数)
#     字符串
#     列表（有序,可重复）
#     元组（不可修改）
#     字典
#     集合（无序，不可重复），集合默认使用set(),不可使用{}直接声明，因{}是用来创建字典


def whileTest():
    i = 0
    while i < 7:
        if i % 2 == 0:
            print("偶数")
        else:
            print("奇数")
        i += 1


if __name__ == '__main__':
    # print(kw.kwlist)
    whileTest()



