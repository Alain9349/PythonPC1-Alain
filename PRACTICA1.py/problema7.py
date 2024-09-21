N1 = float(input("Introduce primer número: ") )
N2 = float(input("Introduce segundo número: ") )
opcion = 0
           
print("¿Qué alternativa eliges?")
opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("La suma de",N1,"+",N2,"es",N1+N2)
elif opcion == 2:
    print("La resta de",N1,"-",N2,"es",N1-N2)
elif opcion == 3:
    print("El producto de",N1,"*",N2,"es",N1*N2)
else:
    print("Opción inválida")