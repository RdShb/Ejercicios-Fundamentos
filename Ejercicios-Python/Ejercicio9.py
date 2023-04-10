palabra = input("Escriba una palabra: ")
palindromo = []
cont = 0
for i in range(len(palabra) , 0, -1):
    palindromo.append(palabra[i-1])
for j in palabra:
    if palabra[i] == palindromo[1]:
        cont = cont +1
if cont == len(palabra):
    print("Es palindromo")
else:
    print ("No es palindromo")