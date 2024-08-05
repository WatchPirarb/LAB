sum =0
while True:
    num = int(input("num = "))
    if num ==0:
        break
    if num %3==0 and num%5==0:
        sum+=num
print(sum)
