#注意一定在if __name__=='__main__'运行否则会报错
import multiprocessing as mp
def job(a,b):
    print("aaa")
if __name__=='__main__':
    pl=mp.Process(target=job,args=(1,2))
    pl.start()