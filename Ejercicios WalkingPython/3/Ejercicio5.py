palabra = input("Escriba una palabra: ")
rpalabra = []
for i in range(len(palabra) , 0, -1):
    rpalabra.append(palabra[i-1])
print(f"Tu palabra es: {palabra}")
print(f"Tu palabra invertida es : {rpalabra}")