def averlist(lst):
    return sum(lst)/len(lst)


def averlistlist(lst):
    averagelist = []
    for list in lst:
        averagelist.append(averlist(list))
    return averagelist


lst = input('Geef een lijst: '.split(','))
