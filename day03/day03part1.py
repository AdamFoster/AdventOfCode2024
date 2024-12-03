#answer = 153469856

import re

p = re.compile('^mul\\(([0-9]+),([0-9]+)\\)')

#filename = 'sample01.txt'
filename = 'input.txt'

total = 0
with open(filename, "r") as f:
    for line in f:
        while len(line) > 7:
            if m := p.match(line):
                total += int(m.group(1)) * int(m.group(2))
                print(m.group(), total)

                line = line[m.end():]
            else:
                line = line[1:]
print(total)
