import re


with open('../puzzle_in/03.txt') as file:
    data = file.read().rstrip()

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

result = 0

for match in matches:
    m  = match.replace('mul(', '').replace(')', '')
    m = m.split(',')
    number_one = int(m[0])
    number_two = int(m[1])
    
    result += number_one * number_two

print(result)
