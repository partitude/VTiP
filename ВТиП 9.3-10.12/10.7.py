text = 'мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
print(' '.join([ word for word in text.split() if not word.startswith('м') ]))
