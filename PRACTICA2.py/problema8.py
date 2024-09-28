print("Ingrese un numero")
numero=int(input())
fact=1  
for i in range(1,numero+1):
    fact*=i
print("El factorial de", numero,"!","es:", fact)