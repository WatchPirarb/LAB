import math as m
a = int(input())
b = int(input())
c = int(input())
crad = m.radians(c)
ans = a**2+b**2-2*a*b*m.cos(crad)
answ = m.sqrt(ans)
print(answ,"cm.")
