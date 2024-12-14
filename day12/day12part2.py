#answer = 1374934

from collections import deque


#filename = 'sample02.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data.append(line.strip())

R = len(data)
C = len(data[0])
DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

visited: set[tuple[int,int]] = set()

def flood2(start:tuple[int,int]) -> dict[tuple[int,int], list[tuple[int,int]]]:
    value = data[start[0]][start[1]]
    flooded:dict[tuple[int,int], list[tuple[int,int]]] = {} # (r,c) -> edges
    remaining = deque()
    remaining.append(start)
    done = False
    while remaining:
        loc = remaining.popleft()
        edges = [d for d in DIRS]
        for d in DIRS:
            rr = loc[0]+d[0]
            cc = loc[1]+d[1]
            if 0<=rr<R and 0<=cc<C:
                if data[rr][cc] == value:
                    edges.remove(d)
                    if (rr,cc) not in flooded and (rr,cc) not in remaining:
                        remaining.append((rr,cc))
        flooded[loc] = edges
    return flooded

totalprice = 0
for r in range(R):
    for c in range(C):
        if (r,c) in visited:
            continue
        area = flood2((r,c))
        print(area)
        perimiter = 0
        for loc in area:
            visited.add(loc)
            for edge in area[loc]:
                if edge == (1,0):
                    if (loc[0],loc[1]-1) not in area:
                        perimiter += 1
                    elif edge not in area[(loc[0],loc[1]-1)]:
                        perimiter += 1
                elif edge == (-1,0):
                    if (loc[0],loc[1]-1) not in area:
                        perimiter += 1
                    elif edge not in area[(loc[0],loc[1]-1)]:
                        perimiter += 1
                elif edge == (0,1):
                    if (loc[0]-1,loc[1]) not in area:
                        perimiter += 1
                    elif edge not in area[(loc[0]-1,loc[1])]:
                        perimiter += 1
                elif edge == (0,-1):
                    if (loc[0]-1,loc[1]) not in area:
                        perimiter += 1
                    elif edge not in area[(loc[0]-1,loc[1])]:
                        perimiter += 1
        price = len(area)*perimiter
        print(len(area), perimiter, price)
        totalprice += price

print(totalprice)

