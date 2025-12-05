
ranges = []
ingredients = []

with open('./2025/Day_5/real.txt') as f:
    for line in f:
        lines = line.strip().split()
    
        if len(lines) == 0:
            continue

        if '-' in lines[0]:
            ranges.append(lines[0])
            continue
        if len(lines) > 0:
            ingredients.append(lines[0])

def check_range(range_str, ingredient):
    low, high = map(int, range_str.split('-'))

    if low <= int(ingredient) <= high:
        return True

    return False


count = 0

for ingredient in ingredients:
    for range_str in ranges:
        if check_range(range_str, ingredient):
            count += 1
            break

print(count)