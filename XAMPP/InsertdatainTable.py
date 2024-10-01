import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",passwd="202003",db="Python_Tawin_1",charset="utf8")
    cs = con.cursor()
    cs.execute("""INSERT INTO student_NU(student_id,f_name,l_name,major_name)
               VALUES(66310700,"นายสตีฟ","เรนเอด","วิทยาการคอมพิวเตอร์")""")
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