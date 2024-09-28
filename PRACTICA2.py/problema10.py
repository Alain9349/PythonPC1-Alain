meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato mm/dd/aaaa: ')
cambiar_formato_fecha= fecha.split('/')
fecha_nueva='{}-{}-{}'. format(cambiar_formato_fecha[2],cambiar_formato_fecha[1],cambiar_formato_fecha[0])
print(fecha_nueva)