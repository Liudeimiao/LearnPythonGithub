#python 线程 生产者 和消费者 demo

from threading import Thread,current_thread
import  time
import random
from queue import Queue

queue = Queue(5) # 定义队列 为 5 个空间

class ProducerThread(Thread):# 定义生产者线程
    def run(self):
        nums = range(100)
        name = current_thread().getName()
        global queue

        while True:
            num = random.choice(nums);
            queue.put(num)

            print('生产者 %s 生产数据 %s' % (name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 休眠 %s 秒' %(name,t))



class CustomerThread(Thread):
    def run(self):
        global queue
        name = current_thread().getName()

        while True:
            num = queue.get()
            queue.task_done()

            print('消费者 %s 消费数据 %s' %(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('消费者 %s 休眠 %s 秒' %(name,t))



p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p3 = ProducerThread(name='p3')

c1 = CustomerThread(name='c1')
c1.start()
c2 = CustomerThread(name='c2')
c3= CustomerThread(name='c3')

