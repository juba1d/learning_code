import math
n, m = map(int,input().split())
l = list(map(int, input().split()))
for i in range(n):
	l[i] = math.ceil(l[i]/m)
 
l.reverse()
k = l.index(max(l))
 
print(n-k)