import math

# Read input values
n, m, a = map(int, input().split())

# Calculate the number of flagstones needed along each dimension
num_flagstones_n = (n + a - 1) // a
num_flagstones_m = (m + a - 1) // a

# Total flagstones required is the product of the two quantities
total_flagstones = num_flagstones_n * num_flagstones_m

# Print the result
print(total_flagstones)