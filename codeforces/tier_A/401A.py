import math

n, x = map(int, input().split())
cards = list(map(int, input().split()))

total_sum = abs(sum(cards))

min_cards_needed = math.ceil(total_sum / x)

print(min_cards_needed)