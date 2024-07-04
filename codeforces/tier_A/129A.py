n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
c = 0

for i in range(n):
    if (sum_a - a[i]) % 2 == 0:
        c += 1

print(c)
