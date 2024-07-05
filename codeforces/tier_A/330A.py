# Read the dimensions of the cake grid
r, c = map(int, input().split())

# Initialize the cake grid
cake = [input() for _ in range(r)]

# Initialize sets to keep track of rows and columns that contain strawberries
rows_with_strawberry = set()
cols_with_strawberry = set()

# Populate the sets with rows and columns that contain strawberries
for i in range(r):
    for j in range(c):
        if cake[i][j] == 'S':
            rows_with_strawberry.add(i)
            cols_with_strawberry.add(j)

# Calculate the number of edible cells
# All cells in rows without strawberries plus all cells in columns without strawberries
# Minus the cells counted twice at the intersections of such rows and columns
edible_cells = (r - len(rows_with_strawberry)) * c + (c - len(cols_with_strawberry)) * r - (r - len(rows_with_strawberry)) * (c - len(cols_with_strawberry))

# Print the number of edible cells
print(edible_cells)