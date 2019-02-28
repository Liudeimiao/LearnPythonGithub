import  threading
from threading import  current_thread

class Mythread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')


class MyThread2(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('run')
        print(current_thread().getName(),'stop')



t1 = MyThread2()
t1.start()
t1.join()

print(current_thread().getName(),'end')
