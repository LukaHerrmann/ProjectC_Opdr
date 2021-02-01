def palchecklib(string):
    return string[::-1] == string


def palcheck(string):
    reversed = ''
    for ind in range(1, len(string)+1):
        reversed += string[-ind]
    return reversed == string

string = input('Geef een woord: ')
print('Dit is een palindroom: {}'.format(palcheck(string)))