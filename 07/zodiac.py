
#Python 元组 元组是另一个数据类型，类似于 List（列表）。
#元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (2, 15)

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，
# 返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
#
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# 过滤掉 小于等于（2,15） 的月份组.逻辑不懂 todo
zodiac_day = filter(lambda  x: x<=(month, day), zodiac_days)
print(zodiac_day)


zodac_len = len(list(zodiac_day)) % 12

print(len(list(zodiac_day)))
print(zodiac_name[zodac_len])



a_list = ['abc', 'xyz']
a_list.append('X')
print (a_list)
a_list.remove('xyz')
print(a_list)
# 不能 print（'a_list.remove('abc')'）-->none
a_list.remove('abc')
print(a_list)

#以下展示了使用 filter 函数的实例：
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。

#该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

#过滤出 奇数
def is_odd(n):
    return n % 2 == 1


tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)
