def a(x,y):
    return x+(2+y)/pow(x,2)
def b(x,y):
    from math import sqrt
    return y+1/sqrt(pow(x,2)+10)
x=int(input())
y=int(input())
z=a(x,y)/b(x,y)
from math import sin
q=2.8*sin(x)+abs(y)
print('z=',z,' q=',q)
