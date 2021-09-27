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
 
 
 
 
def verify_cond(n,s,r):
    if r/n<=s:
        return 'AC'
    else:
        return 'TLE'
 
def solve():
    q = inputli()[0]
    for _ in range(q):
        n,s,r =  inputli()
        sol = verify_cond(n,s,r)    
        print(sol)
if __name__ == '__main__':
    solve()