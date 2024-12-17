#answer = 6398

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

def ticks(time:int):
    positions: set[tuple[int,int]] = set()
    for r in robots:
        p, v = r
        pend = ((p[0]+v[0]*time)%C, (p[1]+v[1]*time)%R)
        positions.add(pend)
    return positions
        
def printgrid(positions: set[tuple[int,int]]):
    print("-"*C)
    for r in range(R):
        for c in range(C):
            if (c,r) in positions:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()

for t in range(1000):
    tn = t
    tn = 35 + 101*t
    positions = ticks(tn)
    #print(tn)

    # quads = [[0,0],[0,0]]
    # for position in positions:
    #     xq, yq = 0, 0
    #     if position[0] == C//2 or position[1] == R//2:
    #         pass
    #     else:
    #         if position[0] > C//2:
    #             xq = 1
    #         if position[1] > R//2:
    #             yq = 1
    #         quads[xq][yq] += 1
    #if quads[0][0] == quads[1][0] and quads[0][1] == quads[1][1]:
    print(tn)
    printgrid(positions)
        #ßbreak
    #print(t)
    #print("P", positions)
    #print("Q", quads)