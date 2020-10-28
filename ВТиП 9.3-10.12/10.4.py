from random import randint
rand=randint(1,5)
t=False
x=int(input('введите число'))
if x==rand:
    print('Победа')
else:
    while t==False:
        if x>rand:
            print('меньше,попробуйте еще)')
            x=int(input('введите число'))
            if x==rand:
                t=True                
        else:
            print('больше,попробуйте еще)')
            x=int(input('введите число'))
            if x==rand:
                t=True 
print('Победа')
    
