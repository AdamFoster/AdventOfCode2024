#answer = 

filename = '/Users/adam/DevProjects/AdventOfCode2024/day15/sample01.txt'
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
            al = ""
            for c in line:
                if c == ".":
                    al = al + ".."
                elif c == "#":
                    al = al + "##"
                elif c == "O":
                    al = al + "[]"
                else:
                    assert c == "@"
                    loc = (len(area), len(al))
                    al = al + ".."
            area.append([c for c in al])
        else:
            instructions += line

R = len(area)
C = len(area[0])
EMPTY = "."
BOXL = "["
BOXR = "]"
WALL = "#"
BOXES = [BOXL, BOXR]

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

for ic,ins in enumerate(instructions):
    #printgrid()
    #break
    print(f"{ins=} {ic=}")
    rr,cc = loc[0]+DIRS[ins][0], loc[1]+DIRS[ins][1]
    if area[rr][cc] == EMPTY:
        loc = (rr,cc)
        continue
    elif area[rr][cc] == "#":
        continue
    #original
    else:
        assert area[rr][cc] == BOXL or area[rr][cc] == BOXR
        tr, tc = rr, cc

        if DIRS[ins][0] == 0:
            #horizontal move
            while area[tr][tc] == BOXL or area[tr][tc] == BOXR:
                tr, tc = tr+DIRS[ins][0], tc+DIRS[ins][1]
            if area[tr][tc] == "#":
                continue
            else:
                assert area[tr][tc] == EMPTY, f"{area[tr][tc]=} {tr=} {tc=}"
                loc = (rr,cc)
                mod = BOXES.index(area[rr][cc])
                while (tr,tc) != (rr,cc):
                    mod = (mod+1)%2
                    area[tr][tc] = BOXES[mod]
                    tr,tc = tr-DIRS[ins][0], tc-DIRS[ins][1]
                area[rr][cc] = EMPTY
        else:
            # vertical move
            ttm: list[set[tuple[int,int]]] = [] # try to move
            ttm.append([loc])
            done = False
            canmove = True
            while not done:
                done = True
                tocheck = ttm[-1]
                nextlevel = set()
                for l in tocheck:
                    tr, tc = l[0]+DIRS[ins][0], l[1]+DIRS[ins][1]
                    if area[tr][tc] == EMPTY:
                        continue
                    elif area[tr][tc] == WALL:
                        canmove = False
                        break
                    else:
                        assert area[tr][tc] == BOXL or area[tr][tc] == BOXR
                        done = False
                        nextlevel.add((tr,tc))
                        if area[tr][tc] == BOXL:
                            nextlevel.add((tr,tc+1))
                        else:
                            nextlevel.add((tr,tc-1))
                ttm.append(nextlevel)
            if canmove:
                while len(ttm) > 0:
                    nextlevel = ttm.pop()
                    for l in nextlevel:
                        area[l[0]+DIRS[ins][0]][l[1]+DIRS[ins][1]] = area[l[0]][l[1]]
                        area[l[0]][l[1]] = "."
                loc = (loc[0]+DIRS[ins][0], loc[1]+DIRS[ins][1])

        
        
print(loc)
printgrid()

total = 0

for r in range(R):
    for c in range(C):
        if area[r][c] == BOXL:
            total += 100 * r + c

print(total)