lista = []
n = int(input("Ingrese la cantidad de numeros en la lista: "))
for i in range(0, n):
    ele = int(input())
    lista.append(ele)
print (list(set(lista)))