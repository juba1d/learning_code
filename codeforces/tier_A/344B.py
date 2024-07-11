a, b, c = map(int, input().split())

x = y = z = 0

found = False

for i in range(max(a, b, c) + 1):
    for j in range(max(a, b, c) + 1):
        for k in range(max(a, b, c) + 1):
            if i + j == b and j + k == c and k + i == a:
                x = i
                y = j
                z = k
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print(x, y, z)
else:
    print("Impossible")
