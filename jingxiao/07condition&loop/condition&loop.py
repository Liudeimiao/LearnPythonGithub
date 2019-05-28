# y = |x|
x = 1
if x < 0:
    y = -x
else:
    y = x

print(y)

# if s: # s is a string
#     ...
# if l: # l is a list
#     ...
# if i: # i is an int
#     ...
# ...

# 列表的遍历
# l = [1, 2, 3, 4]
# for item in l:
#     print(item)

d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}


for k in d: # 遍历字典的键
    print(k)
# name
# dob
# gender
#
for v in d.values(): # 遍历字典的值
     print(v)
# jason
# 2000-01-01
# male
#
for k, v in d.items(): # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))
# key: name, value: jason
# key: dob, value: 2000-01-01
# key: gender, value: male


l = [10,2,3,4,5,6,7]

for index in  range(0,len(l)):
    if index<5:
        print(l[index])


for index ,item in enumerate(l):
    if index<5:
        print(index,item)



# while True:
#
#         text = input('Please enter your questions, enter "q" to exit')
#         if text == 'q':
#             print('Exit system')
#             break

# x = [1,-2,3]
# y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
# x = [1,-2,5]
# y = [2*value+5 if value>0 else -value*2+5 for value in x]
# print(y)

# text = 'today,  is,sunday'
#
# text_list = [s.strip() for s in text.split(',') if len(s.strip())>3]
#
# print(text_list)

# lx = [1,2,3]
# ly = [2,3,4]
#
# t = [(xx,yy) for xx in lx for yy in ly if xx !=yy]
#
# print(t)



attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

#zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
ld = [dict(zip(attributes,v)) for v in values]

print(ld)



a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
 # [(1, 4), (2, 5), (3, 6)]
zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

print([{attributes[i]:value[i] for i in range(len(attributes))} for value in values])