n = int(input())
a = (n * n) // 2

for i in range(1, a + 1):
    j = n * n - i + 1
    print(i, j)
