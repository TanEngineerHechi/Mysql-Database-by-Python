import Mysql_ExportExcelbook as MysqlClass

conn = MysqlClass.connect(
    'localhost',
    3306,
    'username',
    'password',
    'database name',
    'utf8'
)
