lista = []

n = int(input("Cuantos numeros quiere introducir en la lista? "))
  
for i in range(0, n):
    ele = int(input())
    lista.append(ele)  
menor = 0
mayor = 0
for i in lista:
    if i < menor:
        menor = i
    if i > mayor:
        mayor = i
print (mayor)
print (menor)
