x=int(input())

counter=0
while x>0:
    choice= input().split(' ')
    #print(choice)
    a=int(choice[0])
    b=int(choice[1])
    c=int(choice[2])
    decision=(a+b+c)
    if decision>1:
        counter+=1
    x-=1
print(counter) 
    
    
