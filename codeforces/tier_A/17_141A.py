#s,i=sorted,input;print('YNEOS'[s(i()+i())!=s(i())::2])

#print("YES"if sorted(input()+input())==sorted(input()) else"NO")

s1=input().lower()
s2=input().lower()
 
string=input().lower()
l=[0]*26
 
for i in range(len(s1)):
    l[ord(s1[i])-97]+=1
 
for i in range(len(s2)):
    l[ord(s2[i])-97]+=1
 
t=0
 
 
for i in range(len(string)):
 
    if l[ord(string[i])-97]!=0:
#        print(string[i],l[ord(string[i])-97])
        l[ord(string[i])-97]-=1
 
    else:
        t=1
        break
 
if t==1:
    
    print("NO")
    
elif t==0 and max(l)==0:
    print("YES")
 
else:
    print("NO")