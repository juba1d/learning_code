t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    x = sum(1 for review in a if review == 1) - sum(1 for review in a if review == -1)
    y = sum(1 for review in b if review == 1) - sum(1 for review in b if review == -1)
    
    print(max(x, y))
