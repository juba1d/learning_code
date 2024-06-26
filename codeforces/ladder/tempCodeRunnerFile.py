a=[0,0,0]
for i in range(3):
	a[i]=list(map(int,input().split()))
for i in range(3):
	for j in range(3):
		sum=0
		sum+=a[i][j]
		if(i>0):
			sum += a[i - 1][j]
		if (i != 2):
			sum += a[i + 1][j]
		if (j > 0):
			sum += a[i][j - 1]
		if (j != 2):
			sum += a[i][j + 1]
 
		print((1-sum)%2,end='')
    print()