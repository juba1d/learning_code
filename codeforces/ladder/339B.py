x1=input("")        
x=x1.split()
n=int(x[0])
m=int(x[1])
y1=input("")       
y=y1.split()
for i in range(0,m):
    y[i]=int(y[i])
a=[]
a.append(y[0]-1)
for i in range(0,m-1):
    if y[i+1]>y[i]:
        a.append(y[i+1]-y[i])
    elif y[i+1]<y[i]:
        a.append(n-y[i]+y[i+1])
    else:
        a.append(0)
print(sum(a))