lista_alumnos={}
for alumno in range (2):
    nombre=input("Ingrese el nombre del alumno: ")
    asignatura=input("Ingrese la asignatura: ")
    nota1=int(input("Ingresa la primera nota: "))
    nota2=int(input("Ingresa la segunda nota: "))
    nota3=int(input("Ingresa la tercera nota: "))
    lista_alumnos[nombre]= [nota1,nota2,nota3]
for alumno, value in lista_alumnos.items():
    print(alumno+" "+" ".join(value))




