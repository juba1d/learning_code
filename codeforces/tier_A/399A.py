t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print("YES")
        continue
    
    a.sort()
    diffs = []
    
    for i in range(1, n):
        dif = abs(a[i] - a[i - 1])
        diffs.append(dif)
    
    diffs.sort(reverse=True)
    
    if diffs[0] > 1:
        print("NO")
    else:
        print("YES")
