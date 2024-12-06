#answer = 1784

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
obstacles = set()

location = (-1,-1)
direction = 0
DIRS = [(-1,0), (0,1), (1,0), (0,-1)] #Up, Right, Down, Left
rows = 0
cols = 0

with open(filename, "r") as f:
    row = 0
    for line in f:
        cols = len(line.strip())
        for c in range(cols):
            if line[c] == '#':
                obstacles.add((row,c))
            elif line[c] == '^':
                location = (row,c)
        row += 1
    rows = row

print(rows, cols, location)


def checkLoop(loc, dir, obs):
    visited = set()
    while 0 <= loc[0] < rows and 0 <= loc[1] < cols:
        visited.add((loc[0], loc[1], dir))
        if (loc[0]+DIRS[dir][0], loc[1]+DIRS[dir][1]) in obs:
            dir = (dir+1) % 4
        else:
            loc = (loc[0]+DIRS[dir][0], loc[1]+DIRS[dir][1])
        if (loc[0], loc[1], dir) in visited:
            return True, visited
    return False, visited
        

total = 0

_, originalPath = checkLoop(location, direction, obstacles)
dedupedPath = set()
for l in originalPath:
    dedupedPath.add((l[0], l[1]))
for l in dedupedPath:
    obstacles.add((l[0], l[1]))
    loop, _ = checkLoop(location, direction, obstacles)
    if loop:
        total += 1
    obstacles.remove((l[0], l[1]))

print(total)