vocales = {"a", "e", "i", "o", "u", "A", "E", "I", "O","U"}
palabra = input("Escriba aqui una palabra: ")
palabra_sin_vocales = "".join(nv for nv in palabra if nv not in vocales)
print(palabra_sin_vocales)

