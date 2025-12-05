
ranges = []

with open('./2025/Day_5/real.txt') as f:
    for line in f:
        lines = line.strip().split()
    
        if len(lines) == 0:
            continue

        if '-' in lines[0]:
            ranges.append(lines[0])
            continue

intervals = []
for range_str in ranges:
    low, high = map(int, range_str.split('-'))
    intervals.append((low, high))

intervals.sort()

merged_intervals = []
for low, high in intervals:
    print(f"Processing interval: {low}-{high}")
    if not merged_intervals or merged_intervals[-1][1] < low:
        merged_intervals.append((low, high))
    else:
        merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], high))

count = 0
for item in merged_intervals:
    count += len(range(item[0], item[1] + 1))

print(count)
    

