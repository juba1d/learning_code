inputs = []

for _ in range(5):
    inputs.append(int(input()))

k, l, m, n, d = inputs

damaged_dragons = 0

for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        damaged_dragons += 1

print(damaged_dragons)