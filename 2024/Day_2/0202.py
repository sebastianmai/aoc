list = []

# read the file
with open('/home/basti/DATEN/Universität/Konstanz/Programmieren/aoc/2024/puzzle_in/02.txt') as file:
    for line in file:
        data = line.strip().split()
        list.append(data)


def is_safe(l):
    increase_prev = None
    for i in range(len(l) - 1):
        difference = int(l[i]) - int(l[i + 1])
        increase = difference < 0

        if abs(difference) not in [1, 2, 3] or (increase_prev is not None and increase_prev != increase):
            return False
        increase_prev = increase
    return True

def check_for_safe(l):
    if is_safe(l):
        return True

    for i in range(len(l)):
        if is_safe(l[:i] + l[i + 1:]):
            return True
    return False


count = 0

for l in list:
    if check_for_safe(l):
        count += 1

print(count)
