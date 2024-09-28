for i in range (1,1000):
    x=2
    residuo = 0
    while x <=i:
        if i % x == 0:
            residuo+= i // x
        x +=1
    if residuo == i:
        print(i)



   




