n = int(input())
j = input().split()
players = {j[0]:int(j[1])}
records = [[j[0],int(j[1])]]
 
for i in range(1,n):
    t = input().split()
    if t[0] in players:
        players[t[0]] += int(t[1])
    else:
        players[t[0]]=int(t[1])
    records.append([t[0],players[t[0]]])
m = max(players.values())
l = []
for i in players.items():
    if i[1]==m:
        l.append(i[0])
for i in records:
    if i[1]>=m and i[0] in l:
        print(i[0])
        break