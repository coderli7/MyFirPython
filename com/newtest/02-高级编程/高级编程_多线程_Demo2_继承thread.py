# 继承的方式，实现多线程

import threading
import time

exitFlag = 0


class myThread(threading.Thread):

    def __init__(self, threadIdParam, nameParam, counterParam):
        threading.Thread.__init__(self)
        self.name = nameParam
        self.threadID = threadIdParam
        self.counter = counterParam

    def print_test(self, delay, counter):
        while counter:
            if exitFlag:
                self.exit()
            time.sleep(int(delay))
            print("%s: %s" % (self, time.ctime(time.time())))
            counter -= 1

    def run(self):
        print('开始线程:' + self.name)
        self.print_test(self.counter, 5)
        print('结束线程' + self.name)


if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 2)

    # print(thread1.name)
    # print(thread1.counter)
    # print(thread1.threadID)

    thread2 = myThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("退出主线程")
