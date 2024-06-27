data = list(input())
symbols = ['H', 'Q', '9']
has = False;
for d in data:
    if d in symbols:
        has = True
        break
if has:
    print("YES")
else:
    print("NO")