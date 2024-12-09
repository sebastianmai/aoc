with open("/home/bastimai/Data/Programms/aoc/2015/day_02/input2.txt", "r") as file:
    input = [list(map(int, line.strip().split('x'))) for line in file]

sum = 0

for i in range(0, len(input)):
    minimum = sorted([input[i][0], input[i][1], input[i][2]])
    sum += minimum[0] * minimum[1] * minimum[2] + 2* (minimum[0] + minimum[1])

print(sum)