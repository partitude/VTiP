L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]
if 'привет' in L:
    L.remove('привет')
    print(L)
else :
    L.insert(-1,'привет')
    print(L)
cou=L.count(4)
print(cou)
if cou>1:
    L.clear()
    print(L)
    
