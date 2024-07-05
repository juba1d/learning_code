n = 3
matrix = []
for _ in range(n):
    line = input().strip()
    matrix.append(list(line))

#https://www.geeksforgeeks.org/centrosymmetric-matrix/

symm="YES"
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=matrix[n-i-1][n-j-1]:
            symm="NO"

#for row in matrix:
#   print(row)
    
print(symm)