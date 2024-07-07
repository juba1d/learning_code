n,m=map(int, input().split())

flag=[]

for _ in range(n):
    flag.append(list(map(int, input().strip())))

valid = True
for i in range(n):
    if len(set(flag[i])) != 1:
        valid = False
        break
    if i > 0 and flag[i][0] == flag[i - 1][0]:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")