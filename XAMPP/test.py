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
    

try:
    con = pymysql.connect(host="localhost",user="root",passwd="202003",db="Python_Tawin_1",charset="utf8")
    cs = con.cursor()
    cs.execute("""INSERT INTO student_NU(student_id,f_name,l_name,major_name)
               VALUES(66310721,"นายจอห์นนี่","สตาฟฟอร์ด","วิทยาการคอมพิวเตอร์")""")
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง sql ไม่ถูกต้อง")
    con.rollback()
else:
    con.commit()
    print("[บันทึกข้อมูลเรียบร้อยแล้ว]")
    con.close()
    cs.close()
    
try:
    con = pymysql.connect(host="localhost",user="root",passwd="202003",db="Python_Tawin_1",charset="utf8")
    cs = con.cursor()
    cs.execute("SELECT * FROM student_NU")  #ดึงข้อมูล
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้")
except pymysql.err.ProgrammingError:
    print("คำสั่ง sql ไม่ถูกต้อง")
else:
    data = cs.fetchall()  #ดึงข้อมูลเพื่อแสดงผล
    for i in data:
        print(i)
    # ปิดการเชื่อมต่อ
    con.close()
    cs.close()