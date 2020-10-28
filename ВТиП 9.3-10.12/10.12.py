from random import randint
N=3
M=5
x=[]
k=1
sov0=0
sov1=0
sov2=0
for i in range (N):
    x.append([0]*M)
    for j in range (M):
        x[i][j]=randint(1,10)
        print ( "{:4d}".format(x[i][j]), end = "" )
    print()
for i in range (N):
    for j in range (M):
        for k in range (M):
            if x[i][j]==x[i][k]:
                if (i==0)and(k!=j):
                    sov0=sov0+1
                if (i==1)and(k!=j):
                    sov1=sov1+1
                if (i==2)and(k!=j):
                    sov2=sov2+1
if (sov0%3==0)and(sov0%2==0)and(sov0/6==1):
    sov0=sov0/2
if (sov1%3==0)and(sov1%2==0)and(sov0/6==1):
    print("chtoto", sov1)
    sov1=sov1/2
if (sov2%3==0)and(sov2%2==0)and(sov0/6==1):
    print("chtoto", sov2)
    sov2=sov2/2
print("Одинаковых чисел в строке 1:",sov0)
print("Одинаковых чисел в строке 2:",sov1)
print("Одинаковых чисел в строке 3:",sov2)
if sov0>sov1:
    if sov0>sov2:
        print("В 1 строке больше всего одинаковых чисел")
    else:
        print("В 3 строке больше всего одинаковых чисел")
else:
    if sov1>sov2:
        print("В 2 строке больше всего одинаковых чисел")
    elif sov2>sov0:
        print("В 3 строке больше всего одинаковых чисел")
if (sov0==sov1)and(sov2==sov0):
    print("В строках одинаковое кол-во одинаковых чисел")
else:
    if (sov0==sov1)and(sov2<sov0):
        print("В строках 1 и 2 одинаковое кол-во одинаковых чисел")
    if (sov1==sov2)and(sov0<sov2):
        print("В строках 2 и 3 одинаковое кол-во одинаковых чисел")
    if (sov0==sov2)and(sov1<sov2):
        print("В строках 1 и 3 одинаковое кол-во одинаковых чисел")




