
n, m = map(int, input().split())


a = []


for i in range(n):
    row = list(input().strip())
    a.append(row)

x = y = 0


for i in range(n):
    cnt = 0
    for j in range(m):
        if a[i][j] == '*':
            cnt += 1
    if cnt == 1:
        x = i
        break


for j in range(m):
    cnt = 0
    for i in range(n):
        if a[i][j] == '*':
            cnt += 1
    if cnt == 1:
        y = j
        break


print(x + 1, y + 1)
