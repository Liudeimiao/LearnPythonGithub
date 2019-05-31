def my_func(message):
    print('Got a message: {}'.format(message))

# 调用函数 my_func()
my_func('Hello World')
# 输出
# Got a message: Hello World

# def find_largest(l):
#     if not isinstance(l,list):
#         print("param is not list")
#         return
#     if len(l)==0 :
#         print("param is empty")
#         return
#     largest = l[0]
#     for item in l:
#         if item > largest:
#             largest = item
#
#     return  largest
#
# largeInt = find_largest([4,3,8,2,10])
# print(largeInt)




# 输出
# largest
# element is: 8

# def my_sum(a, b):
#     return a + b
#
# result = my_sum(3, 5)
# print(result)
#
#
#
#
# print(my_sum([1, 2], [3, 4]))






# 求 一个正整数的阶乘
#

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
#         x = 'nonlocal'
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()
# 输出
# inner: nonlocal
# outer: nonlocal

#闭包的写法

# def nth_power(param):
#
#     def exponent_of(base):
#         return  base ** param
#
#     return exponent_of
#
# square = nth_power(2)
# square2 = nth_power(3)
# result = square(2)
# result2 = square2(3)
#
# print(result)
# print(result2)

def quickSort(arr):
    def partition(arr, left, right):
        pivot = arr[left]
        while left < right:
            while left < right and arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left] = arr[right]
            while left < right and arr[left] < pivot:
                left += 1
            if left < right:
                arr[right] = arr[left]
        arr[left] = pivot
        return left
    def innerQuickSort(arr, left, right):
        stack = []
        stack.append(left)
        stack.append(right)
        while len(stack) > 0:
            right = stack.pop()
            left = stack.pop()
            pivotIndex = partition(arr, left, right)
            if pivotIndex + 1 < right:
                stack.append(pivotIndex+1)
                stack.append(right)
            if left + 1 < pivotIndex:
                stack.append(left)
                stack.append(pivotIndex - 1)
    innerQuickSort(arr, 0, len(arr)-1)

arr = [394, 129, 11, 39, 28]
quickSort(arr)
print(arr)




















