def diffind(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    if len1 > len2:
        maxlength = len1
    else:
        maxlength = len2
    for numb in range(maxlength):
        if numb > len1-1 or numb > len2-1:
            return numb
        if string1[numb] != string2[numb]:
            return numb



firststring = input('Geef een string: ')
secondstring = input('Geef een string: ')
print('Het eerste verschil zit op index: {}'.format(diffind(firststring, secondstring)))