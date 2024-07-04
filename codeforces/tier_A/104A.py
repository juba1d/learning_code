x = int(input())

if x <= 10:
    print(0)
elif x > 21:
    print(0)
else:
    x -= 10
    if x == 10:
        print(15)
    else:
        print(4)
