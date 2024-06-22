n = int(input())  # Read an integer n from input

matrix = []  # Initialize an empty list to store the matrix
c = 0  # Initialize a variable c to store the sum of selected elements
used = []  # Initialize an empty list to keep track of used coordinates

# Reading the matrix input
for i in range(n):
    matrix.append([int(i) for i in input().split()])  # Read each row and convert elements to integers

# Iterating through the matrix to calculate the sum of selected elements
for i in range(n):
    # Check and sum the element at position (i, n // 2)
    if f"{i} {n // 2}" not in used:
        c += matrix[i][n // 2]
        used.append(f"{i} {n // 2}")
    
    # Check and sum the element at position (n // 2, i)
    if f"{n // 2} {i}" not in used:
        c += matrix[n // 2][i]
        used.append(f"{n // 2} {i}")
    
    # Check and sum the element at position (i, i)
    if f"{i} {i}" not in used:
        c += matrix[i][i]
        used.append(f"{i} {i}")
    
    # Check and sum the element at position (i, (n - 1) - i)
    if f"{i} {(n - 1) - i}" not in used:
        c += matrix[i][(n - 1) - i]
        used.append(f"{i} {(n - 1) - i}")

# Print the final sum c
print(c)
