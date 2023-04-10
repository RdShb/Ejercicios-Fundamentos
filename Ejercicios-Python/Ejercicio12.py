n = int(input("Ingrese un numero: "))
if n < 2:
    print("No es primo!")
for i in range(2, int(n)):
    if n % i == 0:
        print("No es primo!")
        quit()
print("Es primo")