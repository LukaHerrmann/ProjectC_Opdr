def cyclic(ch, n):
    return str(ch)[n:] + str(ch)[:n]


print(cyclic(1011000, 3))
print(cyclic(1011100, -4))