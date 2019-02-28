
# 装饰器 的 使用。。 就是 在在核心 代码搞 装饰，然后不要写在 核心代码里面。
#通过 @  类似注解的方式，将代码写在别处。
def new_tips(args):
    def tip(func):
        def nei(a,b):
            print("start %s  %s" %(args,func.__name__))
            func(a,b)
            print("stop")
        return nei  # return 要和 自身的def 对齐。。不然会报错 TypeError: 'NoneType' object is not callable
    return tip

@new_tips("add_module")
def add(a,b):
    print(a+b)

@new_tips("sub_module")
def sub(a,b):
    print(a-b)


add(3,3)

sub(5,3)