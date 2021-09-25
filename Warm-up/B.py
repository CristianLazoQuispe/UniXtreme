import math




def solution():
    [a,b,c] = list(map(int,input().split()))

    if a ==0 and b==0:
        if c==0:
            print(-1)
            return
        else:
            print(0)
            return

    if a ==0 :
        if b!=0:
            print(1)
            print(format(-c/(1.0*b), ".6f"))
            return
        else:
            print(-1)
            return

    solucion =  b*b-4*a*c

    if solucion<0:
        print(0)
        return

    elif solucion==0:
        print(1)
        print(format(-b/(2.0*a), ".6f"))
        return 
    else:
        print(2)
        a = [(-b-math.sqrt(solucion))/(2.0*a),(-b+math.sqrt(solucion))/(2.0*a)]
        a = sorted(a)
        for v in a:
            print(format(v, ".6f"))
        return

solution()