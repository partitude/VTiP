import random
print('У первого выпало:')
a = random.randint(1, 6)
print(a)
print('У второго выпало:')
b = random.randint(1, 6)
print(b)
if a > b:
    print('Победил первый игрок')
elif a==b:
    print('Ничья')
elif a<b:
    print('Победил второй игрок')
