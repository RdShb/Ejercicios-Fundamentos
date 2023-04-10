##El codigo suma todos los numeros anteriores a n, sin sumar el propio n
n = int(input("Ingrese un numero: "))
total = 0
for i in range(n):
    total = total + i
print(total)
