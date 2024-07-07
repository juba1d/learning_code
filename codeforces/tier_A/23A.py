s=input()
m=0
l=[]
for i in range (0,len(s)):
    for j in range (i+1,len(s)+1):
        l.append(s[i:j])
for i in l:
    if(l.count(i)>=2):
        if(len(i)>m):
            m=len(i)
print(m)