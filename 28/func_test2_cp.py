def count(First = 0):

    cnt = [First] # 定义列表

    def add(): # 里面的函数
        cnt[0]+=1 # 列表里第一个数 累加1
        return cnt[0]  #返回累加数

    return add  # 返回函数

num3 = count(3)  # 转换为变量

print(num3())  # 打印返回值



