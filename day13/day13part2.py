#answer = 103729094227877

filename = 'sample01.txt'
filename = 'input.txt'

F = 10000000000000


total = 0
with open(filename, "r") as f:

    while line:= f.readline():
        aa = line.split(':')[1].strip().split(',')
        bb = f.readline().split(':')[1].strip().split(',')
        ss = f.readline().split(':')[1].strip().split(',')
        f.readline() # eat empty line

        a = (int(aa[0][2:]), int(aa[1][3:]))
        b = (int(bb[0][2:]), int(bb[1][3:]))
        s = (int(ss[0][2:]), int(ss[1][3:]))
    
        s = (F+s[0], F+s[1]) # part 2

        print(a,b,s)

        q = None
        p = None
        q_num = s[1]*a[0] - s[0]*a[1]
        q_dom = b[1]*a[0] - b[0]*a[1]
        if q_dom == 0:
            print(f"{q_num=} {q_dom=}")
        elif q_num % q_dom != 0:
            print("No integer solutions for q")
        else:
            q = q_num // q_dom
            p_num = s[0] - b[0]*q
            p_dom = a[0]
            if p_dom == 0:
                p = 0
            elif p_num % p_dom != 0:
                print("No integer solutions for p")
            else:
                p = p_num // p_dom
        cost = p*3 + q if p and q else 0
        print(f"{q=} {p=} {cost=}")
        
        total += cost
        

print(total)

