#answer = 1939

#filename = 'sample02.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data.append([x for x in line.strip()])
    

rows = len(data)
cols = len(data[0])

d1 = [(1,1),(-1,-1)]
d2 = [(-1,1),(1,-1)]

for r in range(rows):
    data[r] += ['.' for x in range(4)]
for r in range(4):
    data.append(['.' for x in range(cols+4)])

count = 0
for r in range(rows):
    for c in range(cols):
        if data[r][c] == 'A':
            p1 = data[r+d1[0][0]][c+d1[0][1]] + data[r+d1[1][0]][c+d1[1][1]]
            p2 = data[r+d2[0][0]][c+d2[0][1]] + data[r+d2[1][0]][c+d2[1][1]]
            if (p1 == "MS" or p1 == "SM") and (p2 == "MS" or p2 == "SM"):
                count = count + 1
        else:
            pass

print(count)