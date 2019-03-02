# print('abc',end='\n')
# print('abc')
#

# 关键字函数 类似java 的重载。可变长参数。
# def func (a, b, c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
#
# func(1, c=3)



# # 取得参数的个数
# def  howlong(first, *other):
#     print( 1 + len(other))
#
# howlong()

#
# var1 = 123
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
# #
# #
# #
# func()
# print(var1)

# iter() next()

# list1 =[1, 2, 3]
# it = iter(list1)
# print( next(it))
# print( next(it))
# print( next(it))
# print( next(it)) # except
# #
#
#

#每次取出一个数，自己去加2
# for i in range(10,20,2):
#     print(i)


#yield  生成器，带 yield 的生成器。
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
#
# for i in frange(10,20,0.5):
#     print(i)



# #
# #
# #
# #
# #
def true():return True
lambda : True

# print(true())
# #
# #
# # >>> def add(x,y):
# # ...     return x+y
# # ...
# #
# # >>> def add(x,y): return x+y
# # lambda  x,y: x+y
# x = 1
# y = 2
# print(lambda x,y:x+y)
# #
# #
# # >>> add(3,5)
# # 8
# # >>>
#
#
#
# # lambda  x:x<= (month, day)
# #
# # def func1(x):
# #     return  x<= (month, day)
# #
# #
# #
# lambda  item:item[1]
#
# def func2(item):
#         return item[1]
#
# adic = {'a':'aa','b':"bb",'c':'cc'}



# pyhton 内置函数。
# # filter() map() reduce() zip()
# #
#



# a=[1,2,3,4,5,6,7]
# #强制转换 list
# list = list(filter(lambda x:x>2 , a))
#
# print(list)
# >>> help(filter)
#
# >>> a=[1,2,3,4,5,6,7]
# >>> list(filter(lambda x:x>2 , a))
# [3, 4, 5, 6, 7]
# >>> help(map)
#

# map() 对参数 依次处理。
a=[1,2,3]
b=[3,2,1]
list2 =  list(map(lambda x,y:x+y ,a,b))
print(list2)

# <map object at 0x105686e10>
# >>> list(map(lambda x:x ,a))
# [1, 2, 3]
# >>> list(map(lambda x:x+1 ,a))
# [2, 3, 4]
# >>> b=[4,5,6]
# >>> list(map(lambda x,y:x+y ,a,b))
# [5, 7, 9]
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> [1, 2, 3]
# [1, 2, 3]
# >>> [4, 5, 6]
# [4, 5, 6]
# >>> help(reduce)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'reduce' is not defined
# >>> from functools import reduce
#
#
# >>> from functools import reduce
# >>> reduce(lambda x,y: x+y ,[2,3,4],1 )
# 10
# >>> ((1+2)+3)+4
#
# >>> for i in zip((1,2,3),(4,5,6)):
# ...     print(i)
# ...
# (1, 4)
# (2, 5)
# (3, 6)

# reduce() 函数会对参数序列中元素进行累积。
#函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

from functools import reduce

def add(x,y):
    return x + y

print (reduce(lambda x,y:x+y, range(1, 101)))




























# def func():
#    a = 1
#    b = 2
#    return a+b
#
#
# def sum(a):
#     def add(b):
#       return  a+b
#
#     return add
#
# # add 函数名称或函数的引用
# # add() 函数的调用
#
# num1 =  func()
#
# num2 =  sum(2)
# print( num2(4))
#
# #
# # print(type(num1))
# # print(type(num2))
# #
#
# count()
#







