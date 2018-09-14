#进程池，也就是把所有进程放在一个池子里,用了pool后可以由return
#在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。
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
