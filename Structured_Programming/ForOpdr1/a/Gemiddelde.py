def averlist(lst):
    return sum(lst)/len(lst)


def averlistlist(lst):
    averagelist = []
    for list in lst:
        averagelist.append(averlist(list))
    return averagelist


lst = [[1,2,3,4,1121,2,46],[12,4,65,123,67,32,13,4,5,8],[1,23,4,6,13,4,7,2]]
lst2 = [1,3,5,1,3,3,5,61212,123,3]
print('Gemiddelde: {}'.format(averlistlist(lst)))