#answer = 6239783302560

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data = [int(x) for x in line.strip()]

size = sum(data)
blocks = [] #(data, size)
for i,d in enumerate(data):
    if i%2 == 0:
        blocks.append((i//2, d))
    else:
        blocks.append((-1, d))

e = len(blocks)-1

while blocks[e][1] == -1:
    e -= 1

print(blocks)

while e > 0:
    for i in range(e):
        mover = blocks[e]
        space = blocks[i]
        if mover[0] > -1 and space[0] == -1:
            if space[1] == mover[1]:
                blocks[i] = mover
                blocks[e] = (-1, mover[1])
                break
            elif space[1] > mover[1]:
                newspace = (-1, space[1]-mover[1])
                blocks[i] = (mover[0], mover[1])
                blocks[e] = (-1, mover[1])
                blocks.insert(i+1, newspace)
                e += 1
                break
            else: #no fit, increase i and try again
                pass
    e -= 1

print(blocks)

i = 0
total = 0
for b in blocks:
    if b[0] == -1:
        i += b[1]
    else:
        for j in range(b[1]):
            total += i * b[0]
            i += 1

print(total)