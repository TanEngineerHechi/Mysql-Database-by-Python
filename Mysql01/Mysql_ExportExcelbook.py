import pandas as pd
import pymysql
import openpyxl


# 创建链接，获得链接对象
def connect(host, port, user, password, db, charset):
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset
    )
    return connection


def select_sql(connection):
    try:
        conn = connection
        df0 = pd.read_sql("""show tables""", conn)
        print(df0)
        tableIndexNum = df0.index.values.max()
        i = 0
        a = []
        while i <= tableIndexNum:
            a += [df0.iat[i, 0]]  # 定义数组a=[]
            i += 1
        print(a)
        i = 0
        # with as 上下文语法，结束后自动close
        with pd.ExcelWriter('database.xlsx') as writer:
            while i <= tableIndexNum:
                sql1 = "select * from %s limit 3" % a[i]
                df1 = pd.read_sql(sql1, conn)
                print(df1)
                df1.to_excel(writer, sheet_name=a[i])
                i += 1


    except Exception as err:
        print(type(err), err)

    # 6. 总是执行
    finally:
        # 7.0 最终要关闭链接：
        conn.close()
