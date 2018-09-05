import multiprocessing as mp
from queue import Queue
def job1(q):
    sum=0
    for i in range(10):
        sum+=i
    q.put(sum)
    print("11")
def job2(q):
    sum=0
    for i in range(30):
        sum+=i
    q.put(sum)
    print("22")
if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=job1,args=(q,))
    p2=mp.Process(target=job2,args=(q,))#一定要加逗号表示是可以迭代的
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    re1=q.get()
    re2=q.get()
    print(re1,re2)
