import threading

from threading import current_thread

class MyThread(threading.Thread): # 类似java 继承。
    def run(self):
        print(self.getName(),'start')
        print('run')
        print(self.getName(),'stop')


for i in  range(1,6,1):
    t1 = MyThread()
    t1.start()
    t1.join()
