#answer = 78965138 # too high

import re

p = re.compile('^mul\\(([0-9]+),([0-9]+)\\)')

#filename = 'sample02.txt'
filename = 'input.txt'

total = 0
with open(filename, "r") as f:
    data = ""
    for line in f:
        data = data + line.strip()

    line = data
    while len(line) > 7:
        if m := p.match(line):
            total += int(m.group(1)) * int(m.group(2))
            print(m.group(), total)
            line = line[m.end():]
        elif line.startswith("don't()"): 
            print("Found dont with ", len(line), "remaining", line[0:10])
            while not line.startswith("do()") and len(line) > 4:
                line = line[1:]
            print("Resuming with ", len(line), "remaining", line[0:10])

        else:
            line = line[1:]
print(total)
