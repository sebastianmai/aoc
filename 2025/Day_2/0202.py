

with open('./2025/Day_2/input_real.txt') as file:
    for line in file: 
        data = line.strip().split(',')

res = 0

for ranges in data:
    first, second = ranges.split('-')
    print(f'{first}, {second}')

    for i in range(int(first), int(second)+1):
        string_i = str(i)

        if len(string_i) < 2:
            continue

        for pattern_len in range(1, len(string_i)//2 + 1):
            pattern = string_i[:pattern_len]
            if string_i.count(pattern) * pattern_len == len(string_i):
                res += i
                break        
        
print(f'Result: {res}')