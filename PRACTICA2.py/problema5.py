numeros_primos=[]
for x in range(1,101):
    cont=0
    for y in range (1,x+1):
        if x%y==0:
            cont+=1
    if cont <=2:
        numeros_primos.append(x)
print (sum(numeros_primos)-1)

