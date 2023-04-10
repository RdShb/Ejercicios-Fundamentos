lista = []
nuevalista = []
n = int(input("Cuantos palabras quiere introducir en la lista? "))
  
for i in range(0, n):
    ele = int(input())
    lista.append(ele) 
for numero in lista:
    if numero % 3 == 0:
        nuevalista.append(numero)
print(lista)
print(nuevalista)

