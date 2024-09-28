resultado = []
for n in range(1500,2701):
   if n % 7 == 0 and n % 5 == 0:
      resultado.append(n)
print("Los numeros que son divisibles por 7 y multiplos de 5 entre 1500 y 2700 son: ") 
print(resultado)


