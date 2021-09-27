
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
 
 
def solve(a,k):
    cnt =0
    suma = 0
    for value in range(k):
        if cnt == k:
            return suma
        if a[0]==a[1]:
            if a[1]!=a[2]:
                if cnt<=(k-2):
                    cnt+=2
                    suma+=a[0]*2
                    a[0]-=1
                    a[1]-=1
                else:
                    cnt+=1
                    suma+=a[1]
                    a[1]-=1
            else:
                if cnt<=(k-3):
                    cnt+=3
                    suma+=a[0]*3
                    a[0]-=1
                    a[1]-=1
                    a[2]-=1
                elif cnt<=(k-2):
                    cnt+=2
                    suma+=a[0]*2
                    a[1]-=1
                    a[2]-=1
                else:
                    cnt+=1
                    suma+=a[2]
                    a[2]-=1
 
        else:
            if cnt<=(k-1):
                cnt+=1
                suma+=a[0]*1
                a[0]-=1
    #print(cnt,suma)
    return suma
[a1,a2,a3,k] = inputli()
 
 
a = sorted([a1,a2,a3])[::-1]
 
ans = solve(a,k)
 
print(ans)