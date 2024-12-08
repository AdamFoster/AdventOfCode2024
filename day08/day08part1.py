#answer = 254

#filename = 'sample01.txt'
filename = 'input.txt'

width = 0
height = 0
antennas: dict[str, list[tuple[int,int]]] = {}
with open(filename, "r") as f:
    for r,line in enumerate(f):
        height += 1
        width = len(line)-1
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
            an = (t[0]+dr, t[1]+dc)
            if 0 <= an[0] < height and 0 <= an[1] < width:
                antinodes.add(an)

            dr = s[0]-t[0]
            dc = s[1]-t[1]
            an = (s[0]+dr, s[1]+dc)
            if 0 <= an[0] < height and 0 <= an[1] < width:
                antinodes.add(an)
        locs.insert(i, s)

print(antinodes)
print(len(antinodes))
