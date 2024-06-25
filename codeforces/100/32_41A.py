
s = input().strip()  # Read the first string
t = input().strip()  # Read the second string

if s == t[::-1]:  # Check if t is the reverse of s
    print("YES")
else:
    print("NO")


"""
a=input()
b=input()
n=len(a)
rev=""
for i in range(n):
    rev=rev+a[-1-i]
if rev==b:
    print("YES")
else:
    print("NO")
"""