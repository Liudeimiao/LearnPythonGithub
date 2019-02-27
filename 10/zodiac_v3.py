
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
#
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。 跟 java 的map 差不多。


cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0




while True:

    # 用户输入出生年份月份和日期
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    day = int(input('请输入日期:'))


    n = 0
    while zodiac_days[n] < (month,day):
        if month == 12 and day >23:
            break
        n += 1
    # 输出生肖和星座
    print('你的星座是：%s' % zodiac_name[n])
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    # 给value 赋值。当有自己的生肖 就+1
    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    # 输出生肖和星座的统计信息
    for  each_key in  cz_num.keys():
        print('生肖 %s 有 %d 个'%(each_key,cz_num[each_key]))

    for  each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key,z_num[each_key]))


