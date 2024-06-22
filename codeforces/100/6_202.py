s = input().strip()
current = s[0]
size = len(s)
count = 0

for i in range(size):
    if ord(current) < ord(s[i]):   #compare unicode value and get new character
        current = s[i]
        count = 1
    elif ord(current) == ord(s[i]): #keep counting the current character
        count += 1

print(count * current)
