import math

dial_start = 50
ranges = 100

res = dial_start
count = 0

with open('./02.txt') as file:
    for line in file: 
        data = line.split()[0]
        direction = data[0]
        step = int(data[1:])
        prev = res

        if direction == 'L':
            # number of times we pass index 0 when moving left
            wraps = (step + (ranges - prev)) // ranges
            res = (res - step) % ranges
        else:
            # number of times we pass index 0 when moving right
            wraps = (prev + step) // ranges
            res = (res + step) % ranges

        count += wraps
        
print(count)
