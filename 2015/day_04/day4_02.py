import hashlib

input = "yzbqklnj"
x =  True
i = 0

while x:
    s = input + str(i)
    hash = hashlib.md5(s.encode()).hexdigest()

    if all(char == '0' for char in hash[:6]):
        print(hash)
        print(i)
        x = False
        
    i += 1