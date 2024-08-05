year_month = input()
m,y = map(int, year_month.split())
inyear = y-543
leap_year = (inyear % 4 == 0 and inyear % 100 != 0) or(inyear % 400 ==0)
month = [31, 28, 31, 30, 31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
if leap_year:
    month[1] =29
days = month[m-1]
print(days)
