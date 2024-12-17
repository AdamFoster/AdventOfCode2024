#answer = 219512160

SAMPLE = False
filename = 'sample01.txt'

R = 7
C = 11
T = 100

if  not SAMPLE:
    filename = 'input.txt'
    R = 103
    C = 101
    T = 100

robots:list[tuple[tuple[int,int],tuple[int,int]]] = []
with open(filename, "r") as f:
    for line in f:
        pos, vel = line.strip().split()
        p = tuple([int(x) for x in pos.strip()[2:].split(',')])
        v = tuple([int(x) for x in vel.strip()[2:].split(',')])
        
        robots.append((p, v))

quads = [[0,0],[0,0]]
for r in robots:
    p, v = r
    pend = ((p[0]+v[0]*T)%C, (p[1]+v[1]*T)%R)
    print(pend)
    xq, yq = 0, 0
    if pend[0] == C//2 or pend[1] == R//2:
        pass
    else:
        if pend[0] > C//2:
            xq = 1
        if pend[1] > R//2:
            yq = 1
        quads[xq][yq] += 1
print(quads)
print(quads[0][0]*quads[0][1]*quads[1][0]*quads[1][1])

