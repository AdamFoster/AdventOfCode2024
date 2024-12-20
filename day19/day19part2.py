#answer = 666491493769758

filename = 'sample01.txt'
filename = 'input.txt'

towels = set()
possible = 0

cache: dict[str,int] = {}
towels: list[str] = []

def process(pattern: str) -> int:
    if pattern in cache:
        return cache[pattern]
    if pattern == "":
        assert False
    
    total = 0
    for t in towels:
        if t == pattern:
            total += 1
        elif pattern.startswith(t):
            subpattern = pattern[len(t):]
            total += process(subpattern)

    cache[pattern] = total
    return total


with open(filename, "r") as f:
    towels = [t.strip() for t in f.readline().strip().split(",")]
    f.readline()

    total = 0
    while pattern := f.readline().strip():
        result = process(pattern)
        print(pattern, result)
        total += result

    print(total)