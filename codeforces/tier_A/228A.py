pailam=(input().split(' '))

for i in range(len(pailam)):
    pailam[i] = int(pailam[i])
pailam.sort()

#print(pailam)

need=4
have=1

for i in range(len(pailam)-1):
    if pailam[i]!=pailam[i+1]:
        have+=1
    
print(need-have)



