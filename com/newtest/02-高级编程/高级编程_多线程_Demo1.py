# 声明多线程的两种方式
# 函数式
# 类式


import _thread
import time


def printTime(tName):
    print('线程{0},开始运行...'.format(tName))


if __name__ == '__main__':
    # try:
    _thread.start_new(printTime, ('thread1',))
    _thread.start_new(printTime, ('thread2',))
    # except:
    #     print('线程启动异常')

while 1:
    pass
