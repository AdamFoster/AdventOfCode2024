#answer = 2547

#filename = 'sample02.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data.append([x for x in line.strip()])
    

rows = len(data)
cols = len(data[0])
DIR = (0,1,2,3)
dirs = [[(0,x) for x in DIR],
        [(0,-x) for x in DIR],
        [(x,0) for x in DIR],
        [(-x,0) for x in DIR],
        [(x,x) for x in DIR],
        [(x,-x) for x in DIR],
        [(-x,x) for x in DIR],
        [(-x,-x) for x in DIR]]

for r in range(rows):
    data[r] += ['.' for x in range(4)]
for r in range(4):
    data.append(['.' for x in range(cols+4)])

count = 0
for r in range(rows):
    for c in range(cols):
        if data[r][c] == 'X':
            potentials = []
            for d in dirs:
                potential = [data[r+inc[0]][c+inc[1]] for inc in d]
                if "".join(potential) == "XMAS":
                    count = count + 1
        else:
            pass

print(count)