import  threading
import time
from threading import current_thread


def MyThread(arg1,arg2):
    print(current_thread().getName(),'start')
    print('%s  %s ' %(arg1,arg2))
    print(current_thread().getName(),'stop')

for i in range(1,6,1):
    t1 = threading.Thread(target=MyThread,args=(i,i+1)) # 线程
    t1.start()  # 线程启动
