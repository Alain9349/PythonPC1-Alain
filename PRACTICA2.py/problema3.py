n=1
par=impar=0

while n != 0:
    n = int(input("Desea ingresar un numero: "))
    if n > 0:
        if n % 2 == 0:
            par +=1
        else:
            impar +=1
    if n == 0:
        break
print(" La cantidad de total de numero pares es: ", par)
print(" La cantidad de total de numero impares es: ", impar)



