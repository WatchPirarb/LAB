import pymysql

con=pymysql.connect(host="localhost",user="root",passwd="202003",db="") #สร้างconnect
cs = con.cursor() #เป็นตัวใช้ทำงานต่างๆ เช่น insert update delete select ผ่าน cursor()
cs.execute("show databases")
sv = cs.fetchone() # นำข้อมูลจาก sql มาแสดงผล
print("%s"%sv)
con.close()
cs.close()