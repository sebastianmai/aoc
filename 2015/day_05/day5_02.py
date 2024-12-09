with open("/home/bastimai/Data/Programms/aoc/2015/day_05/input2.txt", "r") as file:
    input = [line.strip() for line in file]

count = 0

for word in input:
    has_overlapping_pair = any(word[i:i+2] in word[i+2:] for i in range(len(word)-1))

    non_overlapping_pair = any(word[i:i+2] == word[i+2:i+4] for i in range(len(word)-3))

    has_triple_with_one_in_between = any(word[i] == word[i+2] for i in range(len(word)-2))

    if has_overlapping_pair and (non_overlapping_pair or has_triple_with_one_in_between):
        count += 1

print(count)