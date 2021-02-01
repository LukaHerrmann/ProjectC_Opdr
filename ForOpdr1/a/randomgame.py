import random
def makegame(range):
    randomnumb = random.randint(0, range)
    while True:
        guess = int(input('Geef een willekeurig getal: '))
        if guess == randomnumb:
            print('Goed geraden!')
            break
        else:
            print('Verkeerd')


range = int(input('Geef een bereik: '))
makegame(range)