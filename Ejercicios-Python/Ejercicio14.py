lista = []
totalpar = 0
n = int(input("Ingrese la cantidad de numeros en la lista: "))

for i in range(0, n):
    ele = int(input())
    lista.append(ele) 
for j in lista:
    if j%2 == 0:
        totalpar = totalpar + j
print(totalpar)
