#answer = 1495147

filename = 'sample01.txt'
filename = 'input.txt'

area: list[list[str]] = []
instructions: str = ""
loc: tuple[int,int] = (0,0)
with open(filename, "r") as f:
    stage = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            stage += 1
        elif stage == 0:
            if "@" in line:
                loc = (len(area), line.index("@"))
            area.append([c for c in line])
        else:
            instructions += line

R = len(area)
C = len(area[0])
EMPTY = "."
BOX = "O"
area[loc[0]][loc[1]] = EMPTY

DIRS = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}

def printgrid():
    print("-"*C)
    for r in range(R):
        for c in range(C):
            if (r,c) == loc:
                print("@", end="")
            else:
                print(area[r][c], end="")
        print()
    print()

for ins in instructions:
    rr,cc = loc[0]+DIRS[ins][0], loc[1]+DIRS[ins][1]
    if area[rr][cc] == EMPTY:
        loc = (rr,cc)
        continue
    elif area[rr][cc] == "#":
        continue
    else:
        assert area[rr][cc] == BOX
        tr, tc = rr, cc
        while area[tr][tc] == BOX:
            tr, tc = tr+DIRS[ins][0], tc+DIRS[ins][1]
        if area[tr][tc] == "#":
            continue
        else:
            assert area[tr][tc] == EMPTY, f"{area[tr][tc]=} {tr=} {tc=}"
            loc = (rr,cc)
            area[rr][cc] = EMPTY
            area[tr][tc] = BOX
        
print(loc)
printgrid()

total = 0

for r in range(R):
    for c in range(C):
        if area[r][c] == BOX:
            total += 100 * r + c

print(total)