def pyrforloop(numb):
    for number in range(1, numb):
        print(number*'*')
    for number in range(numb, 0, -1):
        print(number*'*')


def pyrwhileloop(numb):
    number = 1
    while number < numb:
        print(number*'*')
        number += 1
    while number > 0 and numb != 0:
        print(number*'*')
        number -= 1


def pyrforloopreverse(numb):
    for number in range(1, numb):
        print((numb-number)*' '+number*'*')
    for number in range(numb, 0, -1):
        print((numb-number)*' '+number*'*')


def pyrwhileloopreverse(numb):
    number = 1
    while number < numb:
        print((numb-number)*' '+number*'*')
        number += 1
    while number > 0 and numb != 0:
        print((numb-number)*' '+number*'*')
        number -= 1



size = int(input('Hoe groot? '))
pyrwhileloopreverse(size)
