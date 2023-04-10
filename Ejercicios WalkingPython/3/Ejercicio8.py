lista = []
nuevalista = []
n = int(input("Cuantos palabras quiere introducir en la lista?"))
  
for i in range(0, n):
    ele = input()
    lista.append(ele) 
for palabra in lista:
    if len(palabra) > 5:
        nuevalista.append(palabra) 
print(f"Las palabras con 5 letras o menos son: {lista}")
print(f"Las palabras con mas de 5 letras son: {nuevalista}")

