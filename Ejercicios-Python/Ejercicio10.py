lista = []

n = int(input("Cuantos nombres quiere introducir en la lista? "))
  
for i in range(0, n):
    ele = input()
    lista.append(ele)  
print (sorted(lista))
