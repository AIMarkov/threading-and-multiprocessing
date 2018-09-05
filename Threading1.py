import threading #文件名别与标识符重复了
import time
def thread_job():
    print("this is the current threading:",threading.current_thread(),"start")
    for i in range(10):
        time.sleep(0.1)
    print('T1 end')
def main():
    add_threading=threading.Thread(target=thread_job,name='T1')#添加一个线程
    add_threading.start()
    add_threading.join()
    print('finish')
if __name__==main():
    main()
#看输出顺序:
# this is the current threading: <Thread(T1, started 12548)> start
# finish
# T1 end
#多线程是同时执行
#如果要使得所有进程都结束再输出“finish”那么要用到join,输出顺序：
# this is the current threading: <Thread(T1, started 13236)> start
# T1 end
# finish
