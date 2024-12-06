#answer = 5131

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
obstacles = set()
visited = set()
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

while 0 <= location[0] < rows and 0 <= location[1] < cols:
    visited.add(location)
    if (location[0]+DIRS[direction][0], location[1]+DIRS[direction][1]) in obstacles:
        direction = (direction+1) % 4
    else:
        location = (location[0]+DIRS[direction][0], location[1]+DIRS[direction][1])

print(len(visited))