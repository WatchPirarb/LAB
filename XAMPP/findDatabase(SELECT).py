import pymysql

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