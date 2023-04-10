lista = []
total = 0
n = int(input("Ingrese la cantidad de numeros en la lista: "))
for i in range(0, n):
    ele = int(input())
    lista.append(ele) 
for j in lista:
    total = total + j
total = total/len(lista)
print(total)