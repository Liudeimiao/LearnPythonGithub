# 日常应用比较广泛的模块是： 常用的标准库


# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__

#元字符
# . ^ $ * + ? {m} {m,n} [] |  \d \D \s ()
# .  点 ：匹配任意一个 字符。
# shift +6 ^   以什么样的结果 做开头。
# $ 以什么结尾  jpg$ 结尾。
# *   a*  星号前面a 出现了 0次或者多次。
#+ 加号前面出现 一次或者多次


# ^$  匹配空行
# .*? 匹配 贪婪模式。

import re

# group 从 1 开始，分组获取。 group() -->完整输出 2018-05-12
# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-05-12').group())
# 输出
# year,month,day  = p.match('2018-05-12').groups()
#
# print(year+month+day)


#p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print (p.match('aa2018-05-10bb').group(2) )
# print (p.match('2018-05-10').groups() )
#
# year, month, day = p.match('2018-05-10').groups()
# print(year)
#
# print (p.search('aa2018-05-10bb'))
# phone = '123-456-789 # 这是电话号码'
# p2 = re.sub(r'#.*$','',phone)
# print(p2)
# p3 = re.sub(r'\D','',p2)
# print(p3)
# findall()

# import  random
# print( random.randint(1,5))
# print( random.choice(['aa','bb','cc']))