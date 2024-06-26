"""

input()
I=lambda:list(map(int,input().split()))
d=I()
a,b=I()
print(sum(d[a-1:b-1]))

"""

# Read input data
import sys
input = sys.stdin.read
# `data = input().split()` is reading the input from the standard input (stdin) and splitting it into
# a list of strings based on whitespace. This allows you to access individual elements of the input
# data easily by indexing the list.
data = input().split()

# Extract values from input
n = int(data[0])  # Number of ranks
d = list(map(int, data[1:n]))  # Years to rise from rank i to i+1
a = int(data[n])  # Current rank of Vasya
b = int(data[n+1])  # Desired rank of Vasya

total_years = 0

# Calculate years needed from rank a to rank b
for i in range(a, b):
    total_years += d[i-1]

# Output the total years needed
print(total_years)
