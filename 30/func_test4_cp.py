import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间： %s 秒" %(stop_time-start_time))
    return  wrapper # 这里是装饰器名字 ， mark 如果用 wrapper() 会 报错。TypeError: 'NoneType' object is not callable


@timmer
def i_can_sleep():
    time.sleep(3)

i_can_sleep()

