#answer = 268

from queue import PriorityQueue
from typing import Callable

SAMPLE = False #or True
filename = 'sample01.txt'

X = Y = 7
LIMIT = 12

if not SAMPLE:
    filename = 'input.txt'
    X = Y = 71
    LIMIT = 1024

DIRS = [(-1,0), (0,-1), (1,0), (0,1)] #Left, Up, Right, Down

blocks: set[tuple[int,int]] = set()
with open(filename, "r") as f:
    for line in f:
        x,y = [int(n) for n in line.strip().split(",")]
        blocks.add((x,y))
        if len(blocks) == LIMIT:
            break

visited: set[tuple[int,int]] = set()

def hfunc(loc: tuple[int,int]) -> int:
    return (X-loc[0] + Y-loc[1])

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

def printgrid(marks):
    for y in range(Y):
        for x in range(X):
            if (x,y) in blocks:
                print("#", end="")
            elif (x,y) in marks:
                print("O", end="")
            else:
                print(" ", end="")
        print()

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
        print(current)
        visited.add(current)

        #openSet.Remove(current)
        neighbours = [(current[0]+d[0],current[1]+d[1]) for d in DIRS]
        for neighbor in neighbours:
            if 0<=neighbor[0]<X and 0<=neighbor[1]<Y and neighbor not in blocks:
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
    printgrid(visited)
    assert False, "Couldn't reach goal"


path = A_Star((0,0),(X-1,Y-1), lambda loc: X-loc[0] + Y-loc[1])
#print(path)

printgrid(path)
print(len(path)-1)
