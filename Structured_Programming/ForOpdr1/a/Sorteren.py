def sort(lst):
    for ind in range(len(lst)):
        if ind > 0 and lst[ind] < lst[ind-1]:
            unsolved = True
            while unsolved:
                if ind > 0 and lst[ind] < lst[ind-1]:
                    lst[ind], lst[ind-1] = lst[ind-1], lst[ind]
                    ind -= 1
                else:
                    unsolved = False
    return lst


list = input('Geef een lijst: ').split(',')
intlist = []
for item in list:
    intlist.append(int(item))
print('De gesorteerde lijst: {}'.format(sort(intlist)))