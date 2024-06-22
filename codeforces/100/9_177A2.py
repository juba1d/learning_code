# Read the size of the matrix
n = int(input())

# Initialize variables to store the sum and track used coordinates
special_sum = 0
used = set()

# Read the matrix input
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate the special sum efficiently
for i in range(n):
    # Sum elements in the middle column
    if (i, n // 2) not in used:
        special_sum += matrix[i][n // 2]
        used.add((i, n // 2))
    
    # Sum elements in the middle row
    if (n // 2, i) not in used:
        special_sum += matrix[n // 2][i]
        used.add((n // 2, i))
    
    # Sum elements on the main diagonal
    if (i, i) not in used:
        special_sum += matrix[i][i]
        used.add((i, i))
    
    # Sum elements on the secondary diagonal
    if (i, n - 1 - i) not in used:
        special_sum += matrix[i][n - 1 - i]
        used.add((i, n - 1 - i))

# Output the calculated special sum
print(special_sum)