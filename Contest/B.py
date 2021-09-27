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
 
#A = [200,25,95,20]
#B = 5
#C = [100,200,300,50,25]
 
A = inputli()
B = inputli()
C = inputli()
 
def minimum_bat(elements,batts):
    batts = sorted(batts)
    sum_elements = sum(elements)
    if sum_elements>max(batts):
        return -1
    else:
        for bat in batts:
            if bat>=sum_elements:
                return bat    
def solve():
    print(minimum_bat(A,C))
if __name__ == '__main__':
    solve()