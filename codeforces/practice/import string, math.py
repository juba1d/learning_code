import string, math
 
def num_to_let(n):
    n-=1
    if (n<26):
        return string.ascii_uppercase[n];
    else:
        return num_to_let(math.floor(n/26)) + string.ascii_uppercase[n%26];
def let_to_num(st):
    if (len(st) == 1):
        return ord(st)-ord('A')+1;
    else:
        return 26*let_to_num(st[0:len(st)-1])+let_to_num(st[len(st)-1]);
 
##actual program
n = int(input())
for i in range(n):
    s = input()
    conv = ''
    RC = [None]*2
    is_rc = (s[0] == 'R' and s[1].isdigit() and (not s[1:].isdigit()))
    if (is_rc):
        a = s.index('R')
        b = s.index('C')
        RC[0] = s[1:b]
        RC[1] = int(s[(b+1):])
        conv = num_to_let(RC[1])+RC[0]
    else:
        ind = 0
        while (not s[ind].isdigit()):
            ind += 1
        RC[0] = s[ind:]
        RC[1] = str(let_to_num(s[:ind]))
        conv = 'R' + RC[0] + 'C' + RC[1]
    print(conv)
    