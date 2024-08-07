sum =0
while True:
    num = int(input("ป้อน 0 เพื่อหยุดการทำงาน = "))
    
    if num == 0:
        break
    
    if num % 3 == 0 and num % 2 == 0:
        sum+=num

print("ผลรวมของเลข ที่หาร 2 และ 3 ลงตัว =",sum)