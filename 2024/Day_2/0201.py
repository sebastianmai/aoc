list = []

# read the file
with open('/home/basti/DATEN/Universität/Konstanz/Programmieren/aoc/2024/puzzle_in/02.txt') as file:
    for line in file:
        data = line.strip().split()
        list.append(data)

count = 0

for l in list:
    test = True
    increase, increase_prev = None, None

    for i in range(0, len(l)-1):
        difference = int(l[i])-int(l[i+1])
        
        if difference > 0:
            increase = True
        else:
            increase = False

        if abs(difference) not in [1,2,3] or increase_prev is not None and increase_prev != increase:
            test = False
            break
        
        increase_prev = increase

    if test:
        count += 1

print(count)
