salary =  float(input("รายได้ = "))
if salary >35000:
    print((salary*0.1)*12)
elif salary >25000:
    print((salary*0.75)*12)
elif salary >15000:
    print((salary*0.55)*12)
else:
    print((salary*0.3)*12)