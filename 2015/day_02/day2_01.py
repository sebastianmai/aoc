with open("/home/bastimai/Data/Programms/aoc/2015/day_02/input.txt", "r") as file:
    input = [list(map(int, line.strip().split('x'))) for line in file]

sum = 0

for i in range(0, len(input)):
    minimum = [int(input[i][0])*int(input[i][1]), int(input[i][0])*int(input[i][2]), int(input[i][1])*int(input[i][2])]
    sum += 2 * minimum[0] + 2 * minimum[1] + 2 * minimum[2] + min(minimum)

print(sum)
