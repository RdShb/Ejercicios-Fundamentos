cadena = input("Escriba una cadena de caracteres: ")
palabra = input("Escriba una palabra: ")
palabrareemplazo = input("Escriba una palabra para reemplazar la palabra anterior: ")
indice = cadena.find(palabra)
while indice != -1:
    cadena = cadena[:indice] + palabrareemplazo + cadena[indice+len(palabra):]
    indice = cadena.find(palabra)
print(cadena)