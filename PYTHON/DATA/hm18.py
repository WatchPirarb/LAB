input= int(input())
a,b = 0,1 
for i in range(input+1):
    a,b =b,a+b
print(a)