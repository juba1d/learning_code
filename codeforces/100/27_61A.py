a = input().strip()
b = input().strip()

for i in range(len(a)):
    print(1 if a[i] != b[i] else 0, end='')
print()
