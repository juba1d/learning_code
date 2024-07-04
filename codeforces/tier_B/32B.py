i = 0
x = input()
out=''
while i<len(x):
      if x[i] == '.':
            out+='0'
            i+=1
            continue
      elif x[i] == '-':
            
            if x[i+1]=='.':
                  out+= '1'
                  i+=1
            elif x[i+1]=='-':
                  out+='2'
                  i+=1
      i+=1
print(out)