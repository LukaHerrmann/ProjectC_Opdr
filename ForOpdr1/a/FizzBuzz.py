def fizzbuzz():
    for number in range(1, 101):
        if number % (3*5) == 0:
            number = 'fizzbuzz'
        elif number % 3 == 0:
            number = 'fizz'
        elif number % 5 == 0:
            number = 'buzz'
        print(number)


fizzbuzz()