year = int(input())

while True:
    year += 1
    year_lst = [int(i) for i in str(year)]
    year_st = set(year_lst)
    if len(year_st) >= 4:
        break

print(year)
