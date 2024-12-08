#answer = 1620690235709

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
result = 0
with open(filename, "r") as f:
    for line in f:
        target,rest = line.split(":")
        components = [int(x) for x in rest.strip().split()]
        target = int(target)

        combos = 2 ** (len(components)-1) -1

        print(target, components, combos)


        success = False

        while combos >= 0:
            trial = [x for x in components]
            combo = combos
            #print(trial)
            total = trial.pop(0)
            while trial:
                if combo % 2 == 0:
                    total = total + trial.pop(0)
                else:
                    total = total * trial.pop(0)
                combo = combo // 2

            if total == target:
                success = True
                break
            combos = combos - 1
        if success:
            result += target
        else:
            #also check for concaternation
            success = False
            combos = 3 ** (len(components)-1) -1
            while combos >= 0:
                trial = [x for x in components]
                combo = combos
                #print(trial)
                total = trial.pop(0)
                while trial:
                    if combo % 3 == 0:
                        total = total + trial.pop(0)
                    elif combo % 3 == 1:
                        total = total * trial.pop(0)
                    else:
                        total = int(str(total)+str(trial.pop(0)))
                    combo = combo // 3

                if total == target:
                    success = True
                    break
                combos = combos - 1
            if success:
                result += target


print(result)