import threading

localThread=threading.local()

def thread_fun(param):
    localThread.arg=param
    print(threading.current_thread().name,localThread.arg)


th1=threading.Thread(target=thread_fun,args=('Lucy',))
th2=threading.Thread(target=thread_fun,args=('Jack',))
th3=threading.Thread(target=thread_fun,args=('Lily',))

th1.start()
th2.start()
th3.start()
# th1.join()
# th2.join()