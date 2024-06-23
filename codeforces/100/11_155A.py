n=int(input())

x=list(map(int,input().split()))

min_val = max_val = ans = 0

for i in range(n):
    a = int(x[i])
    if i == 0:
        min_val = max_val = a
    if a > max_val:
        ans += 1
        max_val = a
    if a < min_val:
        ans += 1
        min_val = a

print(ans)

