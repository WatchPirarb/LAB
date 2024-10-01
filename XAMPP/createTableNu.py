import pymysql

try:
    con = pymysql.connect(host="localhost",user="root",passwd="202003",db="Python_Tawin_1")
    cs = con.cursor()
    cs.execute("""CREATE TABLE student_NU(student_id INT(8)NOT NULL,
               f_name CHAR(25)COLLATE utf8_bin,
               l_name CHAR(25)COLLATE utf8_bin,
               major_name CHAR(25)COLLATE utf8_bin,
               PRIMARY KEY(student_id))""")
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง sql ไม่ถูกต้อง")
else:
    print("สร้างตารางสำเร็จแล้ว")
    con.close()
    cs.close()