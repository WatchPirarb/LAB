import math as m
a = float(input())
b = float(input())
c = float(input())
crad = m.radians(c)
a_rea = 0.5*a*b*m.sin(crad)
print("area =",a_rea,"(sq cm)")