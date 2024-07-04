#so_simple

def cell_converter(location):
    if len(location) > 2 and len(location) < 5:
        col = location[0:2]
        row = location[2:4]
        final_col = (ord(col[0:1]) - 64) * 26 + (ord(col[1:2]) - 64)
        print("R" + str(row) + "C" + str(final_col))
    elif len(location) < 5:
        col = location[0:1]
        row = location[1:2]
        final_col = (ord(col) - 64)
        print("R" + str(row) + "C" + str(final_col))
    else:
        row = location[1:3]
        col = int(location[4:6])
        final_col = chr(64 + col // 26) + chr(64 + col % 26)
        print(final_col + row)

n = int(input())

for i in range(n):
    cell_converter(input())

