from random import randint
N=4
x=[]
for i in range (N):
    x.append([0]*N)
    for j in range (N):
        x[i][j]=randint(1,10)
        print ( "{:4d}".format(x[i][j]), end = "" )
    print()

