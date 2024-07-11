n=int(input())

mag=[]

for _ in range(n):
    mag.append((input()))
    
count=1

for i in range(len(mag)-1):
    if mag[i] != mag[i+1]:
        count+=1

print(count)