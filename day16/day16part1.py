#answer = 98520

from collections import deque


filename = 'sample02.txt'
filename = 'input.txt'

DIRS = [(-1,0), (0,1), (1,0), (0,-1)] #Up, Right, Down, Left
dir = 1

S = E = (0,0)

data = []
with open(filename, "r") as f:
    for line in f:
        if "S" in line:
            S = (len(data), line.index("S"))
        if "E" in line:
            E = (len(data), line.index("E"))
        data.append(line.strip())

DP: dict[tuple[int,int,int], int] = {} # localtion,dir -> best cost
Q = deque()

for i,_ in enumerate(DIRS):
    Q.append((E[0],E[1],i))
    DP[(E[0],E[1],i)] = 0


while Q:
    l = Q.popleft()
    r,c,d = l
    rp,cp = r-DIRS[d][0], c-DIRS[d][1]
    if data[rp][cp] == "#":
        continue

    cost = DP[(r,c,d)] + 1
    if (rp,cp,d) in DP:
        oldcost = DP[(rp,cp,d)]
        if cost < oldcost:
            DP[(rp,cp,d)] = cost
            Q.append((rp,cp,d))
    else:
        DP[(rp,cp,d)] = cost
        Q.append((rp,cp,d))

    d = (d+1) % 4
    cost += 1000
    if (rp,cp,d) in DP:
        oldcost = DP[(rp,cp,d)]
        if cost < oldcost:
            DP[(rp,cp,d)] = cost
            Q.append((rp,cp,d))
    else:
        DP[(rp,cp,d)] = cost
        Q.append((rp,cp,d))

    d = (d+2) % 4
    #cost += 1000 #already added above
    if (rp,cp,d) in DP:
        oldcost = DP[(rp,cp,d)]
        if cost < oldcost:
            DP[(rp,cp,d)] = cost
            Q.append((rp,cp,d))
    else:
        DP[(rp,cp,d)] = cost
        Q.append((rp,cp,d))

print(DP[S[0],S[1],1])
