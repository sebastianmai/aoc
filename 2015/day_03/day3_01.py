with open("/home/bastimai/Data/Programms/aoc/2015/day_03/input.txt", "r") as file:
    input = [list(line) for line in file]
coordinates = (0,0)
sets = set()
sets.add(coordinates)

for i in range(0, len(input[0])-1):
    if input[0][i] == "<":
        coordinates = (coordinates[0]-1, coordinates[1]) 
    elif input[0][i] == ">":
        coordinates = (coordinates[0]+1, coordinates[1])
    elif input[0][i] == "^": 
        coordinates = (coordinates[0], coordinates[1]+1)
    elif input[0][i] == "v":
        coordinates = (coordinates[0], coordinates[1]-1)
    print(coordinates)
    sets.add(coordinates)
    print(sets)

print(len(sets))