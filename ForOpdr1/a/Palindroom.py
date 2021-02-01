def palchecklib(string):
    reversed = string[::-1]
    if reversed == string:
        return True
    else:
        return False


def palcheck(string):
    reversed = ''
    for ind in range(1, len(string)+1):
        reversed += string[-ind]
    if reversed == string:
        return True
    else:
        return False


string = input('Geef een woord: ')
print('Dit is een palindroom: {}'.format(palcheck(string)))