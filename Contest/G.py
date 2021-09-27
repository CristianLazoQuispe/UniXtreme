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
 
 
def solve():
 
    return None
 
[n,m] = inputli()
 
matrix = [None for i in range(n)]
 
sumaf = [None for i in range(n)]
sumac = [None for i in range(m)]
ans = [[None]*m for i in range(n)]
 
for i in range(n):
    fila = inputli()
    matrix[i] = fila
    sumaf[i]= sum(fila)
 
for j in range(m):
    suma = 0
    for i in range(n):
        suma+=matrix[i][j]
    sumac[j]=suma
 
#print(matrix,sumaf,sumac)
for i in range(n):
    for j in range(m):
        ans[i][j] = sumaf[i]+sumac[j]-matrix[i][j]
 
for fila in ans:
    print(list2string(fila))