text = 'Мой дядя самых честных  правил Когда не в шутку занемог Он уважать себя заставил И лучше выдумать не мог'
print(text)
maximum = 0
x=0
for index,word in enumerate(text.split()):
    if len(word) > maximum:
        maximum = len(word)
        print (word)
        x1=x
    x=x+1
print(f'В самом длинном слове {maximum} букв и это {x1+1} слово')
