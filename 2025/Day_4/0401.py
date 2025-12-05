
with open('./2025/Day_4/real.txt') as f:
    lines = f.read().splitlines()

def check_position(lines, row, col):
    max_row = len(lines)
    max_col = len(lines[0])
    min_row = 0
    min_col = 0

    if row < min_row or row >= max_row or col < min_col or col >= max_col:
        #print(f'  Position ({row}, {col}) is out of bounds')
        return 0
    if lines[row][col] == '@':
        #print(f'  Found "@" at position ({row}, {col})')
        return 1
    #print(f' "." at position ({row}, {col})')
    return 0

def count_adjacent(lines, row, col):
    count = 0
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            #print(f'  Checking adjacent position ({x}, {y})')
            count += check_position(lines, x, y)
            if count > 4:
                return 0
    return 1
    

res = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):

        count = 0

        if lines[i][j] == '.':
            continue
        else:
            #print(f'Checking position ({i}, {j}) with value {lines[i][j]}')
            res += count_adjacent(lines, i, j)
            #print(f'  Total count so far: {res}')
            #exit()

print(res)