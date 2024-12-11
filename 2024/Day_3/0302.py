import re

with open('../puzzle_in/03.txt') as file:
    data = file.read().rstrip()

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', data)

enable = True
result = 0
for match in matches:
    if match == 'don\'t()':
        enable = False
        continue
    elif match == 'do()':
        enable = True
        continue

    if enable:
        m = match.replace('mul(', '').replace(')', '')
        number_one, number_two =  m.split(',')
        result += int(number_one) * int(number_two)


print(matches)
print(result)
