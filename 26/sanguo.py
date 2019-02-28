
# # 读取人物名称
# f = open('name.txt',encoding='UTF-8')
# data = f.read()
# data0 = data.split('|')
#
# print(data0)
#
# # 读取兵器名称  每个奇数行，去掉 \n 换行操作。
# # strip() Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#
# f2 = open('weapon.txt',encoding="UTF-8")
# # data2 = f2.read()
# i = 1
# for  line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1
#
# # 读取 三国  替换掉换行符、转为 1行
# f3 = open('sanguo.txt',encoding='GB18030')
# print(f3.read().replace('\n',''))



def func(filename):
    print(open(filename,encoding="UTF-8").read())
    print('test func')



func('name.txt')

def funcRead(filename):
    print(open(filename,encoding="UTF-8").read())
    print('test funcRead')

funcRead("name.txt")