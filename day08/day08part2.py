#answer = 951

#filename = 'sample01.txt'
filename = 'input.txt'

width = 0
height = 0
antennas: dict[str, list[tuple[int,int]]] = {}
with open(filename, "r") as f:
    for r,line in enumerate(f):
        height += 1
        width = len(line.strip())
        for c,a in enumerate(line.strip()):
            if a == '.':
                pass
            else:
                if a in antennas:
                    antennas[a].append((r,c))
                else:
                    antennas[a] = [(r,c)]
print(width, height)

print(antennas)
antinodes: set[tuple[int,int]] = set()

for a in antennas:
    locs = antennas[a]
    for i in range(len(locs)):
        s = locs.pop(i)
        for t in locs:
            dr = t[0]-s[0]
            dc = t[1]-s[1]
            an = t
            while 0 <= an[0] < height and 0 <= an[1] < width:
                antinodes.add(an)
                an = (an[0]+dr, an[1]+dc)

            dr = s[0]-t[0]
            dc = s[1]-t[1]
            an = s
            while 0 <= an[0] < height and 0 <= an[1] < width:
                antinodes.add(an)
                an = (an[0]+dr, an[1]+dc)
        locs.insert(i, s)

# for r in range(height):
#     for c in range(width):
#         if (r,c) in antinodes:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()

print(antinodes)
print(len(antinodes))
