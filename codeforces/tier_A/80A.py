import math

def prime(s):
    if s == 2:
        return True
    if s % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(s)) + 1, 2):
        if s % i == 0:
            return False
    return True

def solve():
    n,m = map(int,input().split())
    while True:
        n += 1
        if prime(n):
            if n == m:
                print("YES")
                return
            else:
                print("NO")
                return

solve()
