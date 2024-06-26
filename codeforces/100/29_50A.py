n, m = map(int, input().split())
# This line of code is calculating the total number of squares that can fit in a rectangle grid of
# size n by m. It does this by multiplying the values of n and m to get the total number of squares,
# and then dividing by 2 to get the number of squares that can fit in half of the grid. The result is
# then printed to the console.
print((n * m) // 2)