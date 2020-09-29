def ss(s,n):
    if len(s)>n:
        print(s.upper())
    else:
        print(s)
    """Возвращает строку в верхнем регистре если длина строки s больше n"""
if __name__=="__main__":
    s1 =str(input())
    n1=int(input())
    ss(s1,n1)
