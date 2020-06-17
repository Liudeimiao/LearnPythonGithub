import xlrd
import pymysql
import re
import time
import logging
import traceback
import os
def exportData():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)s[%(lineno)d] - %(levelname)s：%(message)s',
                        filename=os.path.join(os.getcwd(), 'inputAPNdata.log'))
    logger = logging.getLogger()

    #连接数据库信息
    try:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                               passwd='12345678', db='sd_ues', charset='utf8mb4')
        p = re.compile(r'\s')
        logger.info('数据库连接成功')
    except:
        logger.debug(traceback.format_exc())

        # 打开文件，获取excel文件的workbook（工作簿）对象
    filename = input('请输入xlsx文件路径及文件名：')
    # 文件目录
    data = xlrd.open_workbook(filename,encoding_override="utf-8")


    # 获取当前时间
    updateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 连接游标
    cur = conn.cursor()

    # 多个sheet
    sheets = data.sheets()

    #导入计数
    countLine = 0;
    for i in range(len(sheets)):
        table = sheets[i]
        nrows = table.nrows

        # sheet1 数据封装
        sheetName = data.sheet_names()[i]
        if('4G' in sheetName):
            apnType = 1
        if('23g' in sheetName):
            apnType = 2

        ops = []

        countLine += (nrows-1)
        for i in range(nrows):
            #从第二行开始
            if i !=0:
                r1 = table.row_values(i)
                ops.append((int(apnType), r1[0], r1[1], "", r1[3], 1, 0, updateTime))
        #导入行数

        # 批量插入
        insert_sql =  'INSERT INTO `sd_ues`.`apn_aggregate` (`apnType`, `apnId`, `apnName`, `apnName2`, `cityName`, `userCounts`, `delete_flag`, `update_date`) ' \
               'VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'

        try:
            cur.executemany(
                insert_sql, ops)
        except:
            logger.debug('插入数据出现问题', insert_sql)
            logger.debug(traceback.format_exc())


    conn.commit()
    logger.info('导入数据成功，共：'+str(countLine)+' 条')
    cur.close()
    conn.close()


exportData()