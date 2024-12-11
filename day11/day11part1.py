#answer = 233050

filename = 'sample02.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data = [int(x) for x in line.strip().split()]

def blink(stones: list[int]) -> list[int]: 
    results: list[int] = []
    for stone in stones:
        if stone == 0:
            results.append(1)
        elif len(str(stone)) % 2 == 0:
            ss = str(stone)
            ls = len(ss)
            s1 = int(ss[:ls//2])
            s2 = int(ss[ls//2:], 10)
            #print(ss, s1, s2)
            results.append(s1)
            results.append(s2)
            
        else:
            results.append(stone*2024)
    return results

print(data)    

b = data
for i in range(25):
    b = blink(b)
    print(i, len(b))
