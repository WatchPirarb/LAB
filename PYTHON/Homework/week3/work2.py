chest_size = int(input())

if chest_size >= 46:
    print("XL")
elif chest_size >= 43:
    print("L")
elif chest_size >= 41:
    print("M")
elif chest_size >= 37:
    print("S")
else:
    print("XS")