from random import randint, choice
from math import isclose
image_org = '''
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
'''

num_max = 5
image_parts = image_org.split('\n')
image = ''
operator = '__sub__'
operator_dict = {'__add__':'+', '__sub__': '-', '__mul__':'*', '__truediv__':'/'}


while len(image_parts) > 0:
    guess = 2.2
    a,b = randint(1,num_max), randint(1,num_max)
    operator = choice(list(operator_dict.keys())) if a > b else '__add__'
    #while not isinstance(guess,(int,float)):
    try:
        result = eval('a. {}(b)'.format(operator))
        guess = 1e31
        while not isclose(guess , result,rel_tol=0.1):
            guess = float(input('{} {} {} = ? '.format(a,operator_dict[operator],b)))
            if not isclose(guess, result, rel_tol=0.1):
                print('Forkert - prøv igen!')
    except:
        pass#print(e,dir(e))
    else:
        image += '\n' + image_parts.pop(0) if len(image_parts) > 1 else '\nFlot! Du printede hele spøgelset!'
        print(image)
    finally:
        print('finally')
       
##    if isclose(guess , eval('a. {}(b)'.format(operator)),rel_tol=0.1):
##        image += '\n' + image_parts.pop(0)
##        print(image)
##    else:
##        print('Forkert - prøv igen!')

##print('Flot! Du printede hele spøgelset!')
    