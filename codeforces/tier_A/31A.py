n = int(input())
lengths = list(map(int, input().split()))

found = False
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                if lengths[i] == lengths[j] + lengths[k]:
                    print(i + 1, j + 1, k + 1)  # Output 1-based indices
                    found = True
                    break
        if found:
            break
    if found:
        break

if not found:
    print(-1)
