from random import randint

possible = list(range(5))
answer = randint(1,possible[-1])

guess = False

print('\n'*30)
while guess != answer:
    guess = int(input("Hvor er spøgelset? Bag dør {}? [{}]".format(', '.join([str(pos) for pos in possible]) , possible[0])) or possible[0])
    if not guess in possible:
        print('Ikke muligt')
        continue
    possible.remove(guess)
    
    if guess == answer:
        print('''
     .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'
''')
    else:
        print('''
─────────────────▄████▄
─────▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
───▄▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄
──▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
──▐░░██████░░███████░░█████░░░██████░░▌
──▐░░██░░░░░░░░██░░░░██░░░██░░██░░░██░▌
──▐░░██████░░░░██░░░░██░░░██░░██████░░▌
──▐░░░░░░██░░░░██░░░░██░░░██░░██░░░░░░▌
──▐░░██████░░░░██░░░░░████░░░░██░░░░░░▌
──▐░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌
───▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▀
─────▀▀▀▀▀▀▀▀▀▀▀▀██████▀▀▀▀▀▀▀▀▀▀▀▀▀
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
──────────────────█▀▀█
─────────────────█▀▀▀▀█
─────────────────█▀▀▀▀█
─────────────────█▀▀▀▀█
─────────────────█▀▀▀▀█
─────────────────▀████▀ 
''')

