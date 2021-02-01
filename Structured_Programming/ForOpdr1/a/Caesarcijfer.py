def caesar(string, rotation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newstring = ''
    for character in string:
        index = alphabet.find(character.lower())
        newindex = (index + rotation) % len(alphabet)
        if index == -1:
            newstring += character
        elif character.isupper():
            newstring += alphabet[newindex].upper()
        else:
            newstring += alphabet[newindex]
    return newstring


tobecoded = input('Geef een tekst: ')
rotation = int(input('Geef een rotatie: '))
print('Caesarcode: {}'.format(caesar(tobecoded, rotation)))