#learn sliding window

n, m = map(int, input().split())
puzzle_pieces = list(map(int, input().split()))

puzzle_pieces.sort()

min_difference = float('inf')

"""
index 0 to n-1 | for n things
index i to i+n-1 
    but the last index is m-1
    so i+n-1<=m-1
    i<=m-n
window start from 0 to m-n
    so loop should run for m-n+1
"""

for i in range(m - n + 1):
    difference = puzzle_pieces[i + n - 1] - puzzle_pieces[i]
    if difference < min_difference:
        min_difference = difference

print(min_difference)

