w = input().split()
real_w = list(map(float,w))

groupA = 0
groupB = 0
groupC = 0

for i in real_w:
    if i <10:
        groupA +=1
    elif 10<= i <=20:
        groupB +=1
    else:
        groupC +=1
print(groupA,groupB,groupC)