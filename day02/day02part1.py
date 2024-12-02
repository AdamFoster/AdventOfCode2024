#answer = 341

#filename = 'sample01.txt'
filename = 'input.txt'

safecount = 0
with open(filename, "r") as f:
    for line in f:
        data = [int(x) for x in line.split()]
        safe = True
        sign = 0
        c = data[0]
        for c2 in data[1:]:
            if c == c2:
                safe = False
                print(data, "Equal")
                safe = False
                break
            if sign == 0:
                sign = c2 - c
                sign = sign // abs(sign)
            else:
                newsign = c2 - c
                newsign = newsign // abs(newsign)
                if sign != newsign:
                    print(data, "Not monotonic")
                    safe = False
                    break
            if 1 <= abs(c2-c) <= 3:
                pass #safe
                c = c2
            else:
                print(data, "Not in range")
                safe = False
                break
        if safe:
            print("SAFE", data)
            safecount += 1
print(safecount)