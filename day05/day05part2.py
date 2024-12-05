#answer = 4030

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
priorities = {}
total = 0
with open(filename, "r") as f:
    while line := f.readline().strip():
        if len(line) == 0:
            break
        [prior, page] = [int(x) for x in line.split('|')]
        if page in priorities:
            priorities[page].append(prior)
        else:
            priorities[page] = [prior]

        #print(prior, '=>', page)

    while line := f.readline().strip():
        if len(line) == 0:
            break
        pages = [int(x) for x in line.split(',')]
        valid = False
        modified = False

        while not valid:
            valid = True
            for i in range(len(pages)):
                page = pages[i]
                if page in priorities:
                    for priority in priorities[page]:
                        if priority in pages[i:]:
                            valid = False
                            pages.remove(priority)
                            pages.insert(i,priority)
                            modified = True
                            break
                    if not valid:
                        break
        if modified:
            print(pages, pages[len(pages)//2])
            total += pages[len(pages)//2]
print(total)




