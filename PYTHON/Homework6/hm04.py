n = int(input("จำนวน = "))
num = []
count = 0
i=0

while i <n:
    l = int(input("ตัวเลข = "))
    num.append(l)
    if l <0:
        count+=1
    i+=1
    
max_num = max(num)
min_num = min(num)
diff = max_num - min_num


print("ผลต่าง =",diff)
print("จำนวนเลขลบ =",count)

