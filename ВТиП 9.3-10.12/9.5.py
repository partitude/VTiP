L=['самовар', 'весна', 'лето']
from random import randint
r=L[randint(0,2)]
b=r[randint(0,len(r)-1)]
i=r.index(b)
n=list(r)
n[i]='?'
strok=''.join(n)
print(strok)
