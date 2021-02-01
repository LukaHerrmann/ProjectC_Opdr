def fibo(fn, numb1=0, numb2=1):
    if fn > 0:
        return fibo(fn-1, numb2, numb1+numb2)
    return numb1


print(fibo(120))