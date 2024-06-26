n = int(input())
lst = list(map(int, input().split()))

minValue = abs(lst[0] - lst[1])
indices = [1, 2]

for i in range(n):
    if minValue > abs(lst[i] - lst[(i + 1) % n]):
        indices[0] = i + 1
        indices[1] = (i + 1) % n + 1
        minValue = abs(lst[i] - lst[(i + 1) % n])

print(indices[0], indices[1])

