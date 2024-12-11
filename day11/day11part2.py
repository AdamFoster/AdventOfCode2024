#answer = 276661131175807

filename = 'sample02.txt'
filename = 'input.txt'

STEPS = 75

data = []
with open(filename, "r") as f:
    for line in f:
        data = [int(x) for x in line.strip().split()]

cache: dict[tuple[int,int], int] = {} # (number, step) -> stones at end

def smartblink(stone: int, step: int) -> int:
    if step == STEPS:
        return 1
    if (stone, step) in cache:
        #print("Hit", stone, step)
        return cache[(stone, step)]
    if stone == 0:
        result = smartblink(1, step+1)
    elif len(str(stone)) % 2 == 0:
        ss = str(stone)
        ls = len(ss)
        s1 = int(ss[:ls//2])
        s2 = int(ss[ls//2:], 10)
        #print(ss, s1, s2)
        r1 = smartblink(s1, step+1)
        r2 = smartblink(s2, step+1)
        result = r1 + r2
    else: 
        result = smartblink(stone * 2024, step+1)
    cache[(stone,step)] = result
    return result


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
total = 0
for s in data:
    total += smartblink(s, 0)
print(total)
