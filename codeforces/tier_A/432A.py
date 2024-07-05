n, k = map(int, input().split())
participation_counts = list(map(int, input().split()))

eligible_students = 0
for count in participation_counts:
    if count + k <= 5:
        eligible_students += 1

teams = eligible_students // 3
print(teams)