#answer = 313

filename = 'sample01.txt'
filename = 'input.txt'

towels = set()
possible = 0


with open(filename, "r") as f:
    towels = [t.strip() for t in f.readline().strip().split(",")]
    f.readline()

    while pattern := f.readline().strip():
        found = False
        done = False

        cache: dict[str,bool] = {}

        totest = list()
        totest.append(pattern)
        while not found and totest:
            #print(totest)
            p: str = totest.pop(0)
            cancontinue = False
            for t in towels:
                if t == p:
                    found = True
                    cache[p] = True
                    break
                else:
                    if p.startswith(t):
                        newtest = p[len(t):]
                        if newtest in cache:
                            #print("Cache hit for", newtest, cache[newtest])
                            if cache[newtest]:
                                cancontinue = True
                                cache[p] = True
                        else:
                            totest.insert(0, p[len(t):])
                            cancontinue = True
            if not cancontinue:
                cache[p] = False

        if found:
            possible += 1
            print("Pattern is possible ",pattern)
        else:
            print("Pattern NOT possible",pattern)

    print(possible)