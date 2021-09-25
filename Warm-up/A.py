import math
[n,m,a] = list(map(int,input().split()))

dist = math.ceil(n*1.0/a)*math.ceil(m*1.0/a)

print(dist)