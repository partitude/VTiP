def s(a,b,c):
    p=(a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

print('введите a,b,c')
from math import sqrt
a=float(input())
b=float(input())
c=float(input())
print(s(a,b,c))

