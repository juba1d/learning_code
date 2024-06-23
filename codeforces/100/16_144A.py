# Read the number of soldiers (not actually used in this simplified version)
n = int(input())

# Read the heights of soldiers into a list
heights = list(map(int, input().split()))

# Find the maximum height and its index
max_height = max(heights)
max_index = heights.index(max_height)

# Move the maximum height to the beginning of the list
heights.remove(max_height)
heights.insert(0, max_height)

# Reverse the list to simplify finding the index of the minimum height
heights.reverse()

# Find the minimum height and its index after reversing
min_height = min(heights)
min_index = heights.index(min_height)

# Calculate the result
result = min_index + max_index

# Print the result
print(result)