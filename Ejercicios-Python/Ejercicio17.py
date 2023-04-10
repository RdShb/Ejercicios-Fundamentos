import random

rand = (random.randint(0,100))
n = int(input("Adivine el numero: "))
while n != rand:
    if n < rand:
        print ("El numero es mayor")
        n = int(input("Adivine el numero: "))
    else:
        print ("El numero es menor")
        n = int(input("Adivine el numero: "))
print (f"El numero es {rand}")
