import xlrd
import pymysql
import re
import time


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='12345678', db='sd_ues', charset='utf8mb4')
p = re.compile(r'\s')
#文件目录
data = xlrd.open_workbook('D:\\APN.xlsx')

#sheet1 4G  数据
table = data.sheets()[0]
t = table.col_values(1)
nrows = table.nrows

#sheet2 2/3G 数据
table2 = data.sheets()[1]
t = table.col_values(1)
nrows2 = table.nrows

# 获取当前时间#
updateTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# sheet1 数据封装
ops = []
for i in range(nrows):
    r1 = table.row_values(i)

    #ops.append((r1[2], p.sub('', r1[1]), p.sub('', r1[3]), p.sub('', r1[4]), r1[5], r1[6]))
    if r1[0]=='APNID':
        continue
    ops.append((1,r1[0], r1[1],"", r1[3],1,0,updateTime))

# sheet2 数据封装
ops2 = []
for i in range(nrows2):
    r1 = table2.row_values(i)

    if r1[0]=='APNID':
        continue
    ops2.append((2,r1[0], r1[1],"", r1[3],1,0,updateTime))


cur = conn.cursor()
cur.executemany('INSERT INTO `sd_ues`.`apn_aggregate` (`apnType`, `apnId`, `apnName`, `apnName2`, `cityName`, `userCounts`, `delete_flag`, `update_date`) '
                'VALUES (%s,%s,%s,%s,%s,%s,%s,%s);', ops)

#sheet2 数据
cur.executemany('INSERT INTO `sd_ues`.`apn_aggregate` (`apnType`, `apnId`, `apnName`, `apnName2`, `cityName`, `userCounts`, `delete_flag`, `update_date`) '
                'VALUES (%s,%s,%s,%s,%s,%s,%s,%s);', ops2)
conn.commit()
cur.close()

conn.close()