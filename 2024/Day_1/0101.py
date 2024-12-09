#initialize lists
list_one, list_two = [], []

#read puzzle input
with open('./puzzle_in/01.txt') as file:
    for line in file:
        data = line.strip().split()
        list_one.append(data[0])
        list_two.append(data[1])

#sort the lists
list_one = sorted(list_one)
list_two = sorted(list_two)

#initialize total distance
total_distance = 0

#calculate the distance between the two lists
for i in range(0, len(list_one)):
    distance = abs(int(list_one[i]) - int(list_two[i]))
    total_distance += distance

print(total_distance)
