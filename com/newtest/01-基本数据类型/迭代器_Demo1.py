import sys
#迭代器操作


def fun1():
    list1=['1','a','b','c']
    it1=iter(list1)
    # print(next(it1))
    # print(next(it1))

    # 正常循环
    # for i in it1:
    #     print(i,end="|")

    # while循环方式
    # while True:
    #     try:
    #         print(next(it1))
    #     except StopIteration:
    #         sys.exit()




if __name__ == '__main__':
    # print("aaa")
    fun1()