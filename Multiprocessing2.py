import multiprocessing as mp
import threading as th
from queue import Queue
import time
def job1(q):
    sum=0
    for i in range(1000):
        sum+=i
    q.put(sum)
    print("11")
def job2(q):
    sum=0
    for i in range(1000):
        sum+=i
    q.put(sum)
    print("22")
def multiP():
    q = mp.Queue()
    p1 = mp.Process(target=job1, args=(q,))
    p2 = mp.Process(target=job2, args=(q,))  # 一定要加逗号表示是可以迭代的
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    re1 = q.get()
    re2 = q.get()
    print(re1+re2)
def multiTh():
    q = Queue()
    q1 = th.Thread(target=job1, args=(q,))
    q2 = th.Thread(target=job2, args=(q,))  # 一定要加逗号表示是可以迭代的
    q1.start()
    q2.start()
    q1.join()
    q2.join()
    re1 = q.get()
    re2 = q.get()
    print(re1+re2)
def nomal():
    sum = 0
    for j in range(2):
        for i in range(1000):
            sum+=i
    print('sum:',sum)
if __name__=='__main__':
    a=time.time()
    nomal()
    b=time.time()
    print('nomal_T:',b-a)

    a = time.time()
    multiP()
    b = time.time()
    print('mutiP_T:', b - a)

    c = time.time()
    multiTh()
    d = time.time()
    print('mutiTh_T:', b - a)

