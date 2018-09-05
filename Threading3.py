#当希望用第一个线程的结果作为第二个线程的输入时，要用到lock
import threading
import time
def job1():
    global A
    for i in range(10):
        A+=1
        print('job1:',A)
def job2():
    global A
    for i in range(10):
        A+=10
        print('job2:',A)
if __name__=='__main__':
    #定义一个共享内存（全局变量）
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
