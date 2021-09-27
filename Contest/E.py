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
 
 
 
n = inputi()
 
a = inputlf()
b = inputlf() 
c = inputlf()
 
error = 10e-4
 
def solve2(m):
    fn_1 = m
    
    fn = c[n-1]*1.0*m/a[n-1]
    
    ans = [fn,fn_1]
 
    for i in range(0,n-2):
        idx = n-2-i
 
        ga =  (fn_1*a[idx]-(b[idx]*fn))/(c[idx]*1.0)
        fn = float(fn_1)
        fn_1 = float(ga)
        ans.append(fn_1)
 
    return  ans[::-1],fn_1
    
 
def solve():
    l = 0
    r = 10000000
 
    for i in range(1000):
        m = l+(r-l)/2.0
        ans,final = solve2(m)
        #print(ans,final)
        if  abs(final-1)<error:
            return ans
        else:
            if final<1:
                l = m
            else:
                r = m
    return None
 
 
ans = solve()
 
print(list2string(ans))