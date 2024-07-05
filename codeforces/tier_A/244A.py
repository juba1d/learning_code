n,k=map(int,input().split())

a=list(map(int,input().split()))
l=[]

for i in range(n*k):
	if i+1 not in a:
		l.append(i+1)
j=0

for i in a:
	print(i, end=" ")
	print(*(z for z in l[j:j+n-1]))
	j=j+n-1