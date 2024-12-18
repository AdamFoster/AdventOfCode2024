#answer = 

#filename = '/Users/adam/DevProjects/AdventOfCode2024/day17/sample02.txt'
filename = '/Users/adam/DevProjects/AdventOfCode2024/day17/input.txt'

A = B = C = 0

INS: list[int] = []
with open(filename, "r") as f:
    A = int(f.readline().strip().split()[-1])
    B = int(f.readline().strip().split()[-1])
    C = int(f.readline().strip().split()[-1])
    f.readline()

    INS = [int(x) for x in f.readline().strip().split()[-1].split(",")]

print(A,B,C,INS)

IP = 0
OUTPUT: list[str] = []

def process(opcode, operand):
    global A,B,C,IP,OUTPUT,INS
    jumped = False

    if operand == 4:
        combo = A
    elif operand == 5:
        combo = B
    elif operand == 6:
        combo = C
    else:
        combo = operand

    if opcode == 0: # division
        A = A // (2**combo)
    elif opcode == 1: #bxl bitwise xor
        B = B ^ operand
    elif opcode == 2: #bst mod
        B = combo % 8
    elif opcode == 3: #jnz
        if A != 0:
            IP = operand
            jumped = True
    elif opcode == 4: #bxc
        B = B ^ C
    elif opcode == 5: #out
        OUTPUT.append(str(combo%8))
    elif opcode == 6: #bdv
        B = A // (2**combo)
    elif opcode == 7: #bdv
        C = A // (2**combo)
    
    if not jumped:
        IP = IP + 2

def runProgram(a):
    global A,B,C,IP,OUTPUT,INS
    A = a
    B = 0
    C = 0
    IP = 0
    OUTPUT = []

    done = False
    while not done:
        if IP >= len(INS):
            break
        process(INS[IP],INS[IP+1])
    return OUTPUT


Aparts: list[int] = [0 for x in INS]
Aparts[0] = 1
currentAi = 0
found = False
while not found:
    while Aparts[currentAi] < 8:
        print(Aparts)
        Asofar = 0
        for i in range(currentAi+1):
            Asofar = Asofar*8
            Asofar += Aparts[i]

        output = [int(x) for x in runProgram(Asofar)]
        if output == INS:
            print("Complete:", Aparts)
            found = True
            break
        if output == INS[len(INS)-len(output):]:
            print("Found up to",currentAi,Aparts,output)
            currentAi += 1
            continue
        Aparts[currentAi] += 1

    while Aparts[currentAi] == 8:
        Aparts[currentAi] = 0
        currentAi -= 1
        Aparts[currentAi] += 1
        assert currentAi >= 0


print(Aparts)
Aresult = 0
for a in Aparts:
    Aresult *= 8
    Aresult += a
print(Aresult)