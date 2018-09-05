#进程池，也就是把所有进程放在一个池子里,用了pool后可以由return
import multiprocessing as mp

def job(x):
    return x*x
def multicore():
    pool=mp.Pool(processes=8)#默认是包含所有核，也可以指定
    res=pool.map(job,range(10))#可以多个输入，自动分配进程
    print(res)
    res=pool.apply_async(job,(2,))#这个也是类似于map功能，这里只能传入一个值只会用一个核，但是要加“，”表示可迭代，
    print(res.get())
    #多个输入
    multi_res=[pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res])
if __name__=='__main__':
    multicore()