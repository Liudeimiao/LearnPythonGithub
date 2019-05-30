# if name is not None
#     print(name)

# try:
#     s = input('please enter two numbers separated by comma: ')
#     num1 = int(s.split(',')[0].strip())
#     num2 = int(s.split(',')[1].strip())
#     ... # 省略的意思
# except (ValueError,IndexError) as err:
#     print('Value Error: {}'.format(err))
#
# print('continue')
# ...

# import sys
# try:
#     f = open('file.txt', 'r')
#     ... # some data processing
# except OSError as err:
#     print('OS error: {}'.format(err))
# except:
#     print('Unexpected error:', sys.exc_info()[0])
# finally:
#     f.close()


# class MyInputError(Exception):
#     """Exception raised when there're errors in input"""
#
#     def __init__(self, value):  # 自定义异常类型的初始化
#         self.value = value
#
#     def __str__(self):  # 自定义异常类型的 string 表达形式
#         return ("{} is invalid input".format(repr(self.value))) #repr() 函数将对象转化为供解释器读取的形式。
#
#
# try:
#     raise MyInputError(1)  # 抛出 MyInputError 这个异常
# except MyInputError as err:
#     print('error: {}'.format(err))

class MyInputError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise  MyInputError(1)
except MyInputError as err:
    print('error:{}'.format(err))







