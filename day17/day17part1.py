#answer = 4,6,1,4,2,1,3,1,6

filename = '/Users/adam/DevProjects/AdventOfCode2024/day17/sampleTest.txt'
#filename = 'input.txt'

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

done = False
step = 0
while not done:
    if IP >= len(INS):
        break
    #print(step, IP)
    step += 1
    process(INS[IP],INS[IP+1])
print(",".join(OUTPUT))