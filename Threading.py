import threading #文件名别与标识符重复了
def thread_job():
    print("this is the current threading:",threading.current_thread())
def main():
    add_threading=threading.Thread(target=thread_job)#添加一个线程
    add_threading.start()
    print(threading.active_count())#激活进程数
    print(threading.enumerate())#激活的进程
    print(threading.current_thread())#当前进程
if __name__==main():
    main()