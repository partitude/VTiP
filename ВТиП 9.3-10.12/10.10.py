from random import randint
N=4
M=5
x=[]
for i in range (N):
    x.append([0]*M)
    for j in range (M):
        x[i][j]=randint(1,10)
        print ( "{:4d}".format(x[i][j]), end = "" )
    print()

