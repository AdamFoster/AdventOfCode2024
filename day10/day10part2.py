#answer = 1794

#filename = 'sample02.txt'
filename = 'input.txt'

DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
data: list[list[int]] = []
with open(filename, "r") as f:
    for line in f:
        data.append([int(x) for x in line.strip()])

rows = len(data)
cols = len(data[0])

def countPeaks(loc: tuple[int,int], height: int) -> int:
    if height == 9:
        return 1
    else:
        peaks:int = 0
        for d in DIRS:
            tr, tc = (loc[0]+d[0],loc[1]+d[1])
            if tr < 0 or tr >= rows or tc < 0 or tc >= cols:
                pass
            else:
                if data[tr][tc] == height+1:
                    peaks += countPeaks((tr,tc), height+1)
        return peaks

print(data)
heads = {}
for rn, row in enumerate(data):
    for cn, item in enumerate(row):
        if item == 0:
            heads[(rn,cn)] = countPeaks((rn,cn),0)
                
print(heads)
score = 0
for head in heads:
    score += heads[head]
print(score)