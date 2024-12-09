with open("/home/bastimai/Data/Programms/aoc/2015/day_03/input2.txt", "r") as file:
    input = [list(line) for line in file]
coordinatessanta, coordinatesrobot = (0,0), (0,0)
setssanta, setsrobot = set(), set()

setssanta.add(coordinatessanta)

for i in range(0, len(input[0])-1, 2):
    print(input[0][i], input[0][i+1])
    if input[0][i] == "<" or input[0][i+1] == "<":
        coordinatessanta = (coordinatessanta[0]-1, coordinatessanta[1])
        coordinatesrobot = (coordinatesrobot[0]-1, coordinatesrobot[1])
    elif input[0][i] == ">" or  input[0][i+1] == ">":
        coordinatessanta = (coordinatessanta[0]+1, coordinatessanta[1])
        coordinatesrobot = (coordinatesrobot[0]+1, coordinatesrobot[1])
    elif input[0][i] == "^" or input[0][i+1] == "^": 
        coordinatessanta = (coordinatessanta[0], coordinatessanta[1]+1)
        coordinatesrobot = (coordinatesrobot[0], coordinatesrobot[1]+1)
    elif input[0][i] == "v" or input[0][i+1] == "v":
        coordinatessanta = (coordinatessanta[0], coordinatessanta[1]-1)
        coordinatesrobot = (coordinatesrobot[0], coordinatesrobot[1]-1)

    setssanta.add(coordinatessanta)
    setsrobot.add(coordinatesrobot)

result = setssanta.union(setsrobot)

print(result)
print(len(result))
