from functools import reduce

square = lambda  x:x ** 3

result  = square(3)

print(result)


def square(x):
    return x ** 2

print(square(3))




la = [(lambda x :x*x)(x) for x in range(5)]
# 输出
print(la)


ls =[(1,3),(4,1),(8,-2)]

ls.sort(key= lambda x:x[1])

print(ls)

#map() 会根据提供的函数对指定序列做映射。

#第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
square1 = map(lambda x:x*x,[1,2,3])

print(list(square1))

def square2(x):
    return x*x

square2 = map(square2,[1,2,3])

print(list(square2))

# from tkinter import Button, mainloop
# button = Button(
#     text='This is a button',
#     command=lambda: print('being pressed')) # 点击时调用 lambda 函数
# button.pack()
# mainloop()

lt = [1,2,3,4,5]

new_lt = filter(lambda x:x%2==0,lt)

print(list(new_lt))

lr = [1,2,3,4,5]

from functools import reduce  # py3
new_lr = reduce(lambda  x,y:x*y,lr)

print(new_lr)

d = {'mike': 10, 'lucy': 2, 'ben': 30}

ds = sorted(d.items(),key= lambda  x:x[1],reverse=True)

print(ds)