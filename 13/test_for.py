# 从1 到 10  所有偶数的平方
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append( i*i )


print(alist)


# 列表推导式
blist = [i*i for i in range(1, 11) if(i % 2) == 0]
print(blist)



zodiac_name = {'a':1,'b':2}
for i in zodiac_name:
    zodiac_name[i] = 0

# 列表推导式
z_num = {i:0 for i in zodiac_name}

