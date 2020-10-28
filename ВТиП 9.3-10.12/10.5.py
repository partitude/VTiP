x=input("Введите число:")
s = 0
for i in range(len(x)):
 s=s+int(x[i])*int(x[i])
 print(s)
print("сумма чисел:", s)
