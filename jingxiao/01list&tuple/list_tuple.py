
#列表和元组
#
l = [1, 2, 3, 4]
l[3] = 40  # 和很多语言类似，python 中索引同样从 0 开始，l[3] 表示访问列表的第四个元素
print(l)
[1, 2, 3, 40]

#模仿
list_01 = [5,6,7,8]

list_01[3] = 50
print(list_01)


tup = (1, 2, 3, 4)
new_tup = tup + (5, ) # 创建新的元组 new_tup，并依次填充原元组的值
print(new_tup[-1])
(1, 2, 3, 4, 5)

l = [1, 2, 3, 4]
l.append(5) # 添加元素 5 到原列表的末尾
l
[1, 2, 3, 4, 5]

##切片操作
list_01 = [1, 2, 3, 4]
l[1:3] # 返回列表中索引从 1 到 2 的子列表
print(list_01[1:3])

tup = (1, 2, 3, 4)
tup[1:3] # 返回元组中索引从 1 到 2 的子元组
print(tup[1:3])


#随意嵌套
l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表
print(l)
tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一元组
print(tup)


#  3.4 列表和元组可以通过 list_01（） 和 tuple（） 互相转换
# 如果list_01变量和list_01函数重名  TypeError: 'list_01' object is not callable

list((1,2,3))
print(list((1, 2, 3)))

#tuple([1, 2, 3])
#print(tuple([1, 2, 3]))


#常用内置函数
l = [3, 2, 3, 7, 8, 1]
print(l.count(3))  #  # count（item） 表示：统计列表/元组中 item 出现的次数

t = ("L",7,"L",77);
print(t.count("L"))

print(l.index(7)) # index(item) 表示：返回列表/元组 中 item 第一次出现的索引


# 2
# l.index(7)
# 3
l.reverse() #  原地反转列表
print(l)
l.sort()# 排序列表
print(l)
# l
# [1, 8, 7, 3, 2, 3]
# l.sort()
# l
# [1, 2, 3, 3, 7, 8]
#
tup1 = (3, 2, 3, 7, 8, 1)
# tup.count(3)
# 2
# tup.index(7)
# 3
tup2 = reversed(tup1) #  reversed() 和sorted() 都能对元组和列表进行反转和排序。但是会生成一个新的元组和列表
print(list(tup2))
# [1, 8, 7, 3, 2, 3]
tup4 = sorted(tup1) #
print(tup4)
# [1, 2, 3, 3, 7, 8]


