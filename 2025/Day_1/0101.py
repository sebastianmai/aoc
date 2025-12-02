dial_start = 50
ranges = 100

res = dial_start
count = 0

with open('./02.txt') as file:
    for line in file: 
        data = line.split()[0]
        
        direction = data[0]
        step = int(data[1:])

        prev = res

        if direction == 'L':
            if res - step < 0:
                res = (res - step) % ranges
                print(prev, step, res)
                continue
            if res - step == 0:
                res = 0
                count += 1
                print(prev, step, res)
                continue
            if res - step > 0:
                res = (res - step) % ranges
                print(prev, step, res)

        if direction == 'R':
            if res + step < ranges:
                res = (res + step) % ranges
                print(prev, step, res)
                continue
            if res + step == ranges:
                res = 0
                count += 1
                print(prev, step, res)
                continue
            if res + step > ranges:
                res = (res + step) % ranges
                print(prev, step, res)
        
        
print(count)
