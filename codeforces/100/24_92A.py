n,m = map(int,input().split())
i=1
while i<=n and m>=i:
	m=m-i
	i+=1
	if i==n+1:
		i=1
print(m)