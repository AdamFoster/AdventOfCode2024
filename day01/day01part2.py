#answer = 21070419

#filename = 'sample01.txt'
filename = 'input.txt'

l1 = []
l2 = {}
d = 0
with open(filename, "r") as f:
    for line in f:
        [i1, i2] = [int(x) for x in line.split()]
        l1.append(i1)
        if i2 in l2:
            l2[i2] = l2[i2] + 1
        else:
            l2[i2] = 1
    l1.sort()
    #l2.sort()
    for i1 in l1:
        if i1 in l2:
            d += i1 * l2[i1]

print(d)
    

