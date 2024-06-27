# Reading input values
n, m, a, b = map(int, input().split())

# Calculate cost using only single ride tickets
total_cost_single = n * a

# Calculate cost using only unlimited ride tickets
if n % m == 0:
    total_cost_unlimited = (n // m) * b
else:
    total_cost_unlimited = (n // m) * b + b

# Calculate combined cost
full_tickets_needed = n // m
remaining_rides = n % m
total_cost_combined = full_tickets_needed * b + remaining_rides * a

# Find the minimum cost
min_cost = min(total_cost_single, total_cost_unlimited, total_cost_combined)

# Print the minimum cost
print(min_cost)
