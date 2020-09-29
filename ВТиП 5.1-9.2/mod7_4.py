def f(x):
    """запускается при неудаче"""
    print('Повторите еще раз')
    v=int(input())
    if v!=x:
        f(x)
    else:
        print('Победа')
    return v
if __name__ == "__main__":
    print('введите число от 1 до 10)')
    from random import randint
    x=randint(1,10)
    y=int(input())
    if x!=y:
        f(x)
    else:
        print('Победа')

