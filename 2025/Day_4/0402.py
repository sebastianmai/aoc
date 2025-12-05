
with open('./2025/Day_4/real.txt') as f:
    lines = f.read().splitlines()

def check_position(lines, row, col):
    max_row = len(lines)
    max_col = len(lines[0])
    min_row = 0
    min_col = 0

    if row < min_row or row >= max_row or col < min_col or col >= max_col:
        return 0
    if lines[row][col] == '@':
        return 1
    return 0

def count_adjacent(lines, row, col):
    count = 0
    for x in range(row-1, row+2):
        for y in range(col-1, col+2):
            count += check_position(lines, x, y)
            if count > 4:
                return 0
    return 1

def remove_positions(lines, positions):
    for position in positions:
        row, col = position

        lines[row] = lines[row][:col] + '.' + lines[row][col+1:]
    return lines

res = 0
res_prev = 0
stop = False

while not stop:
    positions = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):

            count = 0

            if lines[i][j] == '.':
                continue
            else:
                x = count_adjacent(lines, i, j)
                if count_adjacent(lines, i, j) == 1:
                    positions.append((i, j))
                
                res += count_adjacent(lines, i, j)

    if res == res_prev:
        stop = True
    res_prev = res

    lines = remove_positions(lines, positions)
print(res)