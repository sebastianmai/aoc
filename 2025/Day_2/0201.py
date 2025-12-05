

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
        
        if string_i[:len(string_i)//2] == string_i[len(string_i)//2:]:
            res += i

            print(f'Found palindrome: {string_i}')

print(f'Result: {res}')