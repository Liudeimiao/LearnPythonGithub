# a*x +b = y 使用闭包的写法

# def a_line(a,b): # 定义不变的值 a,b
#
#     def add(x,z): # 闭包函数 x z
#         return a*x + b -z #方程式子
#
#     return add #返回函数。
#
# num1 = a_line(3,5)
#
# y = num1(10,35)
#
# print(y)

# lambda 表达式
def b_line(a,b):
    return lambda x:x*a+b

    return add

z = b_line(3,5)

print(z(10))