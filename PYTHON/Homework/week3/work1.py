numbers = list(map(int, input().split()))
minnum = min(numbers)
maxnum = max(numbers)
all = sum(numbers)-minnum-maxnum
print(all)