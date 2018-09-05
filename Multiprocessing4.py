#共享内存，使用全局变量是不能行
import multiprocessing as mp
value=mp.Value('i',1)#i表示整数,d表示double，f表示float,表示共享内存可以被所有进程读取,1是值
array=mp.Array('i',[1,2,3])#这个Array只能是列表，一维的，不能是多为数组，不同于numpy
print(array)