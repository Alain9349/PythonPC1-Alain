def fibonacci (n):
    serie_fibonacci =[0,1]
    if n==0:
        return None
    if n==1:
        return 0
    elif n==2:
        return serie_fibonacci
    else:
        for x in range (2,n):
            serie_fibonacci.append(serie_fibonacci[x-1]+serie_fibonacci[x-2])
    return serie_fibonacci
print(fibonacci(10))

