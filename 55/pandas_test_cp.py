from pandas import Series, DataFrame
import pandas as pd


#pandas 数据的预处理

# Series 一维数组 pandas 运算 。自动添加索引。 0-4。 索引可以重复
# obj = Series([4, 5, 6, -7])
#
# print(obj)
# print(obj.index)
# print(obj.values)

# obj2 = Series([4,5,6,-7],index=['a','b','c','d'])
#
# print(obj2)
#
# obj2['c'] = 10
# print(obj2)
#
# print ('f' in obj2)

# sdata = {
#     'beijing': 35000,
#     'shanghai': 71000,
#     'guangzhou': 16000,
#     'shenzhen': 5000}
# obj3 = Series(sdata)
# print( obj3)
#
# obj3.index = ['bj', 'gz', 'sh', 'sz']
# #
# print( obj3)


# DataFrame 操作更高的数组


data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

# print(frame2)

#增加新的列
#print(frame2['city'])
frame2['new'] = 100

#print(frame2)

# 根据条件 增加新的列
frame2['cap'] = frame2['city'] == 'beijing'

#print(frame2)

# 字典嵌套
pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }

frame3 = DataFrame(pop)
#print(frame3.T) # 行和列的转换

# 重新 索引的排序
obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])

obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

#print(obj5)

# method 空值的 填充 bfill（后） ffill（前）
obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

#print( obj6.reindex(range(6),method='bfill'))

#


# 删掉缺失值
from  numpy import nan as  NA

data = Series([1, NA, 2])
#print(data.dropna())

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]
                  ])
data2[4] = NA
# print(data2)
#
# print(data2.dropna(axis=1, how='all'))

data2.fillna(0) # 所有 为na 的 填充为 0
#print(data2.fillna(0))

#缺失值替换
#print(data2.fillna('ggg', inplace=True))
#print(data2)


#层级化索引
import numpy as np

data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

# 转换为二维 数组
print( data3.unstack() )
# 再转换回来 一维数组
print(data3.unstack().stack())


# 输出多个索引
#print ( data3['b':'c'])


