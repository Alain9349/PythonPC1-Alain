nombre_de_usuario= input( "Introducir su nombre: ")
archivo = input( "Si el nombre del archivo termina en : ")
if archivo.endswith(".gif"):
    Mime_type="image/gif"
elif archivo.endswith(".jpg"):
    Mime_type="image/jpeg"
elif archivo.endswith(".jpge"):
    Mime_type="image/jpeg"
elif archivo.endswith(".png"):
    Mime_type="image/png"
elif archivo.endswith(".pdf"):
    Mime_type="application/pdf"
elif archivo.endswith(".text"):
    Mime_type="text/plain"
elif archivo.endswith(".zip"):
    Mime_type="application/zip"
else:
    Mime_type="application/octet-stream"

print( "El tipo de archivo MIME es: ",Mime_type)


