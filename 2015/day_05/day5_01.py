with open("/home/bastimai/Data/Programms/aoc/2015/day_05/input.txt", "r") as file:
    input = [line.strip() for line in file]

count = 0

for word in input:
    vocal = 0
    doubled = False
    for i in range(0, len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            vocal += 1
        if i != len(word)-1 and word[i] == word[i+1]:
            doubled = True

        pairs = ['ab', 'cd', 'pq', 'xy']
        contains_pair = any(pair in word for pair in pairs)

    if vocal >= 3 and doubled and not contains_pair:
        count += 1
    
print(count)