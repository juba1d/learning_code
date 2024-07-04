n, t = map(int, input().split())
z = input()
s = []
for i in range(n):
    s.append(z[i])
j = 0
for i in range(t):
    while j < n - 1:
        if s[j] == 'B' and s[j + 1] == 'G':
            s[j], s[j + 1] = s[j + 1], s[j]
            j += 1
        j += 1
    j = 0
print(''.join(s))