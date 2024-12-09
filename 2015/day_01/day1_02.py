f = open("/home/bastimai/Data/Programms/aoc/2015/day_01/input.txt", "r")
input = f.readline()

sum = 0

for i in range(0, len(input)):
    if input[i] == "(":
        sum += 1
    else:
        sum -= 1
        if sum == -1:
            print(i+1)
            break
