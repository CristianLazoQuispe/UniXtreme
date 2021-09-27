import math
 
def inputi():
    return int(input())
def inputli():
    return list(map(int,input().split(' ')))
def inputls():
    return list(map(str,input().split(' ')))
def inputlf():
    return list(map(float,input().split(' ')))
 
def list2string(lista):
    return ' '.join(list(map(str,lista)))
 
def solve(L,R):
    if L==R:
        if L==0:
            return 1
        return 0
    else:   
        n = R-2*L + 1
        if n>0:
            return int(n*(n+1)/2)
        else:
            return 0
 
if __name__ == '__main__':
    t = inputi()
    for _ in range(t):
        L,R= inputli()
        sol = solve(L,R)    
        print(sol)