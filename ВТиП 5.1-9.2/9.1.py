L = [3, 6, 7, 4, -5, 4, 3, -1]
e=sum(L)
print('сумма=',e)
if e>2:
    print(len(L))
maxl=max(L)
minl=min(L)
print('минимальный =',minl)
print('максимальный=',maxl)
if maxl-minl>10:
    print(sorted(L))
else:
    print('разность меньше 10')
