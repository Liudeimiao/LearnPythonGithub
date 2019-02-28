from threading import  Thread,current_thread
import  time
import random
from queue import Queue

queue = Queue(5) # 队列

class ProducerThread(Thread):  # 生产者 线程
    def run(self):
        name = current_thread().getName()  # 当前线程名字
        nums = range(100) # 0 到100  范围函数
        global queue  # global关键字(内部作用域想要对外部作用域的变量进行修改)

        while True:  # while 循环
            num = random.choice(nums)  # 随机选数
            queue.put(num)      # 放进队列

            print('生产者 %s 生产了 %s ' %(name,num))
            t = random.randint(1,3) # 随机选数
            time.sleep(t)  # 休眠
            print('生产者 %s 休眠了 %s 秒' %(name,t))



class CustomerThread(Thread):  # 消费者 线程
    def run(self):
        name = current_thread().getName() # 当前线程名字
        global  queue    # global关键字(内部作用域想要对外部作用域的变量进行修改)

        while True:
            num =  queue.get() # 获取队列的值
            queue.task_done() # 表明以前排队的任务(示例：使用一个url爬取网页内容完成)已完成。装好了 线程等待。

            print('消费者 %s 消费数据 %s' %(name,num))
            t = random.randint(1,3) # 随机取值
            time.sleep(t) #休眠
            print('消费者 %s 休眠了 %s 秒' %(name,t)) # 打印



p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p3 = ProducerThread(name='p3')

c1 = CustomerThread(name='c1')
c1.start()
c2 = CustomerThread(name='c2')
c3= CustomerThread(name='c3')


