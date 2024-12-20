#answer = 1365

from collections import defaultdict
from queue import PriorityQueue
from typing import Callable

filename = 'sample01.txt'
filename = 'input.txt'

maxcheat = 2

DIRS = [(-1,0), (0,1), (1,0), (0,-1)] #Up, Right, Down, Left

start = end = (0,0)
grid = []
with open(filename, "r") as f:
    for line in f:
        if "S" in line:
            start = (len(grid), line.index("S"))
        if "E" in line:
            end = (len(grid), line.index("E"))
        grid.append(line.strip())

Y = len(grid)
X = len(grid[0])

def printgrid(marks):
    for y in range(Y):
        for x in range(X):
            if (y,x) in marks:
                print("O", end="")
            else:
                print(grid[y][x], end="")
        print()

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(start: tuple[int,int], goal: tuple[int,int], h: Callable[[tuple[int,int]], int]):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = PriorityQueue() # sorted by fscore
    openSet.put((h(start), start))

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
    # to n currently known.
    cameFrom: dict[tuple[int,int], tuple[int,int]] = {}

    # For node n, gScore[n] is the currently known cost of the cheapest path from start to n.
    gScore: dict[tuple[int,int], int] = {} #map with default value of Infinity
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    fScore: dict[tuple[int,int], int] = {}  # map with default value of Infinity
    fScore[start] = h(start)

    while not openSet.empty(): # is not empty
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        currentp,current = openSet.get() #:= the node in openSet having the lowest fScore[] value
        if current == goal:
            return reconstruct_path(cameFrom, current)
        #print(current)
        
        #openSet.Remove(current)
        neighbours = [(current[0]+d[0],current[1]+d[1]) for d in DIRS]
        for neighbor in neighbours:
            if 0<=neighbor[1]<X and 0<=neighbor[0]<Y and grid[neighbor[0]][neighbor[1]] != "#":
                # d(current,neighbor) is the weight of the edge from current to neighbor
                # tentative_gScore is the distance from start to the neighbor through current
                tentative_gScore = gScore[current] + 1 #d(current, neighbor)
                gsn = 10**10
                if neighbor in gScore:
                    gsn = gScore[neighbor]
                if tentative_gScore < gsn:
                    # This path to neighbor is better than any previous one. Record it!
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + h(neighbor)
                    #if neighbor not in openSet:
                    if not any(neighbor in item for item in openSet.queue):
                        openSet.put((fScore[neighbor], neighbor))

    # Open set is empty but goal was never reached
    printgrid([])
    assert False, "Couldn't reach goal"


path = A_Star(start,end, lambda loc: abs(end[0]-loc[0]) + abs(end[1]-loc[1]))
#printgrid(path)
baseline = len(path)
print(f"{baseline=}")

forwards = {}
cost = 0
for p in path:
    forwards[p] = cost
    cost += 1

path = A_Star(end,start, lambda loc: abs(start[0]-loc[0]) + abs(start[1]-loc[1]))
backwards = {}
cost = 0
for p in path:
    backwards[p] = cost
    cost += 1

total = 0
savings = defaultdict(int)
for f in forwards:
    for b in backwards:
        if b == f:
            break
        if abs(f[0]-b[0]) + abs(f[1]-b[1]) <= maxcheat:
            saving = forwards[b] - forwards[f] - (abs(f[0]-b[0]) + abs(f[1]-b[1]))
            if saving >= 100:
                savings[saving] += 1
                #print(saving)
                total += 1

print(savings)
print(total)
# result = 0
# for yt in range(1,Y-1):
#     for xt in range(1,X-1):
#         oldline = grid[yt]
#         grid[yt] = grid[yt][:xt] + "T" + grid[yt][xt+1:]

#         path = A_Star(start,end, lambda loc: abs(end[0]-loc[0]) + abs(end[1]-loc[1]))
#         saving = baseline - len(path)
#         if saving:
#             print(saving)
#         if saving >= 100:
#             result += 1
#         grid[yt] = oldline#

# print("Result", result)

