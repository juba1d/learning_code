n = int(input())

l, r = 1, n
ans = r

while l <= r:
    c = l + (r - l) // 2
    if c * (c + 1) // 2 >= n:
        ans = c
        r = c - 1
    else:
        l = c + 1

if ans * (ans + 1) // 2 == n:
    print("YES")
else:
    print("NO")
