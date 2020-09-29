def max(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    elif a==b:
        return ('числа одинаковы')
a=int(input())
b=int(input())
max(a,b)
print(max(a,b))
