from typing import Set

d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
d1 == d2 == d3 ==d4

d5 = {'name':'liu','age':30,'gender':'male'} # 字典的创建
d6 = dict({'name':'liu','age':30,'gender':'male'}) #函数 创建
d7 = dict([('name','liu'),('age',30),('gender','male')]) # 函数将列表里面的元组->转为字典
d8 = dict(name='jason',age=20,gender='male')# 将元组转为字典
print(d8)


print(d1 == d2 == d3 ==d4)
# True

s1 = {1, 2, 3}
s2 = set([1, 2, 3]) #用 小写的set() 方法
s1 == s2
print(s1 == s2)

s3 = {4,5,6}
s4 = set([4,5,6,4]);# 用函数set() 将列表转为set
print(s4)
s3==s4
print(s3==s4)
#True


d = {'name': 'jason', 'age': 20}
d['name']
print(d['name'])
#d['location']

#print(d.get('name'))
print(d.get('name','null'))


s = {1, 2, 3}
1 in s
print(1 in s)
10 in s
print(10 in s)


d = {'name': 'jason', 'age': 20}
'name' in d
print('name' in d)

print('location' in  d)

print(20 in d)


d = {'name': 'jason', 'age': 20}
d['gender'] = 'male' # 增加元素对'gender': 'male'
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
d
{'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d['dob'] = '1998-01-01' # 更新键'dob'对应的值
d.pop('dob') # 删除键为'dob'的元素对
'1998-01-01'
d
{'name': 'jason', 'age': 20, 'gender': 'male'}

s = {1, 2, 3}
s.add(4) # 增加元素 4 到集合
s
{1, 2, 3, 4}
s.remove(4) # 从集合中删除元素 4
s
{1, 2, 3}



d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
d_sorted_by_key
[('a', 2), ('b', 1), ('c', 10)]
d_sorted_by_value
[('b', 1), ('a', 2), ('c', 10)]


di = {'a':3,'b':2,'c':10}

d_sort1 = sorted(di.items(),key=lambda  x :x[0])#根据字典键的升序排序
d_sort2 = sorted(di.items(),key=lambda  x: x[1])#根据字典值的升序排序
print(d_sort2) # [('b', 2), ('a', 3), ('c', 10)]


def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None


products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]


print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))

def find_other_product_price(products,product_id):
    for id, price in products: # 遍历列表，拿到id和price
        if id == product_id:#判断列表中id和price
            return price

    return None # 返回值 要找到位置，跳出for 循环。


print("432314553 的商品价格为{}".format(find_other_product_price(products,432314553)))


def find_unique_price(products):
    unique_price = []
    for _,price in products:
        if products not  in unique_price:
            unique_price.append(price)

    return len(unique_price)



#print(find_unique_price(products))


def find_unque_set(products):
    unique_set = set()
    for _,price in products:
        unique_set.add(price)

    return len(unique_set)

print(find_unque_set(products))
# 输出


import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

# 计算列表版本的时间
start_using_list = time.perf_counter()
#find_unique_price(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
## 输出
#time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
#find_unque_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
#time elapse using set: 0.008238077163696289

test = [(1,3),(2,6)]
test2 = list(test);
print(test2)