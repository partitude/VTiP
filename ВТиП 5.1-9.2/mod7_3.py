from math import sqrt
from math import sin
from math import degrees
def f():
    print('введите x')
    x=float(input())
    y=sqrt(1-pow(degrees(sin(x)),2))
    return (y)
if __name__ == "__main__":
    x=float(input())
    print(sqrt(1-pow(degrees(sin(x)),2)))
