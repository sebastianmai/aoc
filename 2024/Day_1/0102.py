#initialize lists
list_one, list_two = [], []

#read puzzle input
with open('./puzzle_in/01.txt') as file:
    for line in file:
        data = line.strip().split()
        list_one.append(data[0])
        list_two.append(data[1])

#count the occurances
dictionary = dict()

for i in range(0, len(list_two)):
    if list_two[i] in dictionary.keys():
        dictionary[list_two[i]] += 1
    else:
        dictionary[list_two[i]] = 1

# calculate the similiarity score
similarity = 0

for i in range(0, len(list_one)):
    if list_one[i] in dictionary.keys():
        similarity += dictionary[list_one[i]] * int(list_one[i])

print(similarity)
