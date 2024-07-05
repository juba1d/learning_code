n = int(input())
fingers = list(map(int, input().split()))

total_fingers = sum(fingers)
count = 0

for i in range(1, 6):
    if (total_fingers + i) % (n + 1) != 1:
        count += 1

print(count)