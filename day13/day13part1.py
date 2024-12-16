#answer = 29436

filename = 'sample01.txt'
filename = 'input.txt'

LIMIT = 100*3 + 100 + 1
        

total = 0
with open(filename, "r") as f:

    while line:= f.readline():
        aa = line.split(':')[1].strip().split(',')
        bb = f.readline().split(':')[1].strip().split(',')
        pp = f.readline().split(':')[1].strip().split(',')
        f.readline() # eat empty line

        a = (int(aa[0][2:]), int(aa[1][3:]))
        b = (int(bb[0][2:]), int(bb[1][3:]))
        p = (int(pp[0][2:]), int(pp[1][3:]))

        print(a,b,p)

        bestcost = LIMIT

        for apress in range(100):
            for bpress in range(100):
                x = a[0] * apress + b[0] * bpress
                y = a[1] * apress + b[1] * bpress
                if (x,y) == p:
                    cost = 3*apress + bpress
                    if cost < bestcost:
                        bestcost = cost

        print(bestcost)
        if bestcost < LIMIT:
            total += bestcost
print(total)

