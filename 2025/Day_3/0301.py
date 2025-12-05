
with open('./2025/Day_3/real.txt') as f:
    lines = f.read().splitlines()

res = 0

for line in lines:
    maximum = 0
    
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            together = line[i] + line[j]
            if int(together) > maximum:
                print(f'New maximum found: {together}')
                maximum = int(together)
    res += maximum
            
print(f'Result: {res}')




    