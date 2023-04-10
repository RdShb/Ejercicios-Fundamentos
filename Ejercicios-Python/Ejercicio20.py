n = int(input("Ingrese un numero: "))
numinv = []*10
num = [int(x) for x in str(n)]
for i in reversed(num):
    numinv.append(i)
if num == numinv:
    print("El numero es capicua!")
else:
    print("El numero no es capicua")