#多线程设置的功能不能有返回值的，因此要把其计算的结果放在一个长的队列中
#python中的多线程受GIL（global interpret lock）的影响，不是真正的并行，而是在I/O时锁住当前线程，
# 而执行下一个线程，也就是它实际上是利用了当前线程输入输出的时间来执行其他线程，而非并行
#真正并行可以用多进程实现（multiprocessing）
import threading
import time
from queue import Queue
def job(I,q):
    for i in range(len(I)):
        I[i]=I[i]**2
    q.put(I)
def multithreading():
    q=Queue()
    threads=[]
    data=[[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
        t.join()
    results=[]
    for _ in range(4):
        results.append(q.get())#每次拿出一个，按顺序拿出来的
    print(results)
if __name__ == '__main__':
    multithreading()
