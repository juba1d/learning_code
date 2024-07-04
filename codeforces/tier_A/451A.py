n, m = map(int, input().split())

min_sticks = min(n, m)

if min_sticks % 2 == 0:
    print("Malvika")
else:
    print("Akshat")