import pymysql

try:
    con = pymysql.connect(host="localhost",user="root",passwd="202003",)
    cs = con.cursor()
    cs.execute("CREATE DATABASE Python_Tawin_1")
except pymysql.err.OperaionalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง sql ไม่ถูกต้อง")
else:
    print("สร้างฐานข้อมูลเสร็จแล้ว")
    con.close()
    cs.close()