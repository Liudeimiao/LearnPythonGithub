x = 'abcd'
if x == 'abc' :
    print('x 的值和abc 相等')
elif(x =='abcd'):
    print('x和 abc不相等')


#todo 看不懂 下面的代码
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a','b']
}
print(mcase_frequency)