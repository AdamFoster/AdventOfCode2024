#answer = 1223326

#filename = 'sample01.txt'
filename = 'input.txt'

l1 = []
l2 = []
d = 0
with open(filename, "r") as f:
    for line in f:
        [i1, i2] = [int(x) for x in line.split()]
        l1.append(i1)
        l2.append(i2)
    l1.sort()
    l2.sort()
    for i1,i2 in zip(l1,l2):
        d += abs(i1-i2)

print(d)
    

