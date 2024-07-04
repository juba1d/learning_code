n,m=map(int,input().split())

x=list(map(int,input().split()))

a=x[m-1]


count=0

for i in x:
    if i>=a and i!=0: 
        count+=1
    
print(count)
