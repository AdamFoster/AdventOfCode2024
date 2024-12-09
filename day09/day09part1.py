#answer = 6211348208140

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data = [int(x) for x in line.strip()]

size = sum(data)
blocks = []
for i,d in enumerate(data):
    if i%2 == 0:
        blocks.extend([i//2 for _ in range(d)])
    else:
        blocks.extend([-1 for _ in range(d)])
print(blocks)
assert size == len(blocks)

i = 0
e = len(blocks)-1

while blocks[e] == -1:
    e -= 1

while i < e:
    if blocks[i] == -1:
        blocks[i] = blocks[e]
        blocks[e] = -1
        e -= 1
        while blocks[e] == -1:
            e -= 1
    i += 1

print(blocks)

total = 0
for i,b in enumerate(blocks):
    if b > -1:
        total += i*b
print(total)
