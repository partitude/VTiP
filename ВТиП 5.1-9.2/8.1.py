s = "У лукоморья 123 дуб зеленый 456"
e=s.count('я')
if e>0:
    print('буква "я" есть, ее индекс:')
    print(s.find ('я'))
else:
    print('буквы "я" нет')
    e1=s.count('у')
if s.count('у')>0:
    print('буква "у" есть, количество:')
    print(s.count('у'))
else:
    print('буквы "у" нет')
if s.isalpha()== False:
    print(s.upper())
l=len(s)
if l>4:
    print(s.lower())
print(s.replace(s[0],'O'))
