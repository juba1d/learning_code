n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = (k * l) // nl
total_limes = c * d
total_salt = p // np

max_toasts = min(total_drink, total_limes, total_salt)

toasts_per_person = max_toasts // n

print(toasts_per_person)