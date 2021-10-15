from time import sleep
from words import words
from curtsies.fmtfuncs import yellow, bold
lort = '''
Kim i fare

Kim råber:
"Jeg løber ud i haven."
Kim løber ud.
Han løber ud i haven.
Han falder over en pind.

Kim ligger på jorden.
Han ser sig rundt.
Han tænker:
"Hvor er jeg?
Hvad laver jeg her?"

Gala råber til Kim:
"Pas på mig!
Jeg vil ramme dig."
Kim råber:
"Jeg er ikke bange."

Gala kaster med pinde.
Kim hopper til siden.
Pinden flyver forbi ham.
Gala råber:
"Hvad laver du?"

Kim løber rundt om Gala.
Gala kaster pinde.
Gala kaster mange pinde.
Kim råber til Gala:
"Ram mig!"


Gal løber hem mod kim.
Kim løber væk.
Kim stopper op.
Han råber:
"Nu kan du ramme mig."

Gala kaster en pind.
Pinden rammer ikke Kim.
Den rammer et træ.
Kim råber:
"Tag pinden fra mig."

Gal løber hen mod Kim.
Gala er gal.
Gala vil have pinden.
Kim hopper til side.
Gala drøner forbi.

Gal drøner ind i træet.
Kim ser på Gala.
Kim tænker:
"Gala får ikke pinden.
Gala kan ikke ramme mig."

Kim kaster pinden.
Den rammer et træ.
Så rammer den Kim.
Kim råber:
"Åh nej."

Kim ligger på jorden.
Han er hjemme igen.
Han er i haven.
Han tænker:
"Hvor var jeg henne?"

'''

for line in lort.split('\n'):
    sentence = []
    for word in line.split(' '):
        _word = word.lower().strip('.,:;"!?')
        if _word in words:
            new_word = word[0:word.lower().find(_word)] + str(yellow(_word.upper())) + word[word.lower().find(_word)+len(_word):]
            sentence.append(new_word)
        else: sentence.append(word)
    sentence = ' '.join(sentence)
    print(sentence)
    sleep(0.2*len(line))