n = int(input())

max_coders = (n * n + 1) // 2
print(max_coders)

grid = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            grid[i][j] = 'C'

for row in grid:
    print(''.join(row))
