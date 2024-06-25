s = input()
s = s.replace(' ', '')  # Remove all spaces from the string
s = s.lower()

if s[-2] in {'a', 'e', 'i', 'o', 'u', 'y'}:
    print("YES")
else:
    print("NO")
