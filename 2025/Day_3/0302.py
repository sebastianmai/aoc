import itertools

with open('./2025/Day_3/dummy.txt') as f:
    lines = f.read().splitlines()

res = 0
max_length = 12

for line in lines:
    maximum = 0

    temp = line


    for i in range(len(line), 0, -1):
        if len(temp) > max_length:
            if temp[i-1] in temp[0:i-1]:
                if int(temp.replace(temp[i-1], '', 1)) >= int(temp.replace(temp[0:i-1], '', 1)):
                    temp = temp.replace(temp[i-1], '', 1)
        else:
            res += int(temp)
            print(f'Adding {temp} to result')
            break

            
print(f'Result: {res}')




    