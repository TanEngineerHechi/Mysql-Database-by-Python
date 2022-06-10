import pandas as pd
import pymysql
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'sheet01'

# 创建链接，获得链接对象
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1234',
    db='xxxx',
    charset='utf8'
)

try:
    # 2. 获取游标对象
    # cursor = conn.cursor()
    # with as 上下文语法，结束后自动close
    with conn.cursor() as cursor:
        sql ="select * from xxxx.xxxx limit 3"
        # 3. 通过游标对象向数据库发送SQL语句
        cursor.execute(sql)
        # fetchone:获取一行；fetchall:获取全部；fetchmany:获取多行
        row = cursor.fetchone()
        for data in result:
            print(data)
        if affected_rows >=1:
            print("DB connection success")

except pymysql.MySQLError as err:
    print(type(err), err)

# 6. 总是执行
finally:
    # 7.0 最终要关闭链接：
    conn.close()