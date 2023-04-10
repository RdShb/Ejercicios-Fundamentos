lista = []
nuevalista = []
n = int(input("Cuantos palabras quiere introducir en la lista? "))
  
for i in range(0, n):
    ele = input()
    lista.append(ele) 
for palabra in lista:
    if "a" in palabra or "e" in palabra or "i" in palabra or "o" in palabra or "u" in palabra:
        nuevalista.append(palabra)
print(lista)
print(nuevalista)
