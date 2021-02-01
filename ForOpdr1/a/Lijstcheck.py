def count(lst, target):
    freq = 0
    for number in lst:
        if number == target:
            freq += 1
    return freq


def biggestdiff(lst):
    biggest = 0
    for number in range(len(lst)-1):
        diff = abs(lst[number]-lst[number+1])
        if diff > biggest:
            biggest = diff
    return biggest


def checklst(lst):
    ones = count(lst, '1')
    zeros = count(lst, '0')
    if ones <= zeros:
        return False
    if zeros > 12:
        return False
    return True


list = input('Geef een lijst van eenen en nullen: ').split(',')
print('Deze lijst voldoet: {}'.format(checklst(list)))